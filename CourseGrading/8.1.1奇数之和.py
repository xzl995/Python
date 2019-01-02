"""
【问题描述】
将1～p之间奇数顺序累加存入n中，直到其和首次等于或大于q为止或1～p之间所有奇数参与累加为止。程序输入p,q的值，输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数（分别占一行）。
【输入形式】
分两行输入p和q的值。
【输出形式】
依次输出n的值、参与累加的奇数个数，以及参与运算的最大的那个奇数
【样例输入】
1000
4000
【样例输出】
4096
64
127
"""
def ji_sum(p, q):
    num = 0
    n = 0
    max_js = 1
    for i in range(1, p + 1):
        if n < q:
            if i % 2 != 0:
                n += i
                num += 1
                max_js = i


    print(n)
    print(num)
    print(max_js)

p = int(input())
q = int(input())
ji_sum(p, q)

