# coding=utf-8
# 代码文件：chapter11/limit_enum.py

import enum


@enum.unique  # 防止常量成员值重复
class WeekDays(enum.IntEnum):
    # 枚举常量列表
    # enum.IntEnum类
    # 限制为整数类型
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3  # 'Wed.'
    THURSDAY = 4
    FRIDAY = 5  # 1


day = WeekDays.FRIDAY

print(day)
print(day.value)
print(day.name)
