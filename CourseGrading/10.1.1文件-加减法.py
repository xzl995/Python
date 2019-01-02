"""
【问题描述】
从文件jisuan.txt读入多行（行数不确定）。每一行写有一个两个操作数参加的加法运算式或减法运算式。程序分析每一行的运算式，完成运算，把运算结果写入jieguo.txt，一行一个结果。
【输入形式】
文件內的每一行 是一个两个操作数参加的加法运算式或减法运算式。算式中不含空格
【输出形式】
文件，一行一个结果。结果保留两位小数。
【样例输入】
输入文件内容：
1+2
5-2.3
6+0.8
【样例输出】
输出文件内容：
3.00
2.70
6.80
"""
with open("jisuan.txt") as operation:
    sum = operation.readlines()
    with open("jieguo.txt", "w") as result:
        for flag in sum:
            if "+" in flag:
                flag = flag.split("+")
                flag_result = ("%.2f" % (float(flag[0]) + float(flag[1])))
                result.write(str(flag_result) + '\n')
            elif "-" in flag:
                flag = flag.split("-")
                flag_result = ("%.2f" % (float(flag[0]) - float(flag[1])))
                result.write(str(flag_result) + '\n')



