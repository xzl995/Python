"""
【问题描述】从若干学生成绩中统计高于(严格的大于)平均分的人数，用-1做为学生成绩数据的结束标志
【输入形式】一组学生的成绩
【输出形式】高于平均分的学生人数
【样例输入】70 50 80 -1
【样例输出】2
"""
count = 0
sum = 0
score = input().split()
list = []
for n in score:
    list.append(int(n))
list.remove(-1)
for i in range(0, len(list)):
    sum += list[i]
if len(list) == 0:
    count = 0
    print(count)
else:
    avg = sum / (len(list))
    for i in range(0, len(list)):
        if list[i] > avg:
            count += 1
    print(count)




