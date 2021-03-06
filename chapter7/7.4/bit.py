# coding=utf-8
# code file: chapter7/7.4/bit.py

a = 0b10110010
b = 0b01011110

print("a | b = {0}".format(a | b))  # 0b11111110
# print("a | b = {0:s}".format(a | b))
print("a | b = {0:d}".format(a | b))  # decimal integer
print("a | b = {0:f}".format(a | b))  # decimal float
# print("a | b = {0:F}".format(a | b))
print("a | b = {0:g}".format(a | b))  # decimal integer or decimal float
# print("a | b = {0:G}".format(a | b))
print("a | b = {0:e}".format(a | b))  # Scientific notation represents floating point numbers
# print("a | b = {0:E}".format(a | b))
print("a | b = {0:o}".format(a | b))  # octonary integer
print("a | b = {0:x}".format(a | b))  # hexadecimal
# print("a | b = {0:X}".format(a | b))
print('------------------------------------------')

print("a & b = {0}".format(a & b))  # 0b00010010
print("a ^ b = {0}".format(a ^ b))  # 0b11101100
print("~a = {0}".format(~a))        # -179
print("a >> 2 = {0}".format(a >> 2))  # 0b00101100
print("a << 2 = {0}".format(a << 2))  # 0b11001000

c = -0b1100
print("c >> 2 = {0}".format(c >> 2))  # -0b00000011
print("c <<  2 = {0}".format(c << 2))  # -0b00110000
