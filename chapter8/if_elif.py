# coding=utf-8
# code file: chapter8/if_elif.py

import sys

score = int(sys.argv[1])  # Gets the arguments passed in from the command line

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade = " + grade)
