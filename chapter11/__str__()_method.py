# coding=utf-8
# 代码文件：chapter11/__str__()_method.py


# python根类————object
class Person:
    def __init__(self, name, age):
        self.name = name  # 名字
        self.age = age  # 年龄

    def __str__(self):
        # 重写__str__()
        # 如果不重写，那么默认返回对象类名，以及内存地址等信息，类似于type()
        # __str__()为对象描述自己的信息
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        # s = 'Person [name={0}, age={1}]'.format(self.name, self.age)
        return s


person = Person('Tony', 18)
print(person)
