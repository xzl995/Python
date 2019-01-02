"""
【问题描述】
输入n个学生的成绩，按总分从大到小输出。
【输入形式】
第一行输入学生人数n。
后续n行，每一行输入一个学生的学号, 姓名，语文成绩和数学成绩。各字段之间用空格隔开。
【输出形式】
输出n行。每一行给出学生学号，姓名，总分。按总分从大到小排序。若总分相同，则按学号从小到大排序。
【样例输入】
5
355 dj 60 70
665  kk 70 80
g33 He 55 95
l222 Li 60 80
n77 Liu 70 60
【样例输出】
665	kk	150
g33	He	150
l222	Li	140
355	dj	130
n77	Liu	130
"""

n = int(input())
temp = []
for i in range(n):
    infors = input().split()
    a = []
    for j in infors:
        a.append(j)
    sum = int(a[2]) + int(a[3])
    a.append(sum)
    temp.append(a)
result2 = sorted(temp, key = lambda x:x[0])
result = sorted(temp, key = lambda x:x[-1], reverse = True)

for i in range(n):
    del result[i][2]
    del result[i][2]

for i in range(n):
    for j in range(3):
        print(result[i][j], end = " ")
    print()

