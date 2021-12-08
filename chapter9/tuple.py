# coding=utf-8
# code file: chapter9/tuple.py


a = (21, 32, 43, 45)

for item in a:
    print(item)

print('-----------')
for i, item in enumerate(a):
    # enumerate() can capture a tuple object
    print('{0} - {1}'.format(i, item))
