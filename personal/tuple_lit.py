# coding = utf-8

a = ('Hello', 'World', 1, 2, 3)
# str1, str2, n1, n2, n3 = a


for s in a:
    print(s)
# print(str1)
# print(str2)
# print(n1)
# print(n2)
# print(n3)
print(a)   # tuple is iterable
print('----------*----------')

b = ['Hello', 'World', 1, 2, 3]
i = 0


if i < 3:
    for item in b:
        b.pop()
        # pop() has the returned value it deleted
        # remove() doesn't have, and it can just remove the first one it finds
print(b)
print('-----------**----------')


c = ['Hello', 'World', 1, 2, 3]


print(c)
c.remove(1)
print(c)
print('----------***-----------')


d = ['Hello', 'World', 1, 2, 3]
# e = []
print(d)

i = 0
# if i < 3:
#     for item_1 in d:
#         print('Q')
#         e.append(d.pop())
#         # append() add element into list
#         print(d)
# print(d)
# print(e)
print([d.pop() for item_1 in d if i < 3])
# e = [d.pop() for item_1 in d if i < 3]
# print(e)
print(d)
print("-----------****------------")
f = ['Hello', 'World', 'Hello', "hello", 1, 1, 2, 3]
print(f)
g = set(f)
# Change the list to a collection
# frozenset() is set an immutable collection
h = tuple(f)
# Change the list to a tuple
print(g)
print(h)
print("-----------------*****------------------")

asd = ('Hello', 'World', 'Hello', "hello", 1, 1, 2, 3)
asd_1 = list(asd)
# Change a tuple to a list
asd_2 = set(asd)
print(asd_1)
print(asd_2)
# Tuples and lists are sequences that can be iterated, ordered, and repeated.
# Collection: iterable, unordered, and non-repeatable
print("---------------------******---------------------")


dd = dict(s102='A', s105='B', s109='C')
# make a dictionary, main: a key and values
# dd = dict('102'='A', '105'='B', '109'='C')
# dd = dict(102='A', 105='B', 109='C')
# invalid
# There keys are strings of numbers, if you use dict() to create,
# you should do it like the first one
print(dd)

# https://blog.csdn.net/windy135/article/details/84576614
