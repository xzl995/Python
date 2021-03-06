"""
【问题描述】编写一个程序，输入N个用户的姓名和电话号码，按照用户姓名的词典顺序排列输出用户的姓名和电话号码。
【输入形式】用户首先在第一行输入一个正整数，该正整数表示待排序的用户数目，然后在下面多行输入多个用户的信息，每行的输入格式为：姓名 电话。以回车结束每个用户的输入。
【输出形式】程序输出排序后的结果。每行的输出结果格式也是： 姓名 电话。姓名和电话字段中间没有空格，要求用户姓名不能超过10个字符，超出10个字符时候只取前10个字符作为姓名。电话号码不能超过10位，超过10位时只按10位处理。输出姓名、电话字段各占12个字符宽，输出格式采用默认对齐方式。另外，用户的数量要求不超过50个。
【样例输入】
3
amethystic 1234567
amethyst 654321
wangwei 7645434
【样例输出】
####amethyst######654321
##amethystic#####1234567
#####wangwei#####7645434
【样例说明】程序根据用户姓名的词典顺序排序，最后按照姓名#电话的格式输出。另外，由于规定姓名和电话之间用空格分割，所以输入姓名时请将姓和名一起输入，中间不要有空格。另外输出时候程序将自动补齐12字符宽。程序输出结尾有个回车符。上述样例输出中，#实际上是代表空格。
"""
num = int(input())
tels = []
if num <= 50:
    for n in range(num):
        tels.append(input())
    tels.sort()
    name_tel = []
    for m in range(num):
        tel = tels[m]
        name_tel = tel.split(" ")
        if len(name_tel[0]) > 10 or len(name_tel[1]) >10:
            name_tel[0] = name_tel[0][0 : 10]
            name_tel[1] = name_tel[1][0 : 10]
        print(name_tel[0].rjust(12, " ") + name_tel[1].rjust(12, " "))


