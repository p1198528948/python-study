#!/usr/bin/env python3
amount = float(input("请输入存款数额: "))  # 输入数额
inrate = float(input("请输入存款利率: "))  # 输入利率
period = int(input("请输入存款期限: "))  # 输入期限

# 账户总金额
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1