""" 	
【问题描述】
输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。
【输入形式】
一个字符串。
【输出形式】
出现次数最多的字母及其出现次数
【样例输入】
abcccd
【样例输出】
c 3
"""
n = input()
word = {}
result = {}
for i in n:
    if i not in word.keys():
        word[i] = 1
    else:
        word[i] = word[i] + 1

for (key, value) in word.items():
    if value == max(word.values()):
        result[key] = value
sorted(result.keys())

for key, value in result.items():
    print(key, value)

