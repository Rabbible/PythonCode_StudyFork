# coding=utf-8
# 代码文件：chapter11/Multiple_inheritance.py


class ParentClass1:
    def run(self):
        print('ParentClass1 run...')


class ParentClass2:
    def run(self):
        print('ParentClass2 run...')


class SubClass1(ParentClass1, ParentClass2):
    pass
    # 对，就是你理解的pass，（无任何方法）,
    # 所以当子类实例调用一个方法时，先从子类中查找，如果没有找到则查找父类
    # 父类的查找顺序是按照子类声明的父类列表从左到右查找，如果没有找到再找父类的父类，依次找下去。


class SubClass2(ParentClass2, ParentClass1):
    pass


class SubClass3(ParentClass1, ParentClass2):
    def run(self):
        print('SubClass3 run...')


sub1 = SubClass1()
sub1.run()  # ParentClass1 run...

sub2 = SubClass2()
sub2.run()  # ParentClass2 run...

sub3 = SubClass3()
sub3.run()  # SubClass3 run...
