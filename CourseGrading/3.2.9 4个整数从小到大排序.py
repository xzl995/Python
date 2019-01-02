"""
【问题描述】
输入4个整数，从小到大排序后输出
【输入形式】
输入一行，内容是用空格隔开的4个整数。
【输出形式】
输出一行，内容是排序后的4个整数，整数之间用一个空格隔开。
【样例输入】
5 8 10 2
【样例输出】
2 5 8 10
"""
num = input().split()
list = []
for n in num:
    list.append(int(n))
list.sort()
print(" ".join(str(i) for i in list))