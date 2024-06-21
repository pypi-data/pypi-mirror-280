from django.views import View

from .mixins import ActGetAPIMixin, ModelPostAPIMixin, ModelPutAPIMixin, ModelGetPageAPIMixin, \
    ModelGetListAPIMixin, ModelExportAPIMixin, ModelUploadAPIMixin, ModelDeleteAPIMixin


class BaseView(View):
    pass


class StaffGetView(ActGetAPIMixin, BaseView):
    pass


class StaffPostView(ModelPostAPIMixin, BaseView):
    pass


class StaffPutView(ModelPutAPIMixin, BaseView):
    pass


class StaffGetPageView(ModelGetPageAPIMixin, BaseView):
    pass


class StaffGetListView(ModelGetListAPIMixin, BaseView):
    pass


class StaffTableView(ModelGetPageAPIMixin, ModelExportAPIMixin, ModelUploadAPIMixin, ModelDeleteAPIMixin,
                     ModelPutAPIMixin, ModelPostAPIMixin, BaseView):
    pass
