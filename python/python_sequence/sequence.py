#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
序列，包括字符串(普通字符串和unicode字符串),列表,和元组类型

"""

# 序列类型操作符
"""
seq[index] 切片操作，负索引的范围-len(seq)<=index<=-1
seq[index1:index2]
seq * expr 序列重复expr次
seq1+seq2
obj in seq
obj not in seq

"""
print('a' in 'abc')

a = [1, 2, 3]
a.extend([4, 5])
print(a)

# 用补偿来进行拓展的i企鹅片操作
s = 'abcdefgh'
print(s[::-1])  # 反转操作
print(s[::2])  # 隔一个取一个

# 内建函数
# 类型转换
list()  # 把可迭代的对象转换为列表
str()  # 把对象转为字符串
unicode()  # 把对象转成unicode字符串
tuple()  # 把一个可迭代的对象转成一个元组

print(list(s))

# 可操作类型函数
enumerate(s)
len(s)
max(s)
min(s)
reversed(s)
sorted(s)
print(sum([1, 2, 3, ]))
print(zip(s))
