# coding=utf-8
# code file: chapter10/Function_calls_with_keyword_arguments.py


def print_area(width, height):
    area = width * height
    print("{0} x {1} rectangle_area is :{2}".format(width, height, area))


print_area(320.0, 480.0)  # Function calls without keyword arguments
print_area(width=320.0, height=480.0)  # Function calls with keyword arguments
print_area(320.0, height=480.0)  # Function calls with keyword arguments
# print_area(width=320.0, height)  # error
print_area(height=480.0, width=320.0)  # Function calls with keyword arguments
