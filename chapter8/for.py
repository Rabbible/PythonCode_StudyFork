# coding=utf-8
# code file: chapter8/for.py

print("----range-------")
for num in range(1, 10):  # usable range
    print("{0} x {0} = {1}".format(num, num * num))

print("----character string-------")
#  for
for item in 'Hello':
    print(item)

# Declaring integer lists
numbers = [43, 32, 53, 54, 75, 7, 10]

print("----integer lists-------")

#  for
for item in numbers:
    print("Count is : {0}".format(item))
