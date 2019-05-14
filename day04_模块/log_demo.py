#!/usr/bin/python3
# Filename: log_demo.py

import logging

# 调试模式，实际使用请注释
#logging.basicConfig(level=logging.DEBUG)

# 正常模式
logging.basicConfig(level=logging.ERROR)

if __name__ == '__main__':
   # print('程序自身在运行')
   logging.debug('程序自身在运行')
   logging.error('程序自身在运行')
else:
   # print('我来自另一模块')
   logging.debug('我来自另一模块')
   logging.error('我来自另一模块: log_demo')