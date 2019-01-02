"""
【问题描述】编写一个程序，输入一个正整数N，在屏幕上用*打印以N为边长的正六边形。
【输入形式】输入一个正整数N。
【输出形式】屏幕上输出以N为边长的正六边形。
【样例输入】
 4
【样例输出】
     ****
   *      *
  *        *
 *          *
  *        *
   *      *
     ****
【样例说明】输入的为一个正整数，打印输出一个以这个正整数为边长的正六边形．
###****
##*####*
#*######*
*########*
#*######*
##*####*
###****
#号代表空格。
"""
N = int(input())
temp = []
for i in range(N):
    if i == 0:
        a = [" " * (N - i - 1)+ "*" * N]
        temp.append(a)
    else:
        b = [" " * (N - i - 1) + "*" + " " * (N + (i - 1) * 2) + "*"]
        temp.append(b)
for i in range(len(temp)):
    for j in range(len(temp[i])):
        print(temp[i][j], end = "")
    print()

result = temp[::-1]
for i in range(1, len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end = "")
    print()




