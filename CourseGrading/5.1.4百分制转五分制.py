"""
【问题描述】
给出一个百分制成绩，要求输出成绩等级A、B、C、D、E。90分以上为A，80~89分为B，70~79分为C，60~69分为D，60分以下为E。如果输入小于0或大于100的分数，则输出“Not valid”（注意大小写须一致）。
【输入形式】
输入一个可能带小数点的分数。
【输出形式】
根据对应关系，输出输入分数所对应的五分制分数档。
【样例输入】
91
【样例输出】
A
【样例输入2】
901
【样例输出2】
Not valid
"""
score = int(input())
if score < 0 or score > 100:
    print("Not valid")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif 0 <= score < 60:
    print("E")