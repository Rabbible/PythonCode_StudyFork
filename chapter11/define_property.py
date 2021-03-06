# coding=utf-8
# 代码文件：chapter11/define_property.py

# class Animal(object):
#     """定义动物类"""
#
#     def __init__(self, age, sex=1, weight=0.0):
#         self.age = age  # 定义年龄实例成员变量
#         self.sex = sex  # 定义性别实例成员变量
#         self.__weight = weight  # 定义体重实例成员变量
#
#     def set_weight(self, weight):
#         self.__weight = weight
#
#     def get_weight(self):
#         return self.__weight
#
#
# a1 = Animal(2, 0, 10.0)
# print('a1体重：{0:0.2f}'.format(a1.get_weight()))
# a1.set_weight(123.45)
# print('a1体重：{0:0.2f}'.format(a1.get_weight()))

class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例成员变量
        self.sex = sex  # 定义性别实例成员变量
        self.__weight = weight  # 定义体重实例成员变量

    @property
    def weight(self):  # 替代get_weight(self):     定义属性getter访问器
        return self.__weight

    @weight.setter
    def weight(self, weight):  # 替代set_weight(self, weight):      定义属性setter访问器
        self.__weight = weight


a1 = Animal(2, 0, 10.0)
print('a1体重：{0:0.2f}'.format(a1.weight))  # 这样就可以通过属性来取值
a1.weight = 123.45  # a1.set_weight(123.45)
print('a1体重：{0:0.2f}'.format(a1.weight))
# 属性本质上就是两个方法，在方法前加上装饰器使得方法成为属性。
# 属性使用起来类似公有变量，可以在赋值符号“=”左边或者右边，左边是被赋值，右边是取值
# 定义属性时，应该先定义getter访问器，再定义setter访问器
# 因为@property修饰getter访问器时，定义了weight属性，这样在后面使用@weight.setter装饰器才是合法的
