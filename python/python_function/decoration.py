#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
函数与方法装饰器
装饰器背后主要动机源自python面向对象编程,装饰器是在函数调用之上的修饰
装饰器的语法以@开头，接着是装饰器函数的名称和可选的参数，紧跟着装饰器声明的是被修饰的函数和装饰函数的可选参数
@decorator
def function2Bdecorated(func_opt_args):
    ...
多个装饰器
@deco2
@deco1
def func(arg1,arg2,...):pass

等价于
def func(arg1,arg2,...):pass
func = deco2(deco1(func))

有参书装饰器
@decomarker(deco_args)
def foo():pass
等价与
foo = decomarker(foo)

装饰器仅仅是用来装饰函数的包装，返回一个修改后的函数对象，将其重新赋值原来的标识符，并永久失去对原始函数对象的方法
"""
from time import ctime, sleep


def tsfunc(func):
    def wrappedFunc():
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func()

    return wrappedFunc


@tsfunc
def foo():
    pass


foo()
