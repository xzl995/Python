"""
【问题描述】编写程序实现计算两点之间的距离
【输入形式】标准输入的四行双精度数据分别表示第一个点的横坐标、第一个点的纵坐标、第二个点的横坐标、第二个点的纵坐标。
【输出形式】标准输出的一行双精度数据表示两点之间的距离。
【样例输入】0.0
            0.0
            3.0
            4.0
【样例输出】5.0
【样例说明】
【提示】
Python中如何计算浮点数f的平方根，答案是调用math模块的sqrt函数，如下： 
         math.sqrt(f)
要使用math模块（math模块包含有大量数学计算函数），首先要在程序文件头部引入math模块，写法是：
    import math
"""
import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
f = (x1-x2)**2+(y1-y2)**2
print(math.sqrt(f))

