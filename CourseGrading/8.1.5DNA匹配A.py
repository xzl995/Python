"""
【问题描述】编写与字符串对象的find方法功能相似的函数find(srcString, substring, start, end)，作用是在srcString串的下标start到下标end之间的片段中寻找subString串的第一次出现的位置，返回该位置值；如果没找到，返回-1。
编写程序，输入源串和子串，检验find(someString, substring,start,end)是否正确。
【输入形式】按照somestrig,substring,start,end的顺序输入，各成分之间由空格隔开。Somestring和substring均由A/T/C/G四个字母组成。start和end由自然数构成。
【输出形式】当匹配成功时，输出子串在DNA字符串的位置，以子串第一个字母在DNA字符串中匹配位置的下标；当匹配失败时，输出-1。
【样例输入】ATCGGCGCGGCGT CGG 0 10
【样例输出】2
【样例说明】下标从0开始计数。
"""
def find(srcString, subString, start, end):
    for i in range(start, end + 1):
        for j in range(len(subString)):
            if srcString[i] == subString[j]:
                flag = srcString.index(subString[j])