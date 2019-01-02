"""
【问题描述】
编程实现：从键盘输入5个分数，计算平均分。 
【输入形式】
5个分数，每个分数占一行。
 【输出形式】
新起一行输出平均分。
【样例输入】
60.5 
61.5 
61 
61 
61
【样例输出】
61
【提示】
输入分数时不用输入提示。输出平均分，无须进行格式控制。
"""
score1 = float(input())
score2 = float(input())
score3 = float(input())
score4 = float(input())
score5 = float(input())
sum = score1+score2+score3+score4+score5
print(sum/5)

