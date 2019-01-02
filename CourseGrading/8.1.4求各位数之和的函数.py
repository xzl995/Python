"""
【问题描述】
编写函数sofd，该函数计算一个整数n的各位数字之和并返回，如sofd(252)返回9。 
说明：sofd函数编写时只需考虑n大于等于0的情况，不用处理负整数的情况。
编写程序，输入一个整数n，调用函数sofd，输出它的各位数字之和。
【输入形式】 
一个数字，比如234
【输出形式】
数字各位和，比如 9
【样例输入】
234
【样例输出】
9
"""
def sofd(n):
    result = 0
    for i in n:
        result += int(i)
    return result

print(sofd(input()))
