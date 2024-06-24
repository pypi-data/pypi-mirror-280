import datetime
from typing import List

from django.core.files.uploadedfile import UploadedFile

from .constants import DateTimeFormatEnum
from .errors import ParamEmptyError, ParamTypeError, ParamRangeError, ParamFormatError


class BaseParam(object):
    type_list = []  # 允许的参数类型列表

    def __init__(self, name=None, desc=None, model_field=None, must_has_value: bool = False, default_value=None,
                 query_key=None):
        desc = desc if desc else name
        self.name = name if name else model_field.field.name
        self.desc = desc if desc else model_field.field.verbose_name
        self.must_has_value = must_has_value
        self.default_value = default_value
        self.query_key = query_key

    def get_query_key(self):
        return self.query_key if self.query_key else self.name

    def get_expect_type(self):
        """获取期望的数据类型"""
        return " or ".join([t.__name__ for t in self.type_list])

    def get_desc(self, parent_field=None):
        """获取显示的字段名称，优先显示desc"""
        show_name = self.desc
        if parent_field:
            parent_show_name = parent_field.get_desc()
            show_name = parent_show_name + "的" + show_name
        return show_name

    def extra_check_value(self, value, parent_field=None):
        """额外的检验方法"""
        return value

    @staticmethod
    def check_empty_value(value):
        if value is None:
            return True
        value_type = type(value)
        if value_type == str:
            return not value
        return False

    def check(self, data: dict, parent_field=None):
        value = data.get(self.name, self.default_value)
        show_name = self.get_desc(parent_field)
        if self.must_has_value:
            if self.check_empty_value(value):
                raise ParamEmptyError(show_name)
        if value:
            if self.type_list and any(map(lambda x: isinstance(value, x), self.type_list)) is False:
                raise ParamTypeError(show_name)
        value = self.extra_check_value(value, parent_field=parent_field)
        return value

    def __str__(self):
        key_list = [self.name]
        if self.desc:
            key_list.append(self.desc)
        return "-".join(key_list)


class IntParam(BaseParam):
    type_list = [int, str]

    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_value = min_value
        self.max_value = max_value

    def check_and_convert_value(self, value, conversion_type, parent_field=None):
        if isinstance(value, str):
            try:
                value = conversion_type(value)
            except ValueError:
                raise ParamTypeError(self.get_desc(parent_field))

        if self.min_value is not None and value < self.min_value:
            raise ParamRangeError(self.get_desc(parent_field))
        if self.max_value is not None and value > self.max_value:
            raise ParamRangeError(self.get_desc(parent_field))
        return value

    def extra_check_value(self, value, parent_field=None):
        return self.check_and_convert_value(value, int, parent_field)


class FloatParam(IntParam):
    type_list = [float, int, str]

    def extra_check_value(self, value, parent_field=None):
        return self.check_and_convert_value(value, float, parent_field)


class StrParam(BaseParam):
    type_list = [str, ]

    def __init__(self, min_length=None, max_length=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def extra_check_value(self, value, parent_field=None):
        if value:
            # 检查字符串长度是否在给定的范围内
            if self.min_length is not None and len(value) < self.min_length:
                raise ValueError(
                    f"String length for {self.name} is less than the minimum required length of {self.min_length}.")
            if self.max_length is not None and len(value) > self.max_length:
                raise ValueError(
                    f"String length for {self.name} exceeds the maximum allowed length of {self.max_length}.")

        return value


class StrAndBoolParam(BaseParam):
    type_list = [str, bool, int]


class ListParam(BaseParam):
    """
    list_element is must_has_value arg
    """

    type_list = [list, ]

    def __init__(self, list_element, min_length=None, max_length=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_element = list_element
        self.min_length = min_length
        self.max_length = max_length

    def extra_check_value(self, value, parent_field=None):
        if value:
            # 检查列表长度是否在给定的范围内
            if self.min_length is not None and len(value) < self.min_length:
                raise ValueError(f"The list length is less than the minimum required length {self.min_length}.")
            if self.max_length is not None and len(value) > self.max_length:
                raise ValueError(f"The list length exceeds the maximum allowed length {self.max_length}.")

            new_list = []
            for inx, v in enumerate(value):
                new_v = self.list_element.check(data={self.list_element.name: v}, parent_field=self)
                new_list.append(new_v)
            value = new_list
        return value


class DictParam(BaseParam):
    """
    dict_key_list is must_has_value arg
    """
    type_list = [dict, ]

    def __init__(self, dict_key_list: list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_key_list = dict_key_list

    def extra_check_value(self, value, parent_field=None) -> dict:
        if value is not None:
            result = {}
            for dict_arg in self.dict_key_list:
                result[dict_arg.name] = dict_arg.check(value, self)
            value = result
        return value


class ChoiceParam(BaseParam):
    def __init__(self, choice_list: List, ignore_case=True, *args, **kwargs):
        """
        :param choice_list: 可选元素列表
        """
        super().__init__(*args, **kwargs)
        if self.must_has_value is False:
            choice_list.append(None)
        self.choice_list = choice_list
        self.ignore_case = ignore_case

    def extra_check_value(self, value, parent_field=None):
        if value:
            if self.ignore_case and isinstance(value, str):
                normalized_value = value.lower()
                normalized_choices = [choice.lower() if isinstance(choice, str) else choice for choice in
                                      self.choice_list]
            else:
                normalized_value = value
                normalized_choices = self.choice_list

            if normalized_value not in normalized_choices:
                raise ParamRangeError(self.get_desc(parent_field))

        return value


class BoolParam(ChoiceParam):
    type_list = [bool, int, str]

    def __init__(self, *args, **kwargs):
        choice_list = [True, False, 1, 0, "true", "false"]
        super().__init__(choice_list=choice_list, *args, **kwargs)

    def extra_check_value(self, value, parent_field=None):
        if isinstance(value, str):
            value = value.lower()  # 将字符串转为小写，以便处理像"True"或"False"这样的情况
            if value == "true":
                return True
            elif value == "false":
                return False
        return super().extra_check_value(value, parent_field)


class DateTimeParam(StrParam):
    type_list = [str, ]

    def __init__(self, datetime_format=DateTimeFormatEnum.day_time, *args, **kwargs):
        """
        :param datetime_format: 时间格式
        """
        super().__init__(*args, **kwargs)
        self.datetime_format = datetime_format

    def extra_check_value(self, value, parent_field=None):
        if value:
            try:
                value = datetime.datetime.strptime(value, self.datetime_format.value)
            except ValueError:
                raise ParamFormatError(self.get_desc(parent_field))
        return value


class FileParam(BaseParam):
    type_list = [UploadedFile]

    def __init__(self, allowed_extensions=None, max_size=None, *args, **kwargs):
        """
        :param allowed_extensions: 允许的文件扩展名列表
        :param max_size: 允许的最大文件大小（以M为单位）
        """
        super().__init__(*args, **kwargs)
        self.allowed_extensions = allowed_extensions
        self.max_size = max_size

    def extra_check_value(self, value: UploadedFile, parent_field=None):
        if not value:
            return value

        # 检查文件扩展名
        if self.allowed_extensions:
            ext = value.name.split('.')[-1]  # 获取文件扩展名
            if ext.lower() not in self.allowed_extensions:
                raise ValueError(f"{self.get_desc(parent_field)}: 文件类型不允许")

        # 检查文件大小
        if self.max_size and value.size > self.max_size * 1024 * 1024:
            raise ValueError(f"{self.get_desc(parent_field)}: 文件大小超过限制")

        return value
