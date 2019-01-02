"""
【问题描述】统计一行字符的大写字母，小写字母和数字的个数。先输出大写字母个数，在输出小写字母个数，最后输出数字个数。
【输入形式】ljaij1A
【输出形式】1
           5
           1
【提示】用字符串的方法isupper, islower来判别大小写。isdigit来判断是否是数字。
"""
n = input()
n0 = n.split()
n_isupper = 0
n_islower = 0
n_isdigit = 0
for m in n:
   if m.isupper():
       n_isupper = n_isupper+1
   elif m.islower():
       n_islower = n_islower+1
   elif m.isdigit():
       n_isdigit = n_isdigit+1
print(n_isupper)
print(n_islower)
print(n_isdigit)




