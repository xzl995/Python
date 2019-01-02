"""
【问题描述】
生词本包含多个条目。每个条目由生词和该生词的含义组成。例如，生词name的含义是名字。编写程序，输出所有的含义。
【输入形式】
输入多行。每一行包含生词及其含义。这一行内，生词和含义之间用冒号分隔。
【输出形式】
输出一行。列出所有的含义，之间用空格分隔。含义按字典序从小到大排序
【样例输入】
name:mingzi
hello:nihao
python:manshe
【样例输出】
manshe mingzi nihao
【提示】
1.  在Pycharm集成开发环境中，运行程序的时候如何告诉程序输入已经结束？答案是，按Ctrl + D组合键。在Windows命令行中运行程序的话，则是按Ctrl + Z组合键。
2. 使用字典的values方法能得到全部的值，就是这一题的含义。
"""
import sys
word_dict = {}
while True:
    words = sys.stdin.readline().strip()
    if words == "":
        break
    result = words.split(":")
    word_dict[result[0]] = result[1]
result = sorted(word_dict.values())
for i in result:
    print(i, end = " ")