#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
函数式编程
"""
from random import randint

import math

"""
匿名函数与lambda
lambda [arg1,arg2,...,argN]:expression
匿名是因为不需要以标准的方式来声明
def add(x,y):return x+y <=> lambda x,y:x+y
"""

print(lambda: True)

a = lambda x, y=2: x + y
print(a(1))
print(a(1, 3))

b = lambda *z: z
print(b(23, 'xyz'))

"""
内建函数
apply(func [,nkw][,kw]) 用可选的参数来调用func
filter(func,seq) 调用一个布尔函数func来迭代遍历每个seq中的元素，返回一个是func返回值为true的元素的序列
map(func[,seq1][,seq2]) 将函数func用于给定的序列s的每个元素。并用一个列表来提供返回值
reduce(func[,seq][,init])
"""
# filter
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))

print(filter(lambda n: n % 2, allNums))
# map
print(map(lambda x: x ** 2, range(6)))
print([x ** 2 for x in range(6)])

# 并行迭代每个元素，然后调用func(seq[0],seq[1])
print(map(lambda x, y: x + y, [1, 3, 5], [2, 4, 6]))

print(map(None, [1, 3, 5], [2, 4, 6]))
print(zip([1, 3, 5], [2, 4, 6]))

# reduce 使用一个二元函数(一个接收带两个值作为输入,进行了一些计算然后返回一个值作为输出),一个序列，和一个可选的初始化器,
# 卓有成效地将那个列表的内容减少为一个单一的值
"""
reduce(func,[1,2,3]) = func(func(1,2),3)
"""


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3]))
