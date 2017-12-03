#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
子类和派生

class SubClass(ParentClass1[,ParentClass2],...)
    class suite
"""


class Parent(object):
    def __init__(self):
        print('created an instance of ' + self.__class__.__name__)

    def parent_method(self):
        print('calling parent method')

    def foo(self):
        print('hi,i am p-foo')


class Child(Parent):
    def child_method(self):
        print('calling child method')

    def foo(self):
        """覆盖父类的方法"""
        # 方法1：Parent.foo(self) #调用父类的方法
        # 方法2：super()内建方法，不但能找到基类方法，而且还为我们传进self
        super(Child, self).foo()  # 推荐使用，修改继承关系时不需要修改
        print('hi,i am c-foo')


c = Child()
c.parent_method()
c.child_method()
# 对于任何类，他是一个包含其父类的集合的元组
print(Child.__bases__)

c.foo()

"""
从标准类型派生
"""


# 不可变类型的例子
# 所有的__new__方法都是类方法,该方法必须返回一个合法的实例
class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))


print(RoundFloat(1.5955))


# 可变类型的例子
class SortedKeyDict(dict):
    def keys(self):
        return sorted(super(SortedKeyDict, self).keys())


d = SortedKeyDict((('xyz', 123), ('def', 789), ('abc', 456)))

print(d.keys())

"""
多重继承 
"""


class P1(object):  # 父类1
    def foo(self):
        print('P1-foo')


class P2(object):  # 父类2
    def foo(self):
        print('P2-foo')

        def bar(self):
            print('P2-bar')


class C1(P1, P2):  # 子类1
    pass


class C2(P1, P2):  # 子类2
    def bar(self):
        print('C2-bar')


class GC(C1, C2):  # 子孙类
    pass


gc = GC()
# 查找的顺序 GC - C1 - C2 - P1
gc.foo()

# 查找顺序 GC- C1 - C2
gc.bar()

# mro(method resolution order)属性，查找顺序
print(GC.__mro__)

"""
类，实例和其他对象的内建函数
hasattr()
getattr()
setattr()
delattr()
dir()列出一个模块所有的属性信息
"""
# 判断是否子类或子孙类
print(issubclass(GC, P1))
# 判断是否类的实例
print(isinstance(gc, P1))


class MyClass(object):
    def __init__(self):
        self.foo = 100


myInst = MyClass()
print(hasattr(myInst, 'foo'))
setattr(myInst, 'foo', 101)
print(getattr(myInst, 'foo', 'default value'))
# delattr(myInst, 'foo')
# 显示属性
print(dir(myInst))
# 查找父类
print(super(MyClass))

# 与__dict__类似
print(vars(myInst))
