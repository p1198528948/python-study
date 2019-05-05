#!/usr/bin/env python3
#
print("将华氏温度转为摄氏温度")
print("公式 C = (F - 32) / 1.8")
# 这里必须是 int
temperature_value = int(input("请输入温度值: ")) 

fahrenheit = temperature_value

celsius = (fahrenheit - 32) / 1.8 # 转换为摄氏度
# {:5d} 的意思是替换为 5 个字符宽度的整数，宽度不足则使用空格填充。 
# {:7.2f}的意思是替换为为7个字符宽度的保留两位的小数，小数点也算一个宽度，宽度不足则使用空格填充。
# 其中7指宽度为7，.2f指保留两位小数。
print("{:5d} {:7.2f}".format(fahrenheit , celsius))

# print("Fahrenheit Celsius")
# while fahrenheit <= 250:

#     fahrenheit = fahrenheit + 25