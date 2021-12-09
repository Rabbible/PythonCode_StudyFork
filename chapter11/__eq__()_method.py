# coding=utf-8
# 代码文件：chapter11/__eq__()_method.py


class Person:
    def __init__(self, name, age):
        self.name = name  # 名字
        self.age = age  # 年龄

    def __str__(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s

    # 重写__eq__()
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


p1 = Person('Tony', 18)
p2 = Person('Tony', 18)

print(p1 == p2)  # True
# 如果不重写__eq__()，那么则会得到False
