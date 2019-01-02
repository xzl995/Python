"""
【问题描述】
输入n的值和n个数，进行排序并输出。
【输入形式】
首先输入整数个数n；
接着输入n个整数
【输出形式】
从小到大地输出n个整数
 【输入示例】
3
1  5 -10
【输出示例】
-10 1 5
"""
n = 0
n_list = []
n_len = int(input())
while n < n_len:
    for i in input().split():
        n_list.append(int(i))
        n += 1
n_list.sort()
print(" ".join(str(a) for a in n_list))
