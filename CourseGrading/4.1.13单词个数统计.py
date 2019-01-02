"""
编写一个程序，输入一个句子，然后统计出这个句子当中不同的单词个数。例如，对于句子“one little two little three little boys"，总共有5个不同的单词，one, little, two, three, boys。
说明：
（1）句子当中包含有空格。
（2）输入的句子当中只包含英文字符和空格，单词之间用一个空格隔开。
（3）不用考虑单词的大小写，假设输入的都是小写字符。
（4）句子长度不超过100个字符
（5）该问题实现的基本思路是：
a. 先定义一个存储不同单词的列表
b. 每次从句子中读取下一个单词
c.不断将新读取的单词加入该单词列表中。若单词列表中已存在该单词，则不添加。
【输入形式】
输入只有一行，为输入的句子
【输出形式】
输出只有一行，为句子当中不同的单词个数
【样例输入】
one little two little three little boys
【样例输出】
5
"""
words = input().split()
temp = []
for word in words:
    if word in temp:
        temp = temp
    else:
        temp.append(word)
print(len(temp))

