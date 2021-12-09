# coding=utf-8

# 几何图形
class Figure:
    def draw(self):
        print('绘制Figure...')


# 椭圆形
class Ellipse(Figure):
    def draw(self):
        print('绘制Ellipse...')


# 三角形
class Triangle(Figure):
    def draw(self):
        print('绘制Triangle...')


f1 = Figure()  # 没有发生多态
f1.draw()

f2 = Ellipse()  # 发生多态
f2.draw()

f3 = Triangle()  # 发生多态
f3.draw()

# 类型检查
# isinstance(object, classinfo)
# 可以检查object实例是否由classinfo类或classinfo子类所创建的实例
print(isinstance(f1, Triangle))  # False
print(isinstance(f2, Triangle))  # False
print(isinstance(f3, Triangle))  # True
print(isinstance(f2, Figure))  # True
print(isinstance(f1, Figure))  # True
print('---------------------------------------------')

# issubclass(class, classinfo)
# 用来检查class是否是classinfo的子类
print(issubclass(Ellipse, Triangle))  # False
print(issubclass(Ellipse, Figure))  # True
print(issubclass(Triangle, Ellipse))  # False
