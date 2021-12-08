# coding=utf-8
# code file: chapter9/dictionary.py

student_dict = {102: 'A', 105: 'B', 109: 'C'}

print('---key---')
for student_id in student_dict.keys():
    print('Id：' + str(student_id))

print('---value---')
for student_name in student_dict.values():
    print('student：' + student_name)

print('---key:value---')
for student_id, student_name in student_dict.items():
    print('Id：{0} - student：{1}'.format(student_id, student_name))
