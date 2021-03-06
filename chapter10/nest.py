# coding=utf-8
# 代码文件：chapter10/nest.py


def calculate(n1, n2, opr):
    # opr 为操作符，如+，-，*，/
    multiple = 2

    # 定义相加函数
    def add(a, b):
        return (a + b) * multiple

    # 定义相减函数
    def sub(a, b):
        return (a - b) * multiple

    return add(n1, n2) if (opr == '+') else sub(n1, n2)


print(calculate(10, 5, '+'))  # 输出结果是30
# add(10, 5) 发生错误
# sub(10, 5)  发生错误
# 里层函数不能被直接调用
