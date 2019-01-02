"""
【问题描述】
定义Point类实现三维坐标点。定义dist_from方法实现两点之间距离的计算。
【输入形式】输入两行，第一行是第一个点的坐标值，第二行是第二个点的坐标值。坐标值x, y, z之间用空格隔开。
【输出形式】距离
【样例输入】
0 0 0
1 1 1
【样例输出】
1.73205
"""

import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dist_from(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        dz = self.z - p.z
        return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


x1, y1, z1 = input().split()
x1 = float(x1)
y1 = float(y1)
z1 = float(z1)
p1 = Point(x1, y1, z1)
x2, y2, z2 = input().split()
x2 = float(x2)
y2 = float(y2)
z2 = float(z2)
p2 = Point(x2, y2, z2)
print("%.2f" % p1.dist_from(p2))
