from .constants import DateTimeFormatEnum
from .errors import MethodNeedRedefinedError


class BaseReturnField(object):
    def __init__(self, name, label, width=150, field_type=None, is_slot=False, is_copy=False, is_show=True,
                 is_search=True, choices=None, is_sort=False):
        if width is not None:
            width = max(len(label) * 20, width)
        self.width = width  # 字段 宽度
        self.is_slot = is_slot  # 字段 是否使用插槽处理
        self.is_copy = is_copy  # 字段 是否可复制
        self.name = name  # 字段 名称
        self.label = label  # 字段 标签
        self.field_type = field_type  # 字段 类型
        self.choices = choices  # 字段 可选项
        self.is_show = is_show  # 字段是否显示
        self.is_search = is_search  # 字段是否可搜索
        self.full_name = name  # 字段完整名称
        self.full_label = label  # 字段完整标签
        self.is_sort = is_sort  # 字段 是否可排序
        # 当有可选项时，字段类型设置为Choice
        if self.choices:
            self.field_type = "Choice"
        if self.is_show is False:
            self.is_search = False

    def set_full_info(self, parent=None):
        self.full_label = f"{parent.full_label}{self.label}" if parent else self.label
        self.full_name = f"{parent.full_name}__{self.name}" if parent else self.name

    def get_header_data(self, parent=None):
        self.set_full_info(parent)
        return {
            "label": self.label,
            "name": self.name,
            "full_label": self.full_label,
            "full_name": self.full_name,
            "width": self.width,
            "is_slot": self.is_slot,
            "is_sort": self.is_sort,
            "is_copy": self.is_copy,
            "is_show": self.is_show,
            "is_search": self.is_search,
            'type': self.field_type,
            'choices': self.choices,
        }

    def get_field_value(self):
        raise MethodNeedRedefinedError


class ValueField(BaseReturnField):
    def __init__(self, value, field_type, *args, **kwargs):
        self.value = value
        super().__init__(field_type=field_type, *args, **kwargs)

    def get_field_value(self):
        return {
            self.name: self.value
        }


class AnnotateField(BaseReturnField):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        super().__init__(*args, **kwargs)

    def get_field_value(self, obj=None):
        """获取字段的值"""
        return {
            self.name: getattr(obj, self.name, "")
        }


class ModelField(BaseReturnField):

    def __init__(self, model_field, is_search=True, datetime_format=None, choices=None, *args, **kwargs):
        self.model_field = model_field.field
        self.datetime_format = datetime_format
        label = kwargs.pop("label", None)
        width = kwargs.get("width", None)
        if width is None:
            if self.datetime_format == DateTimeFormatEnum.day_time:
                kwargs['width'] = 200
        super().__init__(name=self.model_field.name, label=self.model_field.verbose_name if label is None else label,
                         field_type=self.model_field.__class__.__name__[:-5], is_search=is_search,
                         choices=choices if choices else getattr(self.model_field, "choices", None), *args, **kwargs)
        if self.datetime_format is not None:
            self.is_sort = True

    def get_field_value(self, obj=None):
        """获取字段的值"""
        field_value = None
        if obj is not None:
            if self.choices:
                field_value = getattr(obj, 'get_%s_display' % self.model_field.name)()
            else:
                field_value = getattr(obj, self.model_field.name)
                if field_value and self.datetime_format:
                    field_value = field_value.strftime(self.datetime_format.value)
        return {
            self.name: field_value
        }


class ModelFuncField(BaseReturnField):
    def __init__(self, func, *args, **kwargs):
        self.func = func
        super().__init__(*args, **kwargs)

    def get_field_value(self, obj=None):
        """获取字段的值"""
        return {
            self.name: getattr(obj, self.func.__name__)()
        }


class BaseRelatedField(BaseReturnField):
    def __init__(self, field_list: list[BaseReturnField], *args, **kwargs):
        self.field_list = field_list
        super().__init__(field_type="Related", is_search=False, *args, **kwargs)

    def get_header_data(self, parent=None):
        res = super().get_header_data(parent=parent)
        res['children'] = [
            child_field.get_header_data(self) for child_field in self.field_list
        ]
        return res


class ForwardRelatedField(BaseRelatedField):

    def __init__(self, model_field, field_list, is_slot=False, *args, **kwargs):
        field = model_field.field
        # if len(field_list) == 1:
        #     is_slot = True
        super().__init__(name=field.name, label=field.verbose_name, field_list=field_list, is_slot=is_slot, *args,
                         **kwargs)


class ReverseRelatedField(BaseRelatedField):

    def __init__(self, model_field, field_list, label=None, queryset=None, *args, **kwargs):
        field = model_field.field
        self.queryset = queryset
        if label is None:
            label = field.verbose_name
        super().__init__(name=field._related_name, label=label, field_list=field_list, *args, **kwargs)


class ForeignKeyField(ForwardRelatedField):
    pass


class ManyToManyField(ForwardRelatedField):
    pass


class ReverseForeignKeyField(ReverseRelatedField):
    pass
