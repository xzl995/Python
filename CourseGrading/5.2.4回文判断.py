"""
【问题描述】
回文是正读和倒读都一样的句子。读入一个最大长度不超过50个字符的句子，判断其是否是回文。
【输入形式】
输入一个最大长度不超过50个字符的句子
【输出形式】
如果是回文字符串，则输出Yes，否则输出No
【输入样例】
abcba
【输出样例】
Yes
【样例说明】
输入abcba，判断出它是回文。
"""
n = input()
temp = []
temp1 = []
temp2 = []
for i in n:
    temp.append(i)
length = len(temp) // 2
if len(n) % 2 != 0:
    temp.pop(length)
temp1 = temp[0 : length]
i = len(temp) - 1
while i >= length:
    temp2.append(temp[i])
    i -= 1
if len(temp) == 0:
    print("Yes")
for n in range(len(temp1)):
    if temp1[n] != temp2[n]:
        print("No")
        break
    elif n >= len(temp1) - 1:
        print("Yes")




# for i in n :
#     temp.append(i)
# a = 0
# b = len(temp) - 1
# while 0 <= a <= b:
#     if temp[a] == temp[b]:
#         a += 1
#         b -= 1
#         if a > b:
#             print("Yes")
#     else:
#         print("No")

