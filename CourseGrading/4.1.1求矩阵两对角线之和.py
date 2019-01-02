"""
【问题描述】求4*4矩阵两对角线之和。第一行全1，第二行全2，第三行全3，第四行全4
【输入形式】无输入
【输出形式】20
"""
list = [
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]
]
sum0 = 0
for i in range(4):
    for j in range(4):
        if i == j:
            sum0 = sum0 + int(list[i][j])
for a in range(4):
    for b in range(4):
        if a + b == 3:
            sum0 += int(list[a][b])
print(sum0)