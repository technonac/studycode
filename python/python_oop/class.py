#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
类
class ClassName(object):
    'class documentation string'
    class suite
"""


# 类的数据属性(静态成员)
class C(object):
    """class c definition"""
    foo = 100  # 类属性
    version = '1.1'

    def show_my_version(self):
        print(C.version)


C.foo = C.foo + 1
print(C.foo)


# 方法
class MyClass(object):
    def myNoActionMethod(self):
        pass


mc = MyClass()
mc.myNoActionMethod()

"""
特殊的类属性
"""
# 类的名称
print('-' * 20 + 'class name')
print(C.__name__)
# 类的文档字符串
print('-' * 20 + 'class doc')
print(C.__doc__)
# 类的属性
print('-' * 20 + 'class property')
print(C.__dict__)
# 类定义所在的模块
print('-' * 20 + 'class module')
print(C.__module__)
# 实例所对应的类 source_module.class_name
print('-' * 20 + 'class class')
print(mc.__class__)

# 包含了一个有所有父类组成的元组
print('-' * 20 + 'class bases')
print(C.__bases__)

print('-' * 20)


# 构造方法，解构方法
class C1(object):
    # 构造器
    def __init__(self):
        print('initialized')

    # 解构器
    def __del__(self):
        print('deleted')


c1 = C1()
c2 = C1()
print(id(c1), id(c2))
del c1
del c2

# 类属性
print(C.version)

# 实例属性，用实例调用创建实例属性
c = C()
c.version = 100
print(c.version)
print(C.version)

"""
静态方法/类方法
"""


class TestStaticMethod(object):
    @staticmethod
    def foo():
        print('calling static method foo()')


class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print('calling class method foo()')
        print('foo is part of class :' + cls.__name__)


tsm = TestStaticMethod()
TestStaticMethod.foo()
tsm.foo()
tcm = TestClassMethod()
TestClassMethod.foo()
tcm.foo()
