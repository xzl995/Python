"""
字符串中字母大小写互换
【问题描述】编写程序，功能是把输入的字符串的大写字母变成小写字母，小写字母变成大写字母，非字母的字符不作变换。输出变换后的结果。
【输入形式】字符串，包含字母和非字母字符。
【输出形式】字符串，字母的大小写已经发生变换。
【样例输入】abcABC
【样例输出】ABCabc
"""
n = input()
m = ""
for i in n :
    if i.isupper():
        i = i.lower()
        m = m + i
    elif i.lower():
        i = i.upper()
        m = m + i
print(m)