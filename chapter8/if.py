# coding=utf-8
# code file: chapter8/if.py

import sys

# print(sys.argv[:])

score = int(sys.argv[1])  # Gets the arguments passed in from the command line

if score >= 85:
    print("excellent！")

if score < 60:
    print("keep on！")

if (score >= 60) and (score < 85):
    print("it is Ok, but not the best！")
