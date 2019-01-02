"""
【问题描述】
输入一组整数a，而后输入一个整数k，把k加入到数组a的尾部，然后输出整数数组。
【输入形式】
第一行。是一组整数a。用空格隔开。
第二行。是一个整数k。
【输出形式】
输出一行，即整数数组a。用1个空格隔开。
【样例输入】
1 2 3 4
5
【样例输出】
1 2 3 4 5
"""
a0 = input().split()
k = input()
a = []
for n in a0:
    a.append(n)
a.append(k)
print(" ".join(str(i) for i in a))