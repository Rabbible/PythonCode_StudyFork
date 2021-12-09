# coding=utf-8
# 代码文件：chapter11/succession.py


class Person:

    def __init__(self, name, age):
        self.name = name  # 名字
        self.age = age  # 年龄

    def info(self):
        template = 'Person [name={0}, age={1}]'
        _s = template.format(self.name, self.age)
        return _s


p = Person('小赵', 18)
print(p.info())


# class Student:
#
#     def __init__(self, name, age, school):
#         self.name = name  # 名字
#         self.age = age  # 年龄
#         self.school = school  # 所在学校
#
#     def info(self):
#         template = 'Student [name={0}, age={1}, school={2}]'
#         _s = template.format(self.name, self.age, self.school)
#         return _s

class Student(Person):
    # 继承Person

    def __init__(self, name, age, school):
        super().__init__(name, age)
        # 调用父类的构造方法，初始化父类实例变量
        self.school = school  # 所在学校

    # def info(self):
    #     template = 'Student [name={0}, age={1}, school={2}]'
    #     _s = template.format(self.name, self.age, self.school)
    #     return _s


s = Student('Tom', 28, '清华大学')
print(s.info())
