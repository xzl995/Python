"""
【问题描述】
从键盘输入两个举重运动员的成绩信息：
   姓名、体重、抓举成绩、挺举成绩
输出获胜运动员的姓名。
总成绩高者获胜（总成绩=抓举成绩+挺举成绩）
总成绩相同时，体重轻者获胜。
【输入形式】姓名1 体重1 抓举成绩1 挺举成绩1  姓名2 体重2 抓举成绩2 挺举成绩2 
【输出形式】获胜运动员的姓名
【样例输入】athlete1  78 120 130  athlete2 80 121 128
【样例输出】athlete1
"""
name1,weight1,z_score1,t_score1,name2,weight2,z_score2,t_score2 = input().split()
weight1 = int(weight1)
z_score1 = int(z_score1)
t_score1 = int(t_score1)
weight2 = int(weight2)
z_score2 = int(z_score2)
t_score2 = int(t_score2)
if z_score1+t_score1 > z_score2+t_score2:
    print(name1)
elif z_score1+t_score1 < z_score2+t_score2:
    print(name2)
elif weight1 < weight2:
    print(name1)
elif weight1 > weight2:
    print(name2)
