#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
集合类型
集合对象是一组无序排列的可哈希的值

"""
# 创建集合
s = set('cheeseshop')  # 可变集合
t = frozenset('bookshop')  # 不可变集合
print(s)
print(t)
print(type(s))
print(type(t))
print(len(s))

# 访问集合中的尘缘
print('s' in s)
for i in s:
    # print(i)
    pass

# 更新集合
s.add('z')
print(s)

s.update('pypi')
print(s)

s.remove('z')
print(s)

s -= set('pypi')
print(s)

# 删除集合
# del s

# 集合类型操作符
# in not in
print('k' in s)

print(set('posh') == set('shop'))

# 子集< <= 和超集 > >=
print(set('shop') < set('cheeseshop'))

# union 并集
print(s | t)

# and 交集
print(s & t)

# 差补/相对补集(-)
print(s - t)  # 只属于集合s，而不属于集合t

# 相对差分 异或 只能属于集合s或者集合t，不能同时属于
print(s ^ t)

# 内建函数
set([])
frozenset([])

# 内建方法
# 所有集合可用
s.issubset(t)
s.issuperset(t)
s.union(t)  # 并集
s.intersection(t)  # 交集
s.difference(t)  # 返回一个新集合，该集合是s的成员，但不是t成员
s.symmetric_difference(t)  # 异或
s.copy()  # 返回一个新集合，它是集合s的浅复制

# 适用于可变集合
s.update(t)
s.intersection_update(t)
s.difference_update(t)
s.add('')
s.remove('')
