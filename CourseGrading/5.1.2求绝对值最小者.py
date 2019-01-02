"""
【问题描述】编写程序实现：计算并输出标准输入的三个数中绝对值最小的数。
【输入形式】标准输入的每一行表示参与计算的一个数。
【输出形式】标准输出的一行表示输入的三个数中绝对值最小的数,如果有多个,以一个空格作为间隔.
【样例输入】
－1
3
1
【样例输出】
-1.0 1.0
"""
temp = []
temp1 = []
for i in range(3):
    n = input()
    temp1.append(float(n))
for n in range(len(temp1)):
    temp.append(abs(temp1[n]))
minTemp = min(temp)
for j in range(len(temp1)):
    if temp1[j] == minTemp or temp1[j] == -minTemp:
        print(temp1[j], end = " ")



