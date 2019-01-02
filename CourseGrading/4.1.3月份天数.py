"""
【问题描述】
编写一个函数 day_of_month(year, month)
编写程序输入年(year)、月(month)，调用该函数，返回该年份该月的天数，输出返回的天数。
公历闰年的计算方法为：
    年份能被4整除且不能被100整除的为闰年
    或者，年份能被400整除的是闰年。
【输入描述】
共一行。有两个整数，第一个是年份，第二个是月份。年份和月份之间以一个空格隔开。
【输出描述】 
输出该年该月的天数。
【输入示例】
2017 11
【输出示例】
30
"""
def day_of_month(year, month):
    big_month = [1, 3, 5, 7, 8, 10, 12]
    small_month = [4, 6, 9, 11]
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            print(29)
        else:
            print(28)
    elif month in big_month:
        print(31)
    else:
        print(30)

year, month = input().split()
year = int(year)
month = int(month)
day_of_month(year, month)
