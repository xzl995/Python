"""
【问题描述】
编写一个程序实现两个一元多项式相乘。
【输入形式】
首先输入第一个多项式中系数不为0的项的系数和指数，以一个空格分隔。且该多项式中各项的系数均为0或正整数，系数和最高幂次不会超过int类型的表示范围。对于多项式 anxn +a n-1 x n-1 + ...+ a1x1 + a0x0 的输入方法如下：
an  n  a n-1  n-1 ...  a1  1  a0  0 
即相邻两个整数分别表示表达式中一项的系数和指数。在输入中只出现系数不为0的项。最后一项的指数后没有空格，只有一个回车换行符。
按照上述方式再输入第二个多项式。
【输出形式】
将运算结果输出到屏幕。将系数不为0的项按指数从高到低的顺序输出，每次输出其系数和指数，均以一个空格分隔，最后一项的指数后也可以有一个空格。
【样例输入】
10 80000 2 6000 7 300 5 10 18 0
3 6000 5 20 8 10 6 0
【样例输出】
30 86000 50 80020 80 80010 60 80000 6 12000 21 6300 10 6020 31 6010 66 6000 35 320 56 310 42 300 25 30 130 20 174 10 108 0
【样例说明】
输入的两行分别代表如下表达式：
10x80000 + 2x6000 + 7x300 + 5x10 + 18
3x6000 + 5x20 + 8x10 + 6
相乘结果为：
30x86000 + 50x80020 + 80x80010 + 60x80000 + 6x12000 + 21x6300 + 10x6020 + 31x6010 + 66x6000 + 35x320 + 56x310 + 42x300 + 25x30 + 130x20 + 174x10 + 108
"""
num1 = input().split()
num2 = input().split()
temp = []
temp_dict = {}
for i in range(0, len(num1), 2):
    for j in range(len(num2)):
        if j % 2 == 0:
            temp.append(int(num1[i]) * int(num2[j]))
        else:
            temp.append(int(num1[i + 1]) + int(num2[j]))

for i in range(1, len(temp), 2):
    if temp[i] not in temp_dict:
        temp_dict[temp[i]] = int(temp[i - 1])
    else:
        temp_dict[temp[i]] += int(temp[i - 1])


result = sorted(temp_dict.items(), key = lambda x:x[0], reverse = True)

for i in range(len(result)):
    print(result[i][1], result[i][0], end = " ")




