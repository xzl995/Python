"""
【问题描述】
输入一组整数。删除其中第3个整数，然后输出删除后的整数数组。
【输入形式】
一行。用空格隔开的一组整数。
【输出形式】
一行。用一个空格隔开的一组整数。
【样例输入】
1 3 4 5 6
【样例输出】
1 3 5 6
"""
n0 = input().split()
n_list = []
for n in n0:
    n_list.append(n)
del(n_list[2])
print(" ".join(str(i) for i in n_list))
