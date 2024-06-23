# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class OrderConditionEnum(Enum):
    """
    排序条件枚举
    """

    ASC = "asc"
    DESC = "desc"
    RAND = "rand"
