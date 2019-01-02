import  random
import math

continuing = True
while continuing:
    n = random.randint(50, 100000)
    c = math.log2(n)
    number = random.randint(1, n)
    print(number)
    print("我已经想好了50到"+str(n)+"之间的一个数。")
    for i in range(int(c)):
        print("你猜一猜看是什么数：")
        guess = int(input())

        if guess == number:
            print("你猜对了。恭喜！")
            break
        elif guess < number:
            print("猜小了")
        else:
            print("猜大了")

    if guess != number:
        print("你猜的都不对。我想的数字是" + str(number) + ".")

    print("再猜一轮？(yes/no)")
    continuing = input().lower().startswith('y')