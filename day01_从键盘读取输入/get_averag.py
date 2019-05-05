#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("请输入十位男性的身高(单位CM):")
while count < N:
	number = float(input())
	sum = sum + number
	count = 1 + count
	print("第 {} 位身高: {}".format(count, number))

# 总和：
print("总和： {}".format(sum))

# 平均值:
average = sum / N
print("平均身高: {:.2f} 米".format(average/100))

print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))