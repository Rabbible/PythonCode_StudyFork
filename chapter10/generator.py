# coding=utf-8
# 代码文件：chapter23/generator.py


# def square(num):
#     n_list = []
#
#     for i in range(1, num + 1):
#         n_list.append(i * i)
#
#     return n_list


def square(num):
    for i in range(1, num + 1):
        yield i * i
        # yield返回的是一个生成器，为可迭代对象,


for j in square(5):
    # 隐式调用生成器的__next__()方法获得元素
    print(j, end=' ')

# 显式调用生成器的__next__()方法获得元素
# 在shell中运行的示例为：
# def square(num):
#     for i in range(1, num + 1):
#         yield i * i
# n_seq= square(5) # enter
# n_seq.__next__() # enter
# ...
