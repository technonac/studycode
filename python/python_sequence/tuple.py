#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
元组
元组是一种不可变的类型
默认集合类型
所有的多对象的，逗号分隔的，没有明确用符号定义的，这些集合默认的类型都是元组
"""
# 创建元组
aTuple = (123, 'abc', 4.56, ['inner', 'tuple'], 7 - 9j)
anotherTuple = (None, 'something to see here')
# 只有一个元素的元组需要在后面加上逗号
emptiestPossibleTuple = (None,)
tupleUseFun = tuple('bar')

print(aTuple)
print(anotherTuple)
print(emptiestPossibleTuple)
print(tupleUseFun)

# 访问元组的值
aTuple[1:4]
aTuple[:3]
aTuple[3][1]

# 如何更新元组,不能更新 或者改变元组的元住宿，需要新建元组
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
print(tup1 + tup2)

# 删除元组的元素或者元组本身，bune不能删除一个单独的元组元素
del aTuple

# 元组操作符和内建函数

# 重复
t = (['xyz', 123], 23, -103.4)
print(t * 2)

# 连接
print(t + ('free', 'easy'))

# 成员关系操作，切片操作
print(23 in t)
print(t[0][1])
print(t[1:])

# 内建函数
print(str(t))
print(max(t))
print(min(t))
print(cmp(t, ()))
print(list(t))

# 操作符
print((2, 3) == (2, 3))


# 所有函数返回的多对象(不包括有符号封装的)都是元组类型

def foo1():
    return 1, 2, 3


def foo2():
    return [1, 2, 3]


def foo3():
    return (1, 2, 3)


print(type(foo1()))

