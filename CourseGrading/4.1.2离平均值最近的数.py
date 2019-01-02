"""
【问题描述】编程求一组数中离平均数最近的那个整数。计算位于前面的部分数的平均值，并返回离该平均值最近的那个数。
【输入形式】输入一行整数；最后一个是参与求平均的数的个数len。例如：1 2 3 4 5 6 7 10 12 13 8；意思是前面有10个数，最后的8是说前面8个数参与求平均，而不是10个数参与求平均。
【输出形式】离平均数最近的那个数。例如：5
【样例输入】1 2 3 4 5 6 7 10 12 13 8
【样例输出】5
"""
num = input().split()
list = []
for n in num:
    list.append(int(n))
len = list.pop()
sum = 0
for a in range(len):
    sum = sum + list[a]
avg = int(round((sum / len), 0))
list.append(avg)
list.sort()
index = list.index(avg)
if list[index - 1] == avg:
    print(list[index - 1])
elif list[index + 1] == avg:
    print(list[index + 1])
elif avg - list[index - 1] > list[index + 1] - avg:
    print(list[index - 1])
else:
    print(list[index + 1])

