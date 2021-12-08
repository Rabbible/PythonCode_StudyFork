# coding=utf-8
# code file: chapter8/range.py

for item in range(1, 10, 2):
    # 1 <= item < 10, step = 2
    print("Count is : {0}".format(item))

print('--------------')

for item in range(0, -10, -3):
    # -10 <= item < 0, step = -3
    print("Count is : {0}".format(item))
