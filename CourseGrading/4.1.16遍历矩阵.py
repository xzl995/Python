"""
【问题描述】
输入一个单词矩阵，输出单词序列。
【输入形式】
3行。每一行有3列，元素之间用空格分隔。每一个元素是一个单词（字母组成的字符串，不含空格）。
【输出形式】
一行。先输出第1列各行，接着第2列各行，再第3列各行。单词之间用一个空格间隔。
【样例输入】
one two three
on to to
go hello ear
【样例输出】
one on go two to hello three to ear
"""
temp = []
for i in range(3):
    word = input().split()
    temp.append(word)
for a in range(3):
    for b in range(3):
        print(temp[b][a], end = " ")