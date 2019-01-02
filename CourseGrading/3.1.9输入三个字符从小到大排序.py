"""
【问题描述】
 从键盘输入三个字符，按ASCII码值从小到大排序输出，字符之间间隔一个空格。
【输入形式】
输入三个字符，每个字符用空格隔开。
【输出形式】
相对应的输出按照ASCII码值从小到大排列的三个字符，每个字符间用空格隔开。
【样例输入】
a c b
【样例输出】
a b c
"""
str1 ,str2, str3 = input().split()
str = []
str.append(str1)
str.append(str2)
str.append(str3)
str.sort()
print(str[0] , str[1] , str[2])

