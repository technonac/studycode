#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
列表解析 list comprehension,动态创建列表

[expr for iter_var in iterable]

for循环，迭代iterable对象的所有条目
expr应用于序列的每个成员
最后的结果值时该表达式产生的列表

[expr for iter_var in iterable if cond_expr]
这个语法在迭代时会过滤或捕获满足条件表达式cond_expr的序列成员
"""

# map() 对所有的列表成员应用一个操作
ma = map(lambda x: x ** 2, range(6))
print(ma)

# 列表解析
lcm = [x ** 2 for x in range(6)]
print(lcm)

# filter() 给予一个条件表达式过滤成员列表
seq = [11, 10, 9, 9, 10, 10, 9, 8, 23, 9, 7, 18, 12, 11, 12]
fi = filter(lambda x: x % 2, seq)
print(fi)

# 列表解析if
lcf = [x for x in seq if x % 2]
print(lcf)

"""
生成器表达式 - 列表解析的一个扩展
生成器时特定的函数，允许你返回一个值，然后'暂停'代码的执行，稍后恢复
列表解析的一个不足就是必要生成所有的数据，用以创建整个列表。生成器表达式通过结合列表解析和生成器解决了这个问题

生成器表达式并不真正创建数字列表，而是返回一个生成器，这个生成器在每次计算出一个条目后，把这个条目产生出来。
生成器表达式使用了延迟计算(lazy evaluation)，所以它在使用内存上更高效.

列表解析
[expr for iter_var in iterable if cond_expr]
生成器表达式
(expr for iter_var in iterable if cond_expr)
"""
rows = [1, 2, 3, 17]


def cols():
    yield 56
    yield 2
    yield 1


x_product_pairs = ((i, j) for i in rows for j in cols())
