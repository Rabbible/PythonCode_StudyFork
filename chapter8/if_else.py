# coding=utf-8
# code file: chapter8/if_else.py

import sys

score = int(sys.argv[1])  # Gets the arguments passed in from the command line

if score >= 60:
    print("pass")
    if score >= 90:
        print("excellent")
else:
    print("fail")
