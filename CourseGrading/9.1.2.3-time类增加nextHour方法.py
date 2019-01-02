"""
【问题描述】
补充类的成员方法nextHour定义。nextHour的方法是走向下一个钟点。采用的是24小时制。
"""
class Time():
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def setTime(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s


    def showTime(self):
        print(str(self.hour) + ':' + str(self.minute) + ':' + str(self.second))

    def nextHour(self):
        if self.hour == 23:
            print(str("0") + ':' + str(self.minute) + ':' + str(self.second))
        else:
            print(str(self.hour + 1) + ':' + str(self.minute) + ':' + str(self.second))



t = Time()
t.showTime()

h, m, s = input().split()
h = int(h)
m = int(m)
s = int(s)

t.setTime(h, m, s)
t.showTime()
t.nextHour()
t.showTime()
