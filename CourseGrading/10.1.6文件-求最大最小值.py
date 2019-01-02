"""
【问题描述】
从in.txt文件读数据，对于该文件每一行：
    求该行中各个数（可能是整数，也可能是浮点数）的最大、最小值，
    把最大值和最小值写入文件out.txt，写成一行，最大值在前，两个数之间隔两个空格。
30 300 30 201 0 395 92 
353 50  50  202  0 430 100 
35 35  0  50 20  20 430 100 
35 35 1.2 50  20 20 365 85 
32.5   32.5  0 47.5  200  381.33333 89 
【样例输出】
395  0
430  0
430  0
365  1.2
381.33333  0
【样例说明】
值输出的内容要与该值输入时的内容完全一致。例如，输入内容是381.33333，输出内容也要是381.33333，不能输出为381.33.
"""
with open("in.txt") as data:
    datas = data.readlines()

temp = []
for data in datas:
    flag = []
    for i in data:
        # if i != 0 and float(i) % int(i) == 0:
        #     flag.append(int(i))
        # elif i == 0:
        #     flag.append(0)
        # else:
        #     flag.append(float(i))
        flag.append(i)
    flag.sort(reverse = True)
    temp.append(flag)
print(temp)
with open("out.txt", "w") as out_data:
    for i in temp:
       out_data.write(i[0],i[-1])

