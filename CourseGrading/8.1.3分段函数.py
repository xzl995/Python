"""
【问题描述】有一个定义在自然数上的函数 f(x) 定义如下：
                若 x <5 , 则 f(x) = x;
                若 5<=x<15, 则 f(x) = x+6;
                若 x>=15, 则 f(x) = x-6。
            试编写该函数，输入x值，返回相应的f(x)值。
【输入形式】输入的一行表示自然数x。
【输出形式】输出的一行表示计算结果f(x)，若输入的数据不合法（如：负整数），输出“illegal input”。
【样例输入】4
【样例输出】4
"""
def f(x):
    if x < 0:
        return "illegal input"
    elif x < 5:
        return x
    elif 5 <= x < 15:
        return x + 6
    else:
        return x - 6

x = int(input())
print(f(x))