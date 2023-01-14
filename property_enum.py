#!/usr/bin/env python

from enum import Enum


class PropertyGroupId(Enum):
    NONE = -1
    BROWN = 0  # 2 properties in group
    LIGHT_BLUE = 1
    PINK = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5
    GREEN = 6
    DARK_BLUE = 7

    RAILROAD = 8  # 4 properties in group
    UTILITY = 9  # 2 properties in group
