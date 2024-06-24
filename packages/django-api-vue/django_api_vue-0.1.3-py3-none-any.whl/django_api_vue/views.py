from django.views import View

from .mixins import ActGetAPIMixin, ModelPostAPIMixin, ModelPutAPIMixin, ModelGetPageAPIMixin, \
    ModelGetListAPIMixin, ModelExportAPIMixin, ModelUploadAPIMixin, ModelDeleteAPIMixin


class BaseView(View):
    pass


class GetView(ActGetAPIMixin, BaseView):
    pass


class PostView(ModelPostAPIMixin, BaseView):
    pass


class PutView(ModelPutAPIMixin, BaseView):
    pass


class GetPageView(ModelGetPageAPIMixin, BaseView):
    pass


class GetListView(ModelGetListAPIMixin, BaseView):
    pass


class TableView(ModelGetPageAPIMixin, ModelExportAPIMixin, ModelUploadAPIMixin, ModelDeleteAPIMixin,
                ModelPutAPIMixin, ModelPostAPIMixin, BaseView):
    pass
