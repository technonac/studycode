#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python对象
python是面向对象编程语言
python使用对象模型来存储数据，构造的任何类型的值都是一个对象
所有python对象都有三个特性：
身份:每个对象都有一个唯一的身份标识自己，任何对象的身份可以使用内建函数id()来得到，这个时执可以被认为是该对象的内存地址
类型：使用内建函数type()来查看python对象的类型
值:对象表示的数据项
"""
# 所有的类型对象的类型都是type，即类型也是对象
import types

print(type(42))
print(type(type(42)))

# Null对象 None
print(type(None))

# 标准类型操作符
# 对象值比较(数字类型根据数值的大小和符号比较，字符串按照字符序列进行比较)
'abc' < 'xyz'
# 对象身份比较
a = [5, 'hat', -9.3]
b = a
print(a is b)
print(a is not b)
print(id(a) == id(b))

# 标准类型 内建函数
# type() 得到对象的类型，并返回相应的type对象
type(object)

# cmp()用于比较两个对象obj1,obj2,如果是用户自定义对象 ，cmp()会调用该类的特殊方法__cmp__()
a, b = -1, 12
print(cmp(a, b))
a, b = 'abc', 'xyz'
print(cmp(a, b))

# str() 返回对象时刻可读性好的字符串表示
str([0, 5, 9, 9])
# repr() 返回一个对象的字符串表示
repr([0, 5, 9, 9])


class Foo:
    pass


class Bar(object):
    pass


foo = Foo()
bar = Bar()

print(type(foo))
print(type(Foo))
print(isinstance(foo, Foo))
print(isinstance('str', types.StringType))
