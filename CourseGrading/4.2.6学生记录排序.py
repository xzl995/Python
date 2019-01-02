"""
【问题描述】
从键盘中读入最多不超过50个学生的学生信息（包括空格隔开的姓名、学号、年龄信息，以学号从低到高排序）
【输入形式】
每次键盘读入最多不超过50个学生的学生信息：
第一行为学生人数；
后面每一行为空格隔开的学生学号、姓名、年龄，其中学号和年龄都是整数。
【输出形式】
分别以姓名顺序（从低到高）和年龄顺序（从低到高）将学生信息输出，每行输出一位学生的信息，其中学号占3位，姓名（英文）占6位，年龄占3位，均为右对齐。年龄相同时按姓名从低到高排序。两种顺序的输出结果用一行空行相隔。
【输入样例】
4
1 aaa 22
45 bbb 23
54 ddd 20
110 ccc 19
【输出样例】
     1    aaa     22       
  45     bbb     23     
110     ccc     19
  54     ddd     20                                      

110     ccc     19       
  54     ddd     20        
    1     aaa     22       
  45     bbb     23                           
【样例说明】
从键盘输入四个学生记录，分别按姓名和年龄排序并输出。
"""
from operator import itemgetter
n = int(input())
infors = []
compare = []
result = []
for i in range(n):
    infor = input().split()
    infors.append(infor)

name = sorted(infors, key = lambda s : s[1])
age = sorted(infors, key = itemgetter(2, 1))



for i in range(n):
    for j in range(3):
        if j == 0 or j == 2:
            print(name[i][j].rjust(3, " "), end = "")
        else:
            print(name[i][j].rjust(6, " "), end = "")
    print()
print()

for i in range(n):
    for j in range(3):
        if j == 0 or j == 2:
            print(age[i][j].rjust(3, " "), end = "")
        else:
            print(age[i][j].rjust(6, " "), end = "")
    print()

