# coding=utf-8
# code file: chapter7/7.3/Logical_Operator.py

i = 0
a = 10
b = 9

if a > b or i == 1:
    print("Or operation to true")
else:
    print("Or operation to false")

if a < b and i == 1:
    print("And operation to true")
else:
    print("And operation to false")


def f1():
    return a > b


def f2():
    print('--f2--')
    return a == b


print(f1() or f2())
