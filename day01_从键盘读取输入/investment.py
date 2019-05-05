#!/usr/bin/env python3
amount = float(input("请输入存款数额: "))  # 输入数额
inrate = float(input("请输入存款利率: "))  # 输入利率
period = int(input("请输入存款期限: "))  # 输入期限

# 账户总金额
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    # 字符串格式化，大括号和其中的字符会被替换成传入 str.format() 的参数，
    # 即 year 和 value。其中 {:.2f} 的意思是替换为 2 位精度的浮点数。
    print("第 {} 年，账户金额为： ￥ {:.2f}".format(year, value))
    amount = value
    year = year + 1