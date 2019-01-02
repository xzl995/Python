"""
【问题描述】
在Student类中增加一个成员方法，功能是判别学生是否有科目不及格，有则返回false，否则返回true。
"""
class Student():
    def __init__(self):
        self.sno = 0
        self.name = ""
        self.mathScore = 0.0
        self.engScore = 0.0
        self.proScore = 0.0

    def average(self):
        return (self.mathScore + self.engScore + self.proScore) / 3

    def allPassed(self):

        if self.mathScore < 60 or self.engScore < 60 or self.proScore < 60:
            return False
        else:
            return True


s = Student()
m, e, p = input().split()
s.mathScore = float(m)
s.engScore = float(e)
s.proScore = float(p)
if s.allPassed():
    print("All passed.")
else:
    print("Not all passed.")