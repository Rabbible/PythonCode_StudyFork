# coding=utf-8
# 代码文件：chapter11/construct_method.py


class Animal(object):
    """定义动物类"""
    # 构造方法
    def __init__(self, age, sex=1, weight=0.0):
        # 设置了默认值
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.weight = weight  # 定义体重实例变量


a1 = Animal(2, 0, 10.0)
a2 = Animal(3, weight=5.0)
a3 = Animal(1, sex=0)

print('a1年龄：{0}'.format(a1.age))

print('a2年龄：{0}'.format(a2.age))
print('a2性别：{0}'.format('雌性' if a2.sex == 0 else '雄性'))
print('a2体重：{0}'.format(a2.weight))

print('a3年龄：{0}'.format(a3.age))
print('a3性别：{0}'.format('雌性' if a3.sex == 0 else '雄性'))
print('a3体重：{0}'.format(a3.weight))

