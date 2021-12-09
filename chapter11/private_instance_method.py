# coding=utf-8
# 代码文件：chapter11/private_instance_method.py


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.__weight = weight  # 定义体重实例变量

# 定义实例方法：

    def eat(self):
        self.__weight += 0.05
        self.__run()
        print('eat...')

    # 定义私有实例方法：

    def __run(self):
        self.__weight -= 0.01
        print('run...')


a1 = Animal(2, 0, 10.0)

a1.eat()
# 输出结果是run...和eat...因为eat()方法中调用了__run()，属于内部调用，所以会运行一次私有方法输出run...
# 但是如果直接从外部调用私有方法，那必然是报错的
# a1.run()
