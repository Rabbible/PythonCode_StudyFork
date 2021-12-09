# coding=utf-8
# 代码文件：chapter10/lambda.py


def calculate_fun(opr):
    if opr == '+':
        return lambda a, b: (a + b)
        # 匿名函数lambda（是函数，有函数类型也可以创建函数对象）：
        # 格式：
        # lambda 参数列表 ：lambda 体
    else:
        return lambda a, b: (a - b)


f1 = calculate_fun('+')
f2 = calculate_fun('-')

print(type(f1))

print("10 + 5 = {0}".format(f1(10, 5)))
print("10 - 5 = {0}".format(f2(10, 5)))
