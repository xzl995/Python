import csv

csv_data = csv.reader(open("StandardPoors500-week-20141018.csv"))
csv_data = list(csv_data)
title = csv_data[0]

# 删除后面不满一季度的数据
csv_data = csv_data[1:(len(csv_data) - ((len(csv_data) - 1) % 13))]
csv_data = csv_data[::-1]
csv_data.insert(0, title)


# 定义一个三维列表data存储数据，按一个季度即13周来做一个元素
data = []
for i in range(1, len(csv_data)):
    if (i - 1) % 13 == 0 and (i + 1) != len(csv_data):
        flag = []
        flag.append([csv_data[i][0], csv_data[i][1], csv_data[i][4], csv_data[i][-1]])
    else:
        flag.append([csv_data[i][0], csv_data[i][1], csv_data[i][4], csv_data[i][-1]])
    if len(flag) % 13 == 0:
        data.append(flag)

# 差值
def D_value(data):
    d_value = []
    for i in range(len(data)):
        flag = []
        for j in range(len(data[0])):
            flag.append(float(data[i][j][-1]))
        d_value.append(flag)
    max_value = {}
    for i in range(len(d_value)):
        max_value[i + 1] = (round((max(d_value[i]) - min(d_value[i])), 3))
    max_value = sorted(max_value.items(), key = lambda m : m[1], reverse = True)
    return max_value

d_value = D_value(data)
# 最大差值
print("-----------------------最大差值的季节-------------------------")
for i in range(len(d_value)):
    if d_value[i][1] == d_value[0][1]:
        print("最大差值为第" + str(d_value[i][0]) + "个季度：")
        print("起始日期:" + data[d_value[i][0] - 1][0][0])
        print("结束日期:" + data[d_value[i][0] - 1][-1][0])
        print("最大差值为：" + str(d_value[i][1]))
        print()

# 最小差值
print("-----------------------最小差值的季节-------------------------")
for i in range(len(d_value)):
    if d_value[i][1] == d_value[-1][-1]:
        print("最小差值为第" + str(d_value[i][0]) + "个季度：")
        print("起始日期:" + data[d_value[i][0] - 1][0][0])
        print("结束日期:" + data[d_value[i][0] - 1][-1][0])
        print("最小差值：" + str(d_value[i][1]))
        print()


# 变化值
def Change_Value(data):
    c_value = {}
    for i in range(len(data)):
        c_value[i + 1] = round((float(data[i][0][1]) - float(data[i][-1][2])), 3)
    c_value = list(c_value.items())
    return c_value

C_Value = Change_Value(data)
abs_value = {}
for key, value in C_Value:
    abs_value[key] = abs(value)
min_abs_value = sorted(abs_value.items(), key=lambda a: a[1])
max_abs_value = sorted(abs_value.items(), key = lambda a : a[1], reverse = True)

N = 1
print("-----------------------变化值的绝对值最小的10个季度-------------------------")
while N <= 10:
    print("第" + str(min_abs_value[N - 1][0]) + "个季度：")
    print("起始日期:" + data[min_abs_value[N - 1][0] - 1][0][0])
    print("结束日期:" + data[min_abs_value[N - 1][0] - 1][-1][0])
    print("变化值：" + str(C_Value[min_abs_value[N - 1][0] - 1][1]))
    print()
    N += 1

i = 1
print("-----------------------变化值的绝对值最大的10个季度-------------------------")
while i <= 10:
    print("第" + str(max_abs_value[i - 1][0]) + "个季度：")
    print("起始日期:" + data[max_abs_value[i - 1][0] - 1][0][0])
    print("结束日期:" + data[max_abs_value[i - 1][0] - 1][-1][0])
    print("变化值：" + str(C_Value[max_abs_value[i - 1][0] - 1][1]))
    print()
    i += 1
