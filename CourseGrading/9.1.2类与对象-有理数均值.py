"""
【问题描述】
计算N个有理数的平均值。要求定义有理数类，并定义计算有理数加法的方法。
【输入格式】
输入第一行给出正整数N（<100）；第二行中按照a1/b1 a2/b2 ...的格式给出N个分数形式的有理数，其中分子和分母全是整数；如果是负数，则负号一定出现在最前面。
【输出格式】
【样例输入】
4
1/2 1/6 3/6 -5/10
【样例输出】
1/6
"""
from fractions import Fraction
class Rational:
    def sum(self,num_list):
        num_sum = 0
        for i in num_list:
            i = Fraction(i)
            num_sum += i

        return num_sum

N = int(input())
num_list = input().split()
num_R = Rational()
print(Fraction(num_R.sum(num_list) / N))