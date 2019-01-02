"""
【问题描述】
补充代码，定义另一个学生对象，输入其成绩，求平均成绩并输出
"""
class Student():
    def __init__(self, math, eng, pro):
        self.sno = 0
        self.name = ""
        self.mathScore = math
        self.engScore = eng
        self.proScore = pro

    def average(self):
        return (self.mathScore + self.engScore + self.proScore) / 3


m, e, p = input().split()
m = float(m)
e = float(e)
p = float(p)
s = Student(m, e, p)
print(s.average())

m1,e1,p1 = (float(i) for i in input().split())
s1 = Student(m1, e1, p1)
print(s1.average())


