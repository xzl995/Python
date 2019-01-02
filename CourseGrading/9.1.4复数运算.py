"""
【问题描述】
编程实现两个复数的运算。
要求：
（1）定义一个类来实现复数。
（2）复数之间的加法、减法、乘法和除法分别用方法来实现。
【输入形式】
运算符号(+,-,*,/) a b c d. 
如果是除法，c，d不同时为0
【输出形式】
a+bi，当b>0时。a-bi，当b<0时。a,b都保留两位小数。
【样例输入】
-  2.5 3.6 1.5 4.9
【样例输出】
1.00-1.30i
【样例输入】
+  1.234 -3.456 -1.234 3.456
【样例输出】
0.00+0.00i
"""
class Complex:
    # def __init__(self, num_list):
    #     self.num_list = num_list
    def ys(self, num_list):
        num_list = num_list.split()
        if num_list[0] == "+":
            if float(num_list[2]) + float(num_list[4]) < 0:
                return str("%.2f" % (float(num_list[1]) + float(num_list[3]))) + str("%.2f" %(float(num_list[2]) + float(num_list[4]))) + "i"
            else:
                return str("%.2f" % (float(num_list[1]) + float(num_list[3]))) + "+" + str("%.2f" % (float(num_list[2]) + float(num_list[4]))) + "i"
        elif num_list[0] == "-":
            if float(num_list[2]) - float(num_list[4]) < 0:
                return str("%.2f" % (float(num_list[1]) - float(num_list[3]))) + str("%.2f" % (float(num_list[2]) - float(num_list[4]))) + "i"
            else:
                return str("%.2f" % (float(num_list[1]) - float(num_list[3]))) + "+" + str("%.2f" % (float(num_list[2]) - float(num_list[4]))) + "i"
        elif num_list[0] == "*":
            # (a+bi)*(c+di)=(ac－bd)+(bc+ad)i
            if (float(num_list[2]) * float(num_list[3])) + (float(num_list[1]) * float(num_list[4])) < 0:
                return str("%.2f" % ((float(num_list[1]) * float(num_list[3])) - (float(num_list[2]) * float(num_list[4])))) + str("%.2f" % ((float(num_list[2]) * float(num_list[3])) + (float(num_list[1]) * float(num_list[4])))) + "i"
            else:
                return str("%.2f" % ((float(num_list[1]) * float(num_list[3])) - (float(num_list[2]) * float(num_list[4])))) + "+" + str("%.2f" % ((float(num_list[2]) * float(num_list[3])) + (float(num_list[1]) * float(num_list[4])))) + "i"
        elif num_list[0] == "/":
            #(a+bi)/(c+di)=(ac+bd)/(c2+d2) +((bc-ad)/(c2+d2))i
            if (((float(num_list[2]) * float(num_list[3])) - (float(num_list[1]) * float(num_list[4]))) / ((float(num_list[3]) ** 2) + (float(num_list[4]) ** 2))) < 0:
                return str("%.2f" % (((float(num_list[1]) * float(num_list[3])) + (float(num_list[2]) * float(num_list[4]))) / ((float(num_list[3]) ** 2) + (float(num_list[4]) ** 2)))) + str("%.2f" % (((float(num_list[2]) * float(num_list[3])) - (float(num_list[1]) * float(num_list[4]))) / ((float(num_list[3]) ** 2) + (float(num_list[4]) ** 2)))) + "i"
            else:
                return str("%.2f" % (((float(num_list[1]) * float(num_list[3])) + (float(num_list[2]) * float(num_list[4]))) / ((float(num_list[3]) ** 2) + (float(num_list[4]) ** 2)))) + "+" + str("%.2f" % (((float(num_list[2]) * float(num_list[3])) - (float(num_list[1]) * float(num_list[4]))) / ((float(num_list[3]) ** 2) + (float(num_list[4]) ** 2)))) + "i"

num_list = input()
num_Com = Complex()
print(num_Com.ys(num_list))