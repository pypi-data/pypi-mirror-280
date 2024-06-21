from .enums import BaseEnum, TwoValueEnum


class RequestActEnum(BaseEnum):
    login = "login"
    GET = "get"
    get_list = "get_list"
    get_page = "get_page"
    export = "export"
    download = "download"
    upload = "upload"
    post = "post"
    put = "put"
    delete = "delete"


class DateTimeFormatEnum(TwoValueEnum):
    day = ("%Y-%m-%d", "日期")
    time = ("%H:%M:%S", "时间")
    day_time = ("%Y-%m-%d %H:%M:%S", "日期时间")
