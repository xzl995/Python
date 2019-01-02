"""
【问题描述】
输入三位数字N，求两位数AB（其中个位数字为B，十位数字为A，且有0 < A < B <=9）。使得下列等式成立：
 AB x BA = N
其中BA是把AB中个、十位数字交换所得的两位数。
编写程序，接收控制台输入的三位整数N，求解A，B并输出。
如果没有解则输出No Answer。
【输入形式】
从键盘输入整数N。
【输出形式】
输出只有一行，包含两个数字A和B。输出时两个数字紧密输出，不使用其它字符进行分隔。
【样例输入】
976
【样例输出】
16
【样例说明】
输入整数N=976。经计算得16*61=976。可得a=1, b=6。将两个字符依次输出。
"""
n = int(input())
temp = []
for A in range(1, 10):
    for B in range(1, 10):
       if (A * 10 + B) * (B * 10 + A) == n:
           temp.append(int(str(A) + str(B)))
       else:
           continue
if len(temp)!= 0:
    print(min(temp))
else:
    print("No Answer")
