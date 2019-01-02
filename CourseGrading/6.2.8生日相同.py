"""
[【描述】
在一个有180人的大班级中，存在两个人生日相同的概率非常大，现给出每个学生的名字，出生月日。试找出所有生日相同的学生。
【输入】
第一行为整数n，表示有n个学生，n<=180。此后每行包含一个字符串和两个整数，分别表示学生的名字（名字第一个字母大写，其余小写，不含空格，且长度小于20）和出生月(1<=m<= 12)日(1 <=d<=31)。名字、月、日之间用一个空格分隔
【输出】
每组生日相同的学生，输出一行，其中前两个数字表示月和日，后面跟着所有在当天出生的学生的名字，数字、名字之间都用一个空格分隔。对所有的输出，要求按日期从前到后的顺序输出。 对生日相同的名字，按名字从短到长按序输出，长度相同的按字典序输出。如果没有任何生日相同的学生，输出：None  。
【样例输入】
6
Avril 3 2
Candy 4 5
Tim 3 2
Sufia 4 5
Lagrange 4 5
Bill 3 2
【样例输出】
3 2 Tim Bill Avril
4 5 Candy Sufia Lagrange
【样例说明】
样例输出中，3月2日有Tim, Bill, Avril三个人在当日出生。
"""
n = int(input())
infors_dict = {}
for i in range(n):
    infors = input().split()
    name = infors[0]
    birth = (infors[1], infors[2])
    if birth not in infors_dict:
        infors_dict[birth] = name
    else:
        infors_dict[birth] = infors_dict[birth] + " " + name

def lenName(name):
    return len(name)

for key, value in infors_dict.items():
    value = value.split()
    value = sorted(value, key = lenName)
    infors_dict[key] = value

infors_dict = sorted(infors_dict.items(), key = lambda x:x[0], reverse = True)
infors_dict = sorted(infors_dict, key = lambda x:x[1], reverse = True)

result = {}
for i in range(len(infors_dict)):
    result[infors_dict[i][0]] = infors_dict[i][1]

for key, value in result.items():
    print(" ".join(str(i) for i in key,), " ".join(str(j) for j in value))






