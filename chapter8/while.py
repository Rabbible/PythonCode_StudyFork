# coding=utf-8
# code file: chapter8/while.py

i = 0

while i * i < 100_000:
    # to have clear view, 100000 is Ok,too
    i += 1

print("i = {0}".format(i))
print("i * i = {0}".format(i * i))