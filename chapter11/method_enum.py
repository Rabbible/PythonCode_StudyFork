# coding=utf-8
# 代码文件：chapter11/method_enum.py

import enum


class WeekDays(enum.Enum):
    # 枚举常量列表
    # enum.Enum类
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 10
    # 5个常量成员，每一个都要初始化


day = WeekDays.FRIDAY
# 实例化枚举类WeekDays,该实例为FRIDAY

print(day)
print(day.value)
# 枚举实例value属性是返回枚举值
print(day.name)
# name属性返回枚举名
