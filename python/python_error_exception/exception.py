#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
错误与异常

try:
    try_suite
except Exception[,reason]:
    except_suite
except (Ex1,Ex2,...)[,reason]:
    suite for multi


else子句
在try范围中没有异常被检测到是，执行else子句
在else范围中的任何代码运行前，try范围中的所有代码必须完全才成功

finally 子句
无论异常是否发生，是否捕捉都会执行的一段代码
try:
    try suite
except Exception:
    suite for exception
else:
    no exceptions detected suite
finally:
    always execute suite

"""

try:
    f = open('blah', 'r')
except IOError, e:
    print("could not open file: ", e)


def safe_float(obj):
    try:
        retval = float(obj)
    except ValueError:
        retval = 'could not convert non-number to float'
    except TypeError:
        retval = 'obejct type cannot be converted to float'
    return retval


# 多个异常合并
def safe_float1(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError), diag:
        retval = str(diag)
    return retval


# 捕获所有的异常
try:
    pass
except BaseException, e:
    pass

# else子句
try:
    f = open('.gitignore', 'r')
    f.close()
except IOError:
    pass
else:
    print('*** no exceptions caught')

"""
上下文管理
with语句的目的在于从流程图中把try，except，finally关键字和资源分配释放的相关代码统统去掉

with context_expr [as var]:
    with suite

它仅能在工作与支持上下文管理协议(context management protocol)的对象
file
decimal.Context

"""

# with open('text', 'w') as f:
#    for eachLine in f:
#        pass

"""
触发异常

raise [SomeException [,args [,traceback]]]
SomeException: 触发异常的名称 
args:异常的参数总是最为一个元组传入(msg,code) 大多数情况下，单一的字符串用来指示错误的原因，如果传的是元组，
通常的组成是一个错误字符串，一个错误编号
traceback:可选
"""
a = False
if a == True:
    raise IOError, "!!!! custom msg !!!!"

"""
断言
断言是一句必须等价于布尔真的判定
如果断言失败，触发AssertError异常 
assert expression [, arguments]
"""
assert 1 == 1
