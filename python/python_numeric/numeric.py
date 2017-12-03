#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
数字提供了标量存储和直接访问，它是不可更改类型，也就是说变更数字的值会生成新的对象
"""
# 转换工厂函数
import math
import random

int(4)
long(42)
float(4)
bool([])

# 功能函数
abs(-1)
coerce(1, 2)
pow(2, 2)
round(3.45)
math.floor(0.5)

# 仅用于整型的函数
hex(255)
print(hex(255))
oct(255)
print(oct(255))
print(chr(97))  # 将ascii值的数字转换成ascii字符
print(ord('a'))  # 接收一个ascii或者unicode返回相应的值

# 数字类型相关的模块
"""
decimal: 十进制浮点运算类Decimal
array: 高校数值数组
math: 标准c库数学运算函数
operator:数字操作符的函数实现
random: 多种伪随机数生成器
"""
print("-" * 15)
# random模块
print(random.randint(0, 10))  # 两个整型参数之前随机整型
print(random.randrange(0, 10, 2))
print(random.uniform(0, 10))  # 返回二者之间的一个浮点型
print(random.random())  # 返回0到1直接按的小数
print(random.choice([1, 2, 3, 5, ]))
