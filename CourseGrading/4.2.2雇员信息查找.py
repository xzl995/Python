"""
【问题描述】
键盘输入5个雇员的信息，雇员的属性有姓、名字、电子邮箱地址、工作单位。找出姓、名字或电子邮箱地址中有"Li"或"li"出现的雇员，输出这些雇员的信息。
【输入形式】
从键盘输入5个雇员的信息，雇员的属性有姓、名字、电子邮箱地址、工作单位。雇员信息之间隔有一行空白。
【输出形式】
输出姓、名字或电子邮箱地址中有"Li"或"li"出现的雇员的信息。雇员信息之间空一行。
【样例输入】
zhang
san
zhangsan@hotmail.com
nudt

li
si
lisi@gmail.com
nudt

wang
wu
wangwuLi@hotmail.com
nudt

zhao
zao
zhaozaoLIU@163.com
nudt

qian
qi
qianqi@163.com
nudt
【样例输出】
li
si
lisi@gmail.com
nudt

wang
wu
wangwuLi@hotmail.com
nudt
"""
def find(infor):
    infors = []
    for n in infor:
        infors.append(n)
    for i in range(len(infors)):
        if infors[i] == "L" or infors[i] == "l":
            if infors[i + 1] == "i":
                return 1
            else:
                return 0

num = 1
n = 0
for i in range(5):
    firstName = input()
    lastName = input()
    Email = input()
    address = input()
    while num <= 4:
        block = input()
        num += 1
        break
    if find(firstName) == 1 or find(lastName) == 1 or find(Email) == 1:
        print(firstName+"\n"+lastName+"\n"+Email+"\n"+address)
        print(" ")




