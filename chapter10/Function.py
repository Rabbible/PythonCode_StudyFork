# coding=utf-8
# code file: chapter10/Function.py


def rectangle_area(width, height):
    # defined function
    area = width * height
    return area


r_area = rectangle_area(320.0, 480.0)

print("320x480 rectangle_area is :{0:.2f}".format(r_area))
