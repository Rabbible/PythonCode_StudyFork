# coding=utf-8
# 代码文件：chapter10/filter_map_reduce.py

from functools import reduce

# 1.filter()
# 过滤操作,对可迭代对象的元素进行过滤
# filter(function, iterable)
users = ['Tony', 'Tom', 'Ben', 'Alex']

users_filter = filter(lambda u: u.startswith('T'), users)
print(list(users_filter))

number_list = range(1, 11)
number_filter = filter(lambda it: it % 2 == 0, number_list)
print(list(number_filter))

# 2.map()
# 映射操作，对可迭代对象的元素进行变换
# map(function, iterable)
users_map = map(lambda u: u.lower(), users)
print(list(users_map))

# users_map = map(lambda u: u.lower(), users_filter)
# python不支持链式API，数据无法从一个函数‘流入’另一个函数
# 想获取users列表中T开头的名字，再转化为小写字母，这样的需求需要使用filter()函数进行过滤，再用map()映射变换
users_map = map(lambda u: u.lower(), filter(lambda u: u.startswith('T'), users))

print(list(users_map))


# 3.reduce()
# 聚合操作, 会将多个数据聚合起来输出单个数据
# reduce(function, iterable[, initializer])
a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a)  # 10    acc为上次累计计算的结果
# a_reduce = reduce(lambda acc, i: acc + i, a, 2)  # 12
print(a_reduce)
