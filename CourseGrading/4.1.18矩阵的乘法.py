"""
【问题描述】
编写程序，完成3*４矩阵和4*３整数矩阵的乘法，输出结果矩阵。
【输入形式】
以先行后列顺序输入第一个矩阵，而后输入第二个矩阵。
【输出形式】
先行后列顺序输出结果矩阵，每个元素的显示宽度为8格，屏幕一行只显示矩阵的一行。
例如要计算如下两个矩阵
第一个矩阵    1 2 3 4
                     5 6 7 8
                     9 1 2 3
第二个矩阵    9 8 7
                     6 5 4
                     3 2 1
                     1 2 3
输入与输出格式如下
【样例输入】
1 2 3 4 5 6 7 8 9 1 2 3 9 8 7 6 5 4 3 2 1 1 2 3
【样例输出】
      34      32      30
     110     100     90
      96       87      78
"""
temp1 = []
temp2 = []
result = []
num = input().split()
i = 0
j = 4
while j<= 13:
    temp1.append(num[i:j])
    i = j
    j += 4
x = 12
y = 15
while y <= len(num):
    temp2.append(num[x:y])
    x = y
    y += 3

for temp1_h in range(3):
    temp1_1 = temp1[temp1_h][0]
    temp1_2 = temp1[temp1_h][1]
    temp1_3 = temp1[temp1_h][2]
    temp1_4 = temp1[temp1_h][3]
    for temp2_l in range(3):
        temp2_1 = temp2[0][temp2_l]
        temp2_2 = temp2[1][temp2_l]
        temp2_3 = temp2[2][temp2_l]
        temp2_4 = temp2[3][temp2_l]
        sum = 0
        sum += int(temp1_1) * int(temp2_1) + int(temp1_2) * int(temp2_2) + int(temp1_3) * int(temp2_3) + int(temp1_4) * int(temp2_4)
        result.append(sum)

result1 = []
i = 0
j = 3
while j < 12:
    result0 = result[i:j]
    i = j
    j += 3
    result1.append(result0)

for i in range(3):
    print(str(result1[i][0]).rjust(8) + str(result1[i][1]).rjust(8) + str(result1[i][2]).rjust(8))


