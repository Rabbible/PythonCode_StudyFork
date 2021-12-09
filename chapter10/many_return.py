# coding=utf-8
# 代码文件：chapter9/many_return.py


def position(dt, speed):
    posx = speed[0] * dt
    posy = speed[1] * dt
    return (posx, posy)
    # 返回元组更安全，因为元组不可变


move = position(60.0, (10, -5))

print("物体位移：({0}, {1})".format(move[0], move[1]))
