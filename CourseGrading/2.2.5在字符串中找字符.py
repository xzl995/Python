"""
【问题描述】编写程序判断输入的字符是否在字符串str中出现。
【输入形式】一行。首先是需查找的字符，接着是空格，再接着是字符串str。注意，字符串str中可能包含空格。
【输出形式】true或者false
【样例输入】m akdfomdkl
【样例输出】true
【样例说明】输出true或者false，不是1或者0
"""
n,str = input().split(" ")
if n in str:
    print('true')
else:
    print('false')