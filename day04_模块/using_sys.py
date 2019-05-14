#!/usr/bin/python3
# 文件名: using_sys.py
# 使用 python 标准库中模块的例子 
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')