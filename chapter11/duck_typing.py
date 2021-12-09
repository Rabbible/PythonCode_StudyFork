# coding=utf-8
# 代码文件：chapter11/duck_typing.py

class Animal(object):
    def run(self):
        print('动物跑...')


class Dog(Animal):
    def run(self):
        print('狗狗跑...')


class Car:
    def run(self):
        # 由于python不做类型检查，所以emmmmmm虽然car不属于animal，但是他依旧可以用.run()，这就是鸭子类型
        print('汽车跑...')


def go(animal):  # 接收参数是Animal
    animal.run()


go(Animal())
go(Dog())
go(Car())
