import uuid

from django.db import models


def get_mysql_default_dict():
    return {}


def get_mysql_default_list():
    return []


class ExportQueryParams(models.Model):
    uuid = models.UUIDField(verbose_name="唯一码", default=uuid.uuid4, unique=True)
    query_params = models.JSONField(verbose_name="查询参数", default=get_mysql_default_dict)

    class Meta:
        db_table = "export_query_params"
        verbose_name = "导出时的查询数据"
        ordering = ("-id",)
