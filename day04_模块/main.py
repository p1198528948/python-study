#!/usr/bin/python3
# Filename: test.py
 
# 导入模块
import support
 
import fibo

import using_name
import log_demo
# 现在可以调用模块里包含的函数了
support.print_func("Runoob")

print("调用模块:" + fibo.__name__)
fibo.fib(1000)
