"""
【问题描述】编写一个程序，输出当前时间的下一秒。
【输入形式】用户在第一行按照小时:分钟:秒的格式输入一个时间。
【输出形式】程序在下一行输出这个时间的下一秒。
【样例输入】23:59:59
【样例输出】0:0:0
【样例说明】用户按照格式输入时间，程序输出此时间的下一秒。
"""
time = input().split(":")

if int(time[2]) != 59:
    time[2] = int(time[2]) + 1
    print(time[0] + ":" + time[1] + ":" + str(time[2]))
elif int(time[1]) != 59:
    time[1] = int(time[1]) + 1
    print(time[0] + ":" + str(time[1]) + ":" + "0")
elif int(time[0]) != 23:
    time[0] = int(time[0]) + 1
    print(str(time[0]) + ":" + "0" + ":" + "0")
else:
    print("0:0:0")