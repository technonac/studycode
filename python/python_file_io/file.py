#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
文件
file()/open() 具有相同用的功能，可以任意替换
"""
# 文件内建方法
import sys

f = open('test.txt', 'r')
# 输入
f.read(-1)  # 读取字节到字符串中
f.readline()  # 读取整行包括行结束符
f.readlines()  # 读取所有行把他们作为字符串列表返回
# 文件迭代
for eachLine in f:
    pass

# 输出
f = file('test.txt', 'w')
f.write('')
f.writelines('')

# 关闭文件
# f.close()

# 文件内建属性
print(f.name)
print(f.mode)

"""
标准文件
sys.stdin 标准输入 一般是键盘
sys.stdout 标准输出 到显示器的缓冲输出
sys.stderr 标准错误 到屏幕的非缓冲输出

命令行参数 
sys.argv 命令行参数的列表
len(sys.argv) 命令行参数的个数argc
sys.argv[0] 程序的名称
"""
print(sys.argv)
