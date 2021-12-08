# coding=utf-8
# code file: chapter4/com/pkg1/hello.py


# import sys
# import os
#
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(os.path.split(rootPath)[0])

import chapter4.com.pkg2.hello as module1
from chapter4.com.pkg2.hello import z

y = 20

print(y)  # Access the current module variable y
print(module1.y)  # Access module variable y for module1
print(z)  # Access module variable z for module1
