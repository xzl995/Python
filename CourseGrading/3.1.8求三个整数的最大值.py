"""
【问题描述】输入3个整数，输出其中最大的一个 。
【样例输入】1 2 3
【样例输出】3
"""
a, b, c = input().split()
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)