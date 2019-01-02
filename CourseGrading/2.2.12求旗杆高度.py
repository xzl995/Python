"""
【问题描述】某战士根据太阳光的仰角和影子长度，利用数学函数来求解旗杆的高度。（圆周率取值为3.1415926）。请你编程实现计算过程。
【输入形式】采用浮点形式输入的角度值和影子长度值
【输出形式】一个浮点数，代表旗杆高度值。保留两位小数。
【样例输入】45  100
【样例输出】100.00
【提示】
程序要用到math模块的tan()函数。假设角度是d，那么下面的代码将计算得到正切函数值，存入tan_value变量。
import math
tan_value = math.tan(d)
"""
import math
angle , shawdow = input().split()
angle = float(angle)
angle = math.radians(angle)
shawdow = float(shawdow)
h = shawdow * math.tan(angle)
print('%.2f' % h)
