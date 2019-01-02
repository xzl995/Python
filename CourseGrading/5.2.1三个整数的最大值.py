"""
【题目描述】输入三个整数，输出最大的一个整数。
【输入形式】从键盘输入三个整数，以空格间隔
【输出形式】输出最大的一个整数
【样例输入】1 2 3
【样例输出】3
"""
n = input().split()
temp = []
for i in n:
    temp.append(int(i))
print(max(temp))