"""
【问题描述】从键盘输入非0整数，以输入0为输入结束标志，求平均值，统计正数负数个数
【输入形式】
      每个整数一行。最后一行是0，表示输入结束。
【输出形式】
     输出三行。
     第一行是平均值。第二行是正数个数。第三行是负数个数。
【样例输入】
                        1
                        1
                        1
                        0
【样例输出】
                        1
                        3
                        0
"""
n = int(input())
nList = []
zs = 0
fs = 0
while n != 0:
    nList.append(n)
    n = int(input())
avg = sum(nList) / len(nList)
for i in nList:
    if i > 0:
        zs += 1
    else:
        fs += 1

print(avg)
print(zs)
print(fs)