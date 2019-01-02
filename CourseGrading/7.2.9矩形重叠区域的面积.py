"""
【问题描述】平面上有两个矩形A和B，其位置是任意的。编程求出其相交部分（即重叠部分）的面积。（0<a，b<1000）
【输入文件】从标准输入读取两行以空格分隔的整数，格式如下：
Ax1 Ay1 Ax2 Ay2
Bx1 By1 Bx2 By2
其中（x1，y1）为矩形一个顶点座标，（x2，y2）为前一顶点的对角顶点座标。各座标值均为整数，取值在0至1000之间。
【输出文件】向标准输出打印一个整数，是两矩形相交部分的面积（可能为0）。在输出末尾要有一个回车符。
【输入样例】
0 0 2 2
1 1 3 4
【输出样例】
1
【样例说明】输入的两个矩阵的相交面积为1
"""
Ax1, Ay1, Ax2, Ay2 =(int(i) for i in input().split())
Bx1, By1, Bx2, By2 =(int(i) for i in input().split())

max_Ay = max(Ay1, Ay2)
max_By = max(By1, By2)
min_Ay = min(Ay1, Ay2)
min_By = min(By1, By2)

max_Ax = max(Ax1, Ax2)
max_Bx = max(Bx1, Bx2)
min_Ax = min(Ax1, Ax2)
min_Bx = min(Bx1, Bx2)

if max_Ay > max_By:
    max_y = max_By
    min_y = min_Ay
elif max_Ay < max_By:
    max_y = max_Ay
    min_y = min_By

if max_Ax > max_Bx:
    max_x = max_Bx
    min_x = min_Ax
elif max_Ax < max_Bx:
    max_x = max_Ax
    min_x = min_Bx

area = (max_y - min_y) * (max_x - min_x)
print(area)