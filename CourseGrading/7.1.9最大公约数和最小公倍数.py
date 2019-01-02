"""
【问题描述】输入两个正整数a和b（0<a，b<1000000），求出其最大公约数和最小公倍数并输出。
【输入文件】从标准输入读取一行，是两个整数a和b，以空格分隔。
【输出文件】向标准输出打印以空格分隔的两个整数，分别是a、b的最大公约数和最小公倍数。
【输入样例】12 18
【输出样例】6 36
【样例说明】12和18的最大公约数是6，最小公倍数是36.
"""
a, b = input().split()
a = int(a)
b = int(b)
temp = []

for i in range(1, min(a, b)+ 1):
    if a % i == 0 and b % i == 0:
        temp.append(i)

for j in range(max(a, b), a * b + 1):
    if j % a == 0 and j % b == 0:
        temp.append(j)
        break

multiple = temp.pop(-1)

print(max(temp), multiple)


