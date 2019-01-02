"""
【题目描述】
编写一个数组求和函数Add(a1, a2); a1是第一个数组，a2是第二个数组，函数返回两者之和result。假设a1={2, 4, 5, 8}, a2={1, 0, 4, 6}，则result={3, 4, 9, 14};
编写程序，依次输入n, a1, a2, 输出result。n是数组的长度，两个数组的长度都为n。
【输入形式】
第一行是数组长度n。
第二行是组成数组a1的n个整数。
第三行是组成数组a2的n个整数。
【输出形式】
结果数组的n个元素。用一个空格隔开。
【输入样例】
4
2 4 5 8
1 0 4 6
【输出样例】
3 4 9 14
"""
def Add(a1, a2):
    result = []
    for i in range(0, len(a1)):
        result.append(int(a1[i]) + int(a2[i]))
    return result

n = int(input())
a1 = input().split()
a2 = input().split()
print(" ".join(str(i) for i in Add(a1, a2)))

