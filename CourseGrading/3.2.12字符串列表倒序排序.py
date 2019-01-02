"""
【问题描述】
输入一组字符串，要求按字典序从大到小排序，输出排序后的结果。
【输入形式】
一行。一组用空格隔开的字符串。
【输出形式】
一行。一组用空格隔开的字符串，按字典序从大到小排序。
【样例输入】
Name hello zen yes
【样例输出】
zen yes hello Name
【样例说明】
按字典序而言，N排在h之前，也就是N小于h。所有大写字母都小于小写字母。
"""
str0 = input().split()
str_list = []
for n in str0:
    str_list.append(n)
str_list.sort(reverse = True)
print(" ".join(str(i) for i in str_list))