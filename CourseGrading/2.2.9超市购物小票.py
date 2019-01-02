"""
【问题描述】某超市促销，对购买的第二件商品（不限商品类别）打9折。路人甲购买两件商品，请按要求输出购物小票。
【输入形式】两个商品的原价
【输出形式】两个商品的购买价格及总价（请注意保留小数点后两位有效数字）。输出的每一行占16格。价格和总价靠右对齐。
【样例输入】
5.6  78.95
【样例输出】
            5.60
           71.06
----------------
Total:     76.66
"""
price1,price2 = input().split()
price1 = float(price1)
price2 = float(price2)
price2 = price2*0.9
sum = price1+price2
price1 = str('%.2f' % price1)
price2 = str('%.2f' % price2)
sum = str('%.2f' % sum)
print(price1.rjust(16))
print(price2.rjust(16))
print('----------------')
print('Total:'+sum.rjust(10))



