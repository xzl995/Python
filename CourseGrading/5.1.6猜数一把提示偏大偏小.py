"""
【问题描述】
编写“猜数游戏”程序，功能是：如果用户输入的数等于程序选定的数（该数设定为10），则输出“you win”，否则如果大于选定的数，则输出“too big”，反之输出“too small”。
【输入形式】
输入一个整数。
【输出形式】
根据与选定值的大小关系，做相应的输出（大小写一致）。
【样例输入】
9
【样例输出】
too small
"""
num = 10
guest = int(input())
if guest == num:
    print("you win")
elif guest > num:
    print("too big")
else:
    print("too small")