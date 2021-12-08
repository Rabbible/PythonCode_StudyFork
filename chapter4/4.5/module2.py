# coding=utf-8
# code file: chapter4/4.5/module2.py

import module1
# different module_names can import, if the module_names are same, you should use package.
from module1 import z

y = 20

print(y)  # Access the current module variable y
print(module1.y)  # Access module variable y for module1
print(z)  # Access module variable z for module1
