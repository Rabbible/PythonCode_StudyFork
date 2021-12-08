# coding=utf-8
# code file: chapter9/collection_derivation.py

n_set = {x for x in range(100) if x % 2 == 0 if x % 5 == 0}
# as same as list
print(n_set)

input_list = [2, 3, 2, 4, 5, 6, 6, 6]

n_list = [x ** 2 for x in input_list]
print(n_list)

n_set = {x ** 2 for x in input_list}
print(n_set)
