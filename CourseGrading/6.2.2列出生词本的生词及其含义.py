"""
【问题描述】
生词本包含多个条目。每个条目由生词和该生词的含义组成。例如，生词name的含义是名字。编写程序，输出多个生词及其含义，列出生词本中包含的生词及其含义。
【输入形式】
输入多行。每一行包含生词及其含义。这一行内，生词和含义之间用冒号分隔。
【输出形式】
输出多行。每一行列出所有的生词及其含义，之间用空格分隔。生词按字典序从小到大排序。
【样例输入】
name:mingzi
hello:nihao
python:manshe
【样例输出】
hello nihao
name mingzi
python manshe
【提示】
1.  在Pycharm集成开发环境中，运行程序的时候如何告诉程序输入已经结束？答案是，按Ctrl + D组合键。在Windows命令行中运行程序的话，则是按Ctrl + Z组合键。
2. 使用字典的items方法能得到全部的键值对组成的列表，写法如：w_list = list(w_dict.items())，这里w_dict代表生词本。
"""
import sys
word_dict = {}
while True:
    words = sys.stdin.readline().strip()
    if words == "":
        break
    result = words.split(":")
    word_dict[result[0]] = result[1]
result = sorted(word_dict)
for i in result:
    print(i, word_dict[i])