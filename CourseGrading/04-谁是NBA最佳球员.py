# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 16:05:34 2018

@author: 59569
"""

import csv

csv_data = csv.reader(open('player_regular_season.csv', 'r'))
csv_data = list(csv_data)

print("输入你想查看的球员人数：")
n = int(input())
title = ["ilkid", "firstname", "lastname", "gp", "minutes", "pts", "reb", "asts", "stl", "blk", "fga", "fgm", "fta", "ftm", "turnover",]
data = []
for i in range(1, len(csv_data) - 1):
    flag = [" " for f in range(len(title))]
    for j in range(len(csv_data[0])):
        if csv_data[0][j] in title:
            flag[title.index(csv_data[0][j])] = csv_data[i][j]
    data.append(flag)

# 处理null值
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "NULL":
            data[i][j] = 0

# 效率值
efficiency_list = []
for i in range(len(data)):
    eff_flag = []
    name = data[i][title.index("firstname")] + " " + data[i][title.index("lastname")]
    eff_flag.append(name)
    fz = (int(data[i][title.index("pts")]) + int(data[i][title.index("reb")]) + int(data[i][title.index("asts")]) + int(data[i][title.index("blk")])) - (((int(data[i][title.index("fga")]) - int(data[i][title.index("fgm")])) + (int(data[i][title.index("fta")]) - int(data[i][title.index("ftm")]))) + int(data[i][title.index("turnover")]))
    efficiency = int(fz / int(data[i][title.index("gp")]))
    eff_flag.append(efficiency)
    efficiency_list.append(eff_flag)

efficiency_dict = {}
count = 0
sum_efficiency = 0
for i in range(len(efficiency_list)):
    if efficiency_list[i][0] not in efficiency_dict:
        sum_efficiency = efficiency_list[i][1]
        count = 1
        efficiency_dict[efficiency_list[i][0]] = [sum_efficiency, count]
    else:
        sum_efficiency = efficiency_dict[efficiency_list[i][0]][0] + efficiency_list[i][1]
        count = efficiency_dict[efficiency_list[i][0]][1] + 1
        efficiency_dict[efficiency_list[i][0]] = [sum_efficiency, count]

new_eff_list = []
for key, value in efficiency_dict.items():
    flag = []
    new_efficiency = round(value[0] / value[1])
    flag.append(key)
    flag.append(new_efficiency)
    new_eff_list.append(flag)

new_eff_list = sorted(new_eff_list, key = lambda e : e[1], reverse = True)

print("效率最高的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("efficiency") / 2)
space = " " * times
print(5 * " ", "Name", space, "efficiency")
print(45 * "-")

for i in range(n):
    time = 25 - len(new_eff_list[i][0]) - len(str(new_eff_list[i][1]))
    space = " " * time
    print(new_eff_list[i][0], space, ":", "%12d" % new_eff_list[i][1])

print()
print()


# 计算函数
def calculate(informations):
    informations_dict = {}
    for i in range(len(data)):
        name = data[i][title.index("firstname")] + " " + data[i][title.index("lastname")]
        if name not in informations_dict:
            informations_dict[name] = int(data[i][title.index(informations)])
        else:
            informations_dict[name] = informations_dict[name] + int(data[i][title.index(informations)])

    informations_dict = sorted(informations_dict.items(), key=lambda i: i[1], reverse=True)

    return informations_dict


# 最长上场时间
player_time = calculate("minutes")
print("上场时间最长的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("上场时间（分钟）") / 2)
space = " " * times
print(5 * " ", "Name", space, "上场时间（分钟）")
print(50 * "-")

for i in range(n):
    time = 32 - len(player_time[i][0]) - len(str(player_time[i][1]))
    space = " " * time
    print(player_time[i][0], space, ":", "%12d" % player_time[i][1])

print()
print()

# 比赛场数最多
game_count = calculate("gp")
print("比赛场数最多的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("比赛场数") / 2)
space = " " * times
print(5 * " ", "Name", space, "比赛场数")
print(50 * "-")

for i in range(n):
    time = 30 - len(game_count[i][0]) - len(str(game_count[i][1]))
    space = " " * time
    print(game_count[i][0], space, ":", "%12d" % game_count[i][1])

print()
print()


# 得分最多
score = calculate("pts")
print("得分最多的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("分数") / 2)
space = " " * times
print(5 * " ", "Name", space, "分数")
print(50 * "-")

for i in range(n):
    time = 30 - len(score[i][0]) - len(str(score[i][1]))
    space = " " * time
    print(score[i][0], space, ":", "%12d" % score[i][1])

print()
print()


# 篮板最多
backboard = calculate("reb")
print("篮板最多的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("篮板次数") / 2)
space = " " * times
print(5 * " ", "Name", space, "篮板次数")
print(50 * "-")

for i in range(n):
    time = 30 - len(backboard[i][0]) - len(str(backboard[i][1]))
    space = " " * time
    print(backboard[i][0], space, ":", "%12d" % backboard[i][1])

print()
print()

# 罚球最多
penalty_shot = calculate("fta")
print("罚球最多的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("罚球次数") / 2)
space = " " * times
print(5 * " ", "Name", space, "罚球次数")
print(50 * "-")

for i in range(n):
    time = 35 - len(penalty_shot[i][0]) - len(str(penalty_shot[i][1]))
    space = " " * time
    print(penalty_shot[i][0], space, ":", "%12d" % penalty_shot[i][1])

print()
print()


# 罚球命中最多
foul_shot = calculate("ftm")
print("罚球命中最多的前" + str(n) + "个球员：" "\n")
times = int(30 - len("Name") - len("罚球命中次数") / 2)
space = " " * times
print(5 * " ", "Name", space, "罚球命中次数")
print(50 * "-")

for i in range(n):
    time = 35 - len(foul_shot[i][0]) - len(str(foul_shot[i][1]))
    space = " " * time
    print(foul_shot[i][0], space, ":", "%12d" % foul_shot[i][1])

