#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Formal Arguments 形参

"""


# 位置参数 必须以在函数中定义的准确顺序来传递
def foo(who):
    pass


foo('')


# 默认参数 如果在函数调用时没有为参数提供值则使用预先定义的默认值
# 所有位置参数必须出现在默认参数钱

def taxMe(cost, rate=0.0825):
    return cost + (cost * rate)


print(taxMe(100))
print(taxMe(cost=100, rate=0.05))

print('-' * 20)
"""
可变长的参数
"""

"""
非关键字可变长参数(元组)
可变长参数元组必须在位置和默认参数之后
def function_name([formal_args, ] *vargs_tuple):
    function_body_suite

星号操作符之后的形参将作为元组传递给 函数，
通过末尾增加一个可变的参数列表变量，我们就能处理超出数目的参数被传入函数的情形
"""


def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    """display regular args and non-keyword variable args"""
    print('formal1 arg1:', arg1)
    print('formal1 arg2:', arg2)
    for eachXtArg in theRest:
        print("another arg: ", eachXtArg)


tupleVarArgs('abc')
print('-' * 20)
tupleVarArgs('abc', 123)
print('-' * 20)
tupleVarArgs('abc', 123, 'xyz', 456.789)
print('-' * 20)

"""
关键字变量参数(字典)
字典中的键作为参数名，值作为相应的参数值
def function_name([formal_args ,][*vargst,] **vargsd):
    function_body_suite
关键字变量参数应该为函数定义的最后一个参数
"""


def dictVarArgs(arg1, arg2='defaltB', **theRest):
    print('formal1 arg1:', arg1)
    print('formal1 arg2:', arg2)
    for eachXtArg in theRest.keys():
        print("Xtra arg %s: %s " % (eachXtArg, theRest[eachXtArg]))


dictVarArgs(arg1=123, arg2='tales', c=123, d='poe')
print('-' * 20)


# 混合
def newfoo(arg1, arg2, *nkw, **kw):
    print('arg1:', arg1)
    print('arg2:', arg2)
    for eachNKW in nkw:
        print("additional non-keyword arg:", eachNKW)
    for eachKW in kw.keys():
        print("additional keyword arg %s : %s" % (eachKW, kw[eachKW]))


newfoo('wolf', 3, 'project', freid=90, gamble=96)
print('-' * 20)
aTuple = (6, 7, 8)
aDict = {'z': 9}
newfoo(1, 2, 3, x=4, y=5, *aTuple, **aDict)
print('-' * 20)
