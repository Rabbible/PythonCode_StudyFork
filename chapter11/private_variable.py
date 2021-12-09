# coding=utf-8
# 代码文件：chapter11/private_variable.py


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.__weight = weight  # 定义体重实例变量

    def eat(self):
        self.__weight += 0.05
        print('eat...')

    def run(self):
        self.__weight -= 0.01
        print('run...')


a1 = Animal(2, 0, 10.0)

# print('a1体重：{0:0.2f}'.format(a1.weight))
# print('a1体重：{0:0.2f}'.format(a1.__weight))
# 试试改成__weight行不行
# 结果还是不行hhhh
# 因为weight变量前加了__所以已经是私有变量了，__weight在类内部访问没有问题，但是如果在外部访问就会报错
a1.eat()
a1.run()
print('a1体重：{0:0.2f}'.format(a1._Animal__weight))
# 将a1.weight改成a1._Animal__weight不符合规范，会破坏封装，虽然这样也可以访问
