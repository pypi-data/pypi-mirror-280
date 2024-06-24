import json

from django.db import transaction
from django.db.models import QuerySet, Prefetch
from django.http import StreamingHttpResponse
from django.utils.encoding import escape_uri_path

from .constants import RequestActEnum
from .errors import RequestMethodNotAllowError, RequestActNotAllowError, MyError, MethodNeedRedefinedError
from .fields import BaseRelatedField, ForeignKeyField, ManyToManyField, ReverseForeignKeyField, \
    ModelField, ModelFuncField, AnnotateField, ValueField
from .models import ExportQueryParams
from .params import BaseParam, IntParam, ListParam, DictParam, StrParam, StrAndBoolParam
from .returns import success_return


class CheckParamMixin:

    @staticmethod
    def check_params_list(params_data, params_list: list[BaseParam]):
        res = {}
        for param in params_list:
            value = param.check(params_data)
            if value is not None:
                res[param.get_query_key()] = value
        return res


class GetAPIMixin(CheckParamMixin):

    def get(self, request, *args, **kwargs):
        raise RequestMethodNotAllowError


class PostAPIMixin(CheckParamMixin):
    @staticmethod
    def set_request_data(request):
        if request.content_type == "application/json":
            request.request_data = json.loads(request.body)
        else:
            data_dict = {}
            for key in request.POST:
                values = request.POST.getlist(key)
                data_dict[key] = values if len(values) > 1 else values[0]
            # 从 request.FILES 获取数据
            for key in request.FILES:
                uploaded_files = request.FILES.getlist(key)
                data_dict[key] = uploaded_files if len(uploaded_files) > 1 else uploaded_files[0]
            request.request_data = data_dict

    post_params_list = []

    def check_post_params_list(self, request) -> dict:
        return self.check_params_list(request.request_data, self.post_params_list)

    def post(self, request, *args, **kwargs):
        raise RequestMethodNotAllowError


class ActAPIMixin(PostAPIMixin):
    @staticmethod
    def set_request_act(request):
        request.request_act = request.request_data.pop("act", request.method.lower())

    def api_method_not_allowed(self, request, *args, **kwargs):
        raise RequestMethodNotAllowError

    def post(self, request, *args, **kwargs):
        self.set_request_data(request)
        self.set_request_act(request)
        handle = getattr(self, "%s_api" % request.request_act, self.api_method_not_allowed)
        return handle(request, *args, **kwargs)


class ActGetAPIMixin(ActAPIMixin):
    def get_api(self, request):
        raise RequestActNotAllowError


class ModelAPIMixin:
    model = None


class ModelPostAPIMixin(ModelAPIMixin, ActAPIMixin):
    def handle_post(self, request):
        res = self.check_post_params_list(request)
        with transaction.atomic():
            self.model.objects.create(**res)

    def post_api(self, request):
        self.handle_post(request)
        return success_return()


class ModelPutAPIMixin(ModelAPIMixin, ActAPIMixin):
    put_select_params_list = [
        IntParam(name="pk", must_has_value=True),
    ]
    put_params_list = []

    def check_put_select_params_list(self, request) -> dict:
        return self.check_params_list(request.request_data, self.put_select_params_list)

    def check_put_params_list(self, request) -> dict:
        return self.check_params_list(request.request_data, self.put_params_list)

    def put_db_operation(self, request, select_params: dict, put_params: dict):
        self.model.objects.filter(**select_params).update(**put_params)

    def handle_put(self, request, select_params: dict, put_params: dict):
        if len(select_params.keys()) == 0:
            raise MyError("未查询到需要修改的数据")
        if len(put_params.keys()) == 0:
            raise MyError("未查询到需要修改的内容")
        with transaction.atomic():
            self.put_db_operation(request, select_params, put_params)

    def put_api(self, request):
        select_params = self.check_put_select_params_list(request)
        put_params = self.check_put_params_list(request)
        self.handle_put(request, select_params, put_params)
        return success_return()


class ModelDeleteAPIMixin(ModelAPIMixin, ActAPIMixin):
    delete_params_list = [
        ListParam(name="pk_list", must_has_value=True, list_element=IntParam(name="int"), query_key="pk__in"),
    ]

    def generate_delete_params(self, request) -> dict:
        return self.check_params_list(request.request_data, self.delete_params_list)

    def delete_db_operation(self, request, delete_param: dict):
        self.model.objects.filter(**delete_param).delete()

    def handle_delete(self, request):
        delete_param = self.generate_delete_params(request)
        with transaction.atomic():
            self.delete_db_operation(request, delete_param)

    def delete_api(self, request):
        self.handle_delete(request)
        return success_return()


class ModelGetListAPIMixin(ModelAPIMixin, ActAPIMixin):
    default_get_list_params_list = []  # 无法修改的默认参数列表
    get_list_params_list = [
        ListParam(name="search_list", list_element=DictParam(name="search_list", dict_key_list=[
            DictParam(name="search_key", dict_key_list=[
                StrParam(name="full_name", must_has_value=True),
                StrParam(name="type", must_has_value=True),
            ]),
            DictParam(name="search_way", dict_key_list=[
                StrParam(name="prop", must_has_value=True),
            ]),
            StrAndBoolParam(name="search_value", must_has_value=True),
        ]))
    ]
    orderby_params_list = [
        StrParam(name="order_by"),
    ]
    page_params_list = []

    field_list = []
    annotate_list = []

    def get_related_list(self, field_list, parent_field_name=None, must_prefetch=False):
        select_related_list = []
        prefetch_related_list = []
        for field in field_list:
            if isinstance(field, BaseRelatedField):
                relate_name = f"{parent_field_name}__{field.name}" if parent_field_name else field.name
                if isinstance(field, ForeignKeyField):
                    if must_prefetch:
                        prefetch_related_list.append(Prefetch(relate_name, queryset=getattr(field, 'queryset', None)))
                    else:
                        select_related_list.append(relate_name)
                else:
                    must_prefetch = True
                    prefetch_related_list.append(Prefetch(relate_name, queryset=getattr(field, 'queryset', None)))
                a1, a2 = self.get_related_list(field.field_list, parent_field_name=relate_name,
                                               must_prefetch=must_prefetch)
                select_related_list.extend(a1)
                prefetch_related_list.extend(a2)
        return select_related_list, prefetch_related_list

    def get_obj_value(self, obj, field_list):
        if obj is None:
            return None
        res = {"pk": obj.pk}
        for field in field_list:
            if isinstance(field, ForeignKeyField):
                res[field.name] = self.get_obj_value(getattr(obj, field.name), field.field_list)
            elif isinstance(field, (ManyToManyField, ReverseForeignKeyField)):
                m2m_obj_list = getattr(obj, field.name).all()
                m2m_data_list = []
                for m2m_obj in m2m_obj_list:
                    m2m_data_list.append(self.get_obj_value(m2m_obj, field.field_list))
                res[field.name] = m2m_data_list
            elif isinstance(field, (ModelField, ModelFuncField, AnnotateField)):
                res.update(field.get_field_value(obj))
            elif isinstance(field, ValueField):
                res.update(field.get_field_value())
            else:
                continue
        return res

    @staticmethod
    def change_way(way):
        res = {
            "start": "__startswith",
            "end": "__endswith",
            "contain": "__contains",
            "gte": "__gte",
            "lte": "__lte",
            "isnull": "__isnull",
            "notnull": "__isnull",
        }
        return res.get(way, "")

    @staticmethod
    def process_search(search):
        key_value = search.get("search_key", {}).get("full_name")
        key_type = search.get("search_key", {}).get("type", "")
        way_value = search.get("search_way", {}).get("prop")
        search_value = search.get("search_value", "")

        if key_type == "DateTime":
            key_value = f"{key_value}__date"
        if way_value == "isnull":
            search_value = True
        elif way_value == "notnull":
            search_value = False

        return key_value, way_value, search_value

    def generate_query_params(self, request) -> dict:
        query_params = {}

        get_param = self.check_params_list(request.request_data, self.get_list_params_list)
        search_list = get_param.get("search_list", [])

        for search in search_list:
            key_value, way_value, search_value = self.process_search(search)

            if way_value != "not-same":
                query_key = f"{key_value}{self.change_way(way_value)}"
                query_params[query_key] = search_value

        return query_params

    def generate_exclude_params(self, request):
        exclude_params = {}

        get_param = self.check_params_list(request.request_data, self.get_list_params_list)
        search_list = get_param.get("search_list", [])

        for search in search_list:
            key_value, way_value, search_value = self.process_search(search)
            if way_value == "not-same":
                if key_value in exclude_params.keys():
                    origin_search_value = exclude_params.pop(key_value)
                    exclude_params[f"{key_value}__in"] = [origin_search_value, search_value, ]
                elif f"{key_value}__in" in exclude_params.keys():
                    exclude_params[f"{key_value}__in"].append(search_value)
                else:
                    exclude_params[key_value] = search_value

        return exclude_params

    def get_queryset(self, request):
        query_params = self.generate_query_params(request)
        query_params.update(self.check_params_list(request.request_data, self.default_get_list_params_list))
        exclude_params = self.generate_exclude_params(request)
        queryset: QuerySet = self.model.objects.filter(**query_params).exclude(**exclude_params)
        select_related_list, prefetch_related_list = self.get_related_list(self.field_list)
        if select_related_list:
            queryset = queryset.select_related(*select_related_list)
        if prefetch_related_list:
            queryset = queryset.prefetch_related(*prefetch_related_list)
        annotate_res = {}
        for field in self.field_list:
            if isinstance(field, AnnotateField):
                annotate_res[field.name] = field.func
        if annotate_res:
            queryset = queryset.annotate(**annotate_res)
        orderby_param = self.check_params_list(request.request_data, self.orderby_params_list)
        order_by = orderby_param.get("order_by", None)
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset

    def get_header_list(self):
        header_list = []
        for field in self.field_list:
            if isinstance(field,
                          (ModelField, ForeignKeyField, ManyToManyField, ReverseForeignKeyField, AnnotateField,
                           ValueField, ModelFuncField)):
                header_list.append(field.get_header_data())
        return header_list

    def base_get_data(self, request):
        queryset = self.get_queryset(request)
        total = queryset.count()
        if request.request_act == RequestActEnum.get_page.name:
            page_param = self.check_params_list(request.request_data, self.page_params_list)
            offset = page_param.get("offset", None)
            limit = page_param.get("limit", None)
            if all(map(lambda x: isinstance(x, int), (offset, limit))):
                queryset = queryset[offset: offset + limit]

        data_list = []
        for obj in queryset:
            data_list.append(self.get_obj_value(obj, field_list=self.field_list))
        res = {
            "total": total,
            "header_list": self.get_header_list(),
            "data_list": data_list,
        }
        return res

    def get_one_data(self, data, header_list):
        data_list = []
        if not isinstance(data, dict):
            data = {}
        for header in header_list:
            name = header.get("name", "")
            children = header.get("children", [])
            if children:
                child_data = data.get(name, {})
                data_list.extend(self.get_one_data(child_data, children))
            else:
                data_list.append(data.get(name, "") if data else "")
        return data_list

    def get_list_api(self, request):
        res = self.base_get_data(request)
        return success_return(res)


class ModelExportAPIMixin(ModelGetListAPIMixin, ActAPIMixin, GetAPIMixin):
    pass

    # sheet = None
    # max_depth = 0
    #
    # header_font = Font(bold=True)
    # alignment = Alignment(horizontal='center', vertical='center')
    #
    # def get_max_depth(self, header_list, current_depth=1):
    #     max_depth = current_depth
    #     for header in header_list:
    #         if 'children' in header:
    #             depth = self.get_max_depth(header['children'], current_depth + 1)
    #             max_depth = max(max_depth, depth)
    #     return max_depth
    #
    # def get_max_width(self, header):
    #     max_width = 0
    #     children = header.get("children", [])
    #     if not children:
    #         return max_width
    #     max_width += len(children)
    #     for child in children:
    #         max_width += self.get_max_width(child) - 1
    #     return max_width
    #
    # def write_header(self, header_list, start_row=1, start_column=1):
    #     for inx, header in enumerate(header_list):
    #         label = header['label']
    #         children = header.get("children", [])
    #         if children:
    #             self.sheet.merge_cells(start_row=start_row, end_row=start_row,
    #                                    start_column=start_column, end_column=start_column + self.get_max_width(header))
    #             self.sheet.cell(start_row, start_column, label).font = self.header_font
    #             self.sheet.cell(start_row, start_column, label).alignment = self.alignment
    #             self.write_header(children, start_row=start_row + 1, start_column=start_column)
    #             start_column = start_column + self.get_max_width(header)
    #         else:
    #             self.sheet.merge_cells(start_row=start_row, end_row=self.max_depth,
    #                                    start_column=start_column, end_column=start_column)
    #             self.sheet.cell(start_row, start_column, label).font = self.header_font
    #             self.sheet.cell(start_row, start_column, label).alignment = self.alignment
    #             start_column += 1
    #
    # def write_data(self, data_list, header_list):
    #     for data in iter(data_list):
    #         one_row = self.get_one_data(data, header_list)
    #         one_row = [json.dumps(i) if isinstance(i, (list, dict)) else i for i in one_row]
    #         self.sheet.append(one_row)

    def flatten_header_list(self, header_list):
        flat_list = []
        for header in header_list:
            # 递归处理子层级
            if "children" in header:
                flat_list.extend(self.flatten_header_list(header["children"]))
            else:
                flat_list.append(header)

        return flat_list

    # def stream_response_generator(self, header_list):
    #     print(self.get_csv_header_list(header_list))
    #     yield self.get_csv_header_list(header_list)

    @staticmethod
    def get_nested_data(data, keys):
        """ 辅助函数，用于通过键列表访问嵌套字典中的数据 """
        for key in keys:
            if isinstance(data, dict) and key in data:
                data = data[key]
            else:
                return ""  # 如果路径无效或数据不是字典，则返回空字符串
        return data

    def stream_response_generator(self, request):
        uuid = request.GET.get("uuid", "")
        export_query_params = ExportQueryParams.objects.get(uuid=uuid)
        request.request_data = export_query_params.query_params
        request.request_act = RequestActEnum.export.name
        queryset = self.get_queryset(request)

        # Yield UTF-8 BOM
        yield '\ufeff'

        # Prepare the header
        header_list = self.flatten_header_list(self.get_header_list())
        header_row = ','.join([header['full_label'] for header in header_list]) + '\n'
        yield header_row

        # Process each row in the queryset
        for row in queryset.iterator():
            row_data = self.get_obj_value(row, field_list=self.field_list)
            data_list = []
            for header in header_list:
                data = self.get_nested_data(row_data, header['full_name'].split("__"))
                data_list.append(str(data))  # Convert data to string
            row_str = ','.join(data_list) + '\n'
            yield row_str

    # def stream_response_generator(self, request):
    #     uuid = request.GET.get("uuid", "")
    #     export_query_params = ExportQueryParams.objects.get(uuid=uuid)
    #     request.request_data = export_query_params.query_params
    #     request.request_act = RequestActEnum.export.name
    #     queryset = self.get_queryset(request)
    #     # 使用 StringIO 作为临时的文件类对象
    #     pseudo_buffer = io.StringIO()
    #     writer = csv.writer(pseudo_buffer)
    #     # 写入UTF-8 BOM
    #     yield '\ufeff'
    #     header_list = self.flatten_header_list(self.get_header_list())
    #     writer.writerow([header['full_label'] for header in header_list])
    #     # 移动到缓冲区的开始
    #     pseudo_buffer.seek(0)
    #     header_data = pseudo_buffer.getvalue()
    #     # 清空缓冲区以备下一行使用
    #     pseudo_buffer.seek(0)
    #     pseudo_buffer.truncate(0)
    #     # 生成器yield数据
    #     yield header_data
    #     for row in queryset.iterator():
    #         row_data = self.get_obj_value(row, field_list=self.field_list)
    #         data_list = []
    #         for header in header_list:
    #             data = row_data
    #             for name in header['full_name'].split("__"):
    #                 data = data.get(name)
    #             data_list.append(data)
    #         writer.writerow(data_list)
    #         # 移动到缓冲区的开始
    #         pseudo_buffer.seek(0)
    #         row_data = pseudo_buffer.getvalue()
    #         # 清空缓冲区以备下一行使用
    #         pseudo_buffer.seek(0)
    #         pseudo_buffer.truncate(0)
    #         # 生成器yield数据
    #         yield row_data

    def get(self, request, *args, **kwargs):
        # 设置响应内容类型为CSV文件
        response = StreamingHttpResponse(self.stream_response_generator(request), content_type="text/csv")
        response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(
            escape_uri_path("%s.csv" % self.model._meta.verbose_name))
        return response

        # uuid = request.GET.get("uuid", "")
        # export_query_params = ExportQueryParams.objects.get(uuid=uuid)
        # response = StreamingHttpResponse(content_type='application/ms-excel')
        # response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(escape_uri_path("导出测试.xlsx"))
        # response['Content-Filename'] = escape_uri_path("%s.xlsx" % self.model._meta.verbose_name)
        # wb = Workbook()  # optimized_write=True
        # self.sheet = wb.active
        # request.request_data = export_query_params.query_params
        # request.request_act = RequestActEnum.export.name
        # res = self.base_get_data(request)
        # header_list = res.get("header_list", [])
        # data_list = res.get("data_list", [])
        # self.max_depth = self.get_max_depth(header_list)
        # self.write_header(header_list)
        # self.write_data(data_list, header_list)
        # wb.save(response)
        # wb.close()
        # return response

    def export_api(self, request):
        export_query_params = ExportQueryParams.objects.create(query_params=request.request_data)
        return success_return({
            "uuid": export_query_params.uuid
        })


class ModelUploadAPIMixin(ModelAPIMixin, ActAPIMixin):
    upload_params_list = []

    def check_upload_params_list(self, request_data) -> dict:
        return self.check_params_list(request_data, self.upload_params_list)

    def upload_api(self, request):
        raise MethodNeedRedefinedError


class ModelGetPageAPIMixin(ModelGetListAPIMixin, ActAPIMixin):
    page_params_list = [
        IntParam(name="offset", default_value=0),
        IntParam(name="limit", default_value=20, max_value=100),
    ]

    def get_page_api(self, request):
        res = self.base_get_data(request)
        return success_return(res)
