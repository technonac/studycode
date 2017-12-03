#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
模块

导入模块
import module1[,module2][,module3]

from module import name1[,name2]

from module import name as alias

加载模块会导致这个模块被执行，也就是被导入模块的顶层代码将直接被执行
一个模块只会被加载一次，无论它被导入多少次
globals()返回调用者和全局名称空间的字典
locals()返回调用者局部名称空间的字典


reload()内建函数可以重新导入一个已经导入的模块
reload(sys)

"""


def foo():
    print('calling foo...')
    aString = 'bar'
    anInt = 42
    print('foo() globals: ', globals().keys())
    print('foo() locals: ', locals().keys())


print('__main__ globals: ', globals().keys())
print('__main__ locals: ', locals().keys())

foo()

"""
包
from package.module import *

"""
