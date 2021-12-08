# coding=utf-8
# code file: chapter9/List_derivation.py

n_list = []
# new an empty list
for x in range(10):
    if x % 2 == 0:
        # even
        n_list.append(x ** 2)
        # append() can only add one into the list
print(n_list)

n_list = [x ** 2 for x in range(10) if x % 2 == 0]
# List derivation
# x ** 2 : Output expression   x : element variable  range(10) : input sequence
# if x % 2 == 0 : condition statement
print(n_list)

n_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
# if And if
print(n_list)
