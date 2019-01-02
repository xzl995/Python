"""
【问题描述】编写一个程序，将某个位数不确定的正整数进行三位分节后输出。
【输入形式】用户在第一行输入一个正整数。
【输出形式】程序将这个正整数三位分节输出，每隔三位加一个逗号（英文逗号）分割。
【样例输入】123456
【样例输出】1,234,567
【样例说明】用户输入正整数1234567，程序从个位开始每隔三位加一个逗号（英文逗号）分割，所以输出为1,234,567
"""
num = input()
if len(num) <= 3:
    print(num)
else:
    result = ""
    num = num[::-1]
    for i in range(len(num)):
        if (i + 1) % 3 == 0 and (i + 1) != len(num):
            result += num[i]
            result += ","
        else:
            result += num[i]
    result = result[::-1]
    print(result)


