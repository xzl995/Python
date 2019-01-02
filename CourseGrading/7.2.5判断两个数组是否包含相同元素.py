"""
【问题描述】
编写一个函数 same_set(a, b)，该函数检查相等长度的两个数组是否包含相同的元素,若包含相同的元素, 则返回1,否则返回0。
不考虑元素的顺序，如果元素重复，重复次数也须相同。
【输入形式】
从键盘输入两个数组，第一行输入数组元素个数，第二行输入第一个数组的各个值，第三行输入第二个数组的各个值。值与值之间用空格间隔。
【输出形式】
如果两个数组包含的元素相同，打印1，否则，打印0。
【样例输入】
7
11 16 9 7 4 1 11
11 11 7 9 16 4 1

【样例输出】
1
【样例说明】
两个数组中均包含11，4，7，9，1，16，而且11的重复次数有两次。
"""
def same_set(a,b):
    if sorted(a) == sorted(b):
        return 1
    else:
        return 0

n = int(input())
a = (int(i) for i in input().split())
b = (int(i) for i in input().split())
print(same_set(a, b))

# n = int(input())
# num1 = input().split()
# num2 = input().split()
# for i in num1:
#     if i in num2:
#         print(1)
#         break
#     else:
#         print(0)