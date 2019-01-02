"""
【问题描述】已知10个四位数输出所有对称数及个数 n，例如1221、2332都是对称数
【输入形式】10个四位数，以空格分隔开
【输出形式】输入的四位数中的所有对称数，对称数个数
【样例输入】1221 2243 2332 1435 1236 5623 4321 4356 6754 3234
【样例输出】1221 2332 2
【样例说明】为测试程序健壮性，输入数中可能包括3位数、5位数等
【评分标准】
"""
num = input().split()
list = []
dc_list = []
for n in num:
    list.append(int(n))
sum = 0
for n in range(0, len(num)):
    for s in range(0, len(num[n])):
        if len(num[n]) % 2 != 0:
            break
        elif num[n][s] != num[n][len(num[n]) - s - 1] and  (len(num[n]) - s - 1) - s != 1:
            break
        elif num[n][s] == num[n][len(num[n]) - s - 1] and  (len(num[n]) - s - 1) - s == 1:
            sum = sum + 1
            dc_list.append(num[n])
print(" ".join(str(i) for i in dc_list), sum)