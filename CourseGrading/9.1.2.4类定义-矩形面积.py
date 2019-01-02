"""
【问题描述】
补充矩形类Rect的定义。它有长度和宽度，area方法的作用是求矩形的面积。
"""
class Rect:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

x = float(input())
y = float(input())
r1 = Rect(x, y)
print(r1.area())