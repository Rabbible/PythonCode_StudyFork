# coding=utf-8
# code file: chapter9/collection.py

student_set = {'A', 'B', 'C'}

for item in student_set:
    print(item)

print('-----------')
for i, item in enumerate(student_set):
    print('{0} - {1}'.format(i, item))
