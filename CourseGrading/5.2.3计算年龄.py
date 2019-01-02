"""
【问题描述】编写一个程序，用户输入出生日期和当前日期，计算出实际年龄。
【输入形式】用户在第一行输入出生日期，在第二行输入当前日期。日期格式为年.月.日，即中间用.分割。
【输出形式】程序在下一行输出实际年龄。
【样例输入】
1964.2.19
2001.7.21  
【样例输出】37
【样例说明】用户第一次输入的日期为出生日期，回车表示本次输入结束。第二次输入的为当前日期，回车表示本次输入结束。系统返回实际年龄
"""
byear ,bmonth, bday = input().split(".")
byear = int(byear)
bmonth = int(bmonth)
bday = int(bday)
tyear, tmonth, tday = input().split(".")
tyear = int(tyear)
tmonth = int(tmonth)
tday = int(tday)
if tyear > byear:
    if tmonth > bmonth:
        age = tyear - byear
    elif tmonth == bmonth:
        if tday >= bday:
            age = tyear - byear
        else:
            age = tyear - byear - 1
    else:
        age = tyear - byear - 1
elif tyear == byear:
        age = 0
print(age)
