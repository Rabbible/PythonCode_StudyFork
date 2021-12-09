# coding = utf-8

import personal.test.pkg1.test1 as module1
# it'll also import the test1's result into this module,
# for example, if i write 'print("Hello, world!")',
# in test2, i will get 'Hello world!' which will display on the screen

print(module1.x)
print(module1.z)

# print(module1.y)
# because of "if __name__ == '__main__'", y has no been attributed

print(module1.z)
