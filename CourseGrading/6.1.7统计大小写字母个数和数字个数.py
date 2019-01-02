"""
【问题描述】统计一行字符的大写字母，小写字母和数字的个数。先输出大写字母个数，在输出小写字母个数，最后输出数字个数。
【输入形式】ljaij1A
【输出形式】1
                        5
                        1
【提示】用字符串的方法isupper, islower来判别大小写。isdigit来判断是否是数字。
"""
word = {"dx" : 0, "xx" : 0, "sz" : 0}
n = input()
for i in n :
    if i.isupper():
        word["dx"] += 1
    elif i.islower():
        word["xx"] += 1
    elif i.isdigit():
        word["sz"] += 1
for i in word.values():
    print(i)