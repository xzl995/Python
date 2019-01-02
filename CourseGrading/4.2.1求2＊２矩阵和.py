"""
【问题描述】输入A，B两个矩阵，规模为2*2，求出这两个整数矩阵相加的和
【输入形式】 一共4行。前两行是矩阵A的元素，后两行是矩阵B的元素。
【输出形式】输出相加得到的结果矩阵。 同一行元素之间隔开一个空格。
【样例输入】
 1 1
 5 5
 7 7
 3 3
【样例输出】
 8 8
 8 8
"""
temp1 = []
temp2 = []
i = 1
while i <= 4:
    n = input().split()
    if i <= 2:
        temp1.append(n)
    else:
        temp2.append(n)
    i += 1

result = [[0, 0],
          [0, 0]]
for i in range(2):
    for j in range(2):
        result[i][j] = int(temp1[i][j]) + int(temp2[i][j])
        print(result[i][j], end = " ")
    print(" ")



