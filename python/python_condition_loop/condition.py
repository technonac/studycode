#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
条件与循环
"""
a = 1
b = 2

# if语句
if a == 1 and b == 2:
    pass
else:
    pass

# if else
if a == 1:
    pass
elif a == 2:
    pass
else:
    pass

# 条件表达式 C?X:Y
# X if C else Y
x, y = 4, 3

smaller = x if x < y else y
print(smaller)

# while
count = 0
while count < 3:
    count = count + 1

# for
for eachLetter in 'name':
    print(eachLetter)
nameList = ['Donn', 'Shirley', 'Ben', 'Janice']
for i, eachLee in enumerate(nameList):
    print("%d %s" % (i, eachLee))

# range内建函数
print(range(2, 19, 3))

# xrange内建函数，当有一个和很大范围的列表时更为合适，因为它不会在内存整理创建列表的完整拷贝
xrange(0, 10, 1)

# 内建函数
albums = ('Poe', 'Gaudi', 'Freud', 'Poe2')
years = (1976, 1987, 1990, 2003)
print('-' * 20 + "sorted")
for album in sorted(albums):
    print(album)

print('-' * 20 + "reversed")
for album in reversed(albums):
    print(album)

print('-' * 20 + "enumerate")
for i, album in enumerate(albums):
    print(i, album)

print('-' * 20 + "zip")
for i, album in zip(albums, years):
    print(i, album)


# pass语句 no operation
def foo_func():
    pass

