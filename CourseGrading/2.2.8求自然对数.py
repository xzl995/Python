"""
【问题描述】
编写程序，输入实数x，通过调用库函数求x的绝对值的平方根的自然对数(log)
【输入形式】
输入一个实数。
【输出形式】
输出计算后的结果。保留5位小数。
【样例输入】
-9
【样例输出】
1.09861
"""
import math
r = float(input())
if r >= 0:
    r0 = math.sqrt(r)
else:
    r0 = math.sqrt(-r)
print('%.5f' % (math.log(r0)))