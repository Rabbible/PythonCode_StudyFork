# coding=utf-8
# code file:chapter9/default.py


def make_coffee(name="卡布奇诺"):
    # Parameter Default Value
    return "制作一杯{0}咖啡。".format(name)


coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()
# if no, then default

print(coffee1)  # 制作一杯拿铁咖啡。
print(coffee2)  # 制作一杯卡布奇诺咖啡。
