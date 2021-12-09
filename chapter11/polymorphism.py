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

# 个人觉得多态性就是在父类的基础上重写了方法，形成的独具特色的方法
# 多态性的前提是继承性，然后就是重写
