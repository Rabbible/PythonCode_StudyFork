# coding=utf-8
# code file: chapter8/condition_expression.py

import sys

score = int(sys.argv[1])  # Gets the arguments passed in from the command line

result = 'pass' if score >= 60 else 'fail'
print(result)
