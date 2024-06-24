from enum import Enum
from typing import Type


class BaseEnum(Enum):
    def __new__(cls, desc):
        obj = object.__new__(cls)
        obj._desc = desc
        return obj

    @property
    def description(self):
        return self._desc

    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.name == value:
                return member
        raise ValueError(f"{value} is not a valid {cls.__name__}")

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


def roast_type_enum_choices(enum_class):
    # 定义一个函数来获取所有的枚举值
    return [(member.value, member.value) for member in enum_class]


def enum_choices(enum_class):
    # 定义一个函数来获取所有的枚举值
    return [(member.name, member.value) for member in enum_class]


def many_enum_choices(enum_class_list):
    # 定义一个函数来获取所有的枚举值
    return [(member.name, member.value) for enum_class in enum_class_list for member in enum_class]


def enum_choices_dict(enum_class):
    return [{"value": i[0], "label": i[1]} for i in enum_choices(enum_class)]


def get_enum_or_param_error(enum_class: Type[BaseEnum], name: str):
    value = getattr(enum_class, name, None)
    if value is None:
        raise ValueError(f"'{name}' is not a valid member of {enum_class.__name__}")
    return value


class TwoValueEnum(BaseEnum):
    def __new__(cls, value, desc):
        obj = object.__new__(cls)
        obj._value = value
        obj._desc = desc
        return obj

    @property
    def value(self):
        return self._value

    @property
    def whole_value(self):
        return self._value, self._desc

    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"{value} is not a valid {cls.__name__}")


def two_value_enum_choices(enum_class):
    # 定义一个函数来获取所有的枚举值
    return [(member.value, member.description) for member in enum_class]
