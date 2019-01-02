"""
【问题描述】
平面上有两个矩形A和B，其位置是任意的。编程求出其相交部分（如图中阴影部分）的面积。
image.png
   【输入形式】
从标准输入读取两行以空格分隔的整数，格式如下：
Ax1 Ay1 Ax2 Ay2
Bx1 By1 Bx2 By2
其中（x1，y1）和（x2，y2）为矩形对角线上端点的坐标。各坐标值均为整数，取值在0至1000之间。
【输出形式】
向标准输出打印一个整数，是两矩形相交部分的面积（可能为0）。
【输入样例】
0 0 2 2
1 1 3 4

【输出样例】
1
【提示】
输入的两点可以是矩形任一对角线上的端点，求相交的面积可以先求矩形在X轴和Y轴上的交集。矩形在X轴上的交集可以按照如下算法进行求解：假设AX1和AX2中的较大值为MAX_AX，较小值为MIN_AX；BX1和BX2中的较大值为MAX_BX，较小值为MIN_BX。用MAX_AX和MAX_BX中的较小者减去MIN_AX和MIN_BX中的较大者，结果为正表示两矩形在X轴上的交集，若为负则表示不相交。
"""
# Ax1, Ay1, Ax2, Ay2, = input().split()
# Bx1, By1, Bx2, By2, = input().split()
# def MaxMin(x1, x2):
#     if x1 > x2:
#         Max = x1
#         Min = x2
#     else:
#         Max = x2
#         Min = x1
#     return Max, Min
#
# MAX_AX, MIN_AX = MaxMin(Ax1,Ax2)
# MAX_BX, MIN_BX = MaxMin(Bx1,Bx2)
# MAX_AY, MIN_AY = MaxMin(Ay1,Ay2)
# MAX_BY, MIN_BY = MaxMin(By1,By2)
# print(MAX_AX)


Ax1, Ay1, Ax2, Ay2, = input().split()
Bx1, By1, Bx2, By2, = input().split()
A = []
B = []
def find(x1, x2):
    if x1 > x2:
        MAX_AX, MIN_AX = x1, x2
    else:
        MAX_AX, MIN_AX = x2, x1
    return MAX_AX, MIN_AX
Ax = find(Ax1, Ax2)
Bx = find(Bx1, Bx2)
Ay = find(Ay1, Ay2)
By = find(By1, By2)

lessx = int(Ax[0]) if int(Bx[0]) > int(Ax[0]) else int(Bx[0])
morex = int(Bx[1]) if int(Bx[1]) > int(Ax[1]) else int(Ax[1])
lessy = int(Ay[0]) if int(By[0]) > int(Ay[0]) else int(By[0])
morey = int(By[1]) if int(By[1]) > int(Ay[1]) else int(Ay[1])
if lessx - morex >0 and lessy - morey >0:
    print((morex-lessx) * (morey-lessy))
else:
    print(0)
