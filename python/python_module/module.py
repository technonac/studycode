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


在Python中，一个.py文件就称之为一个模块（Module）
为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）,
可以有多级目录，组成多级层次的包结构
每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mypac
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

from mypac.web.urls import http

http("hello")
