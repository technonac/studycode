#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
列表
列表是能保留任意数目的python对象的灵活的容器
"""
# 列表的创建
aList = [123, 'abc', 4.56, ['inner', 'list'], 7 - 9j]
anotherList = [None, 'something to see here']
aListThatStartEmpty = []
aListUseFun = list('foo')
print(aList)
print(anotherList)
print(aListThatStartEmpty)
print(aListUseFun)

# 列表的访问
print(aList[0])
print(aList[1:4])
print(aList[:3])
print(aList[3][0])

# 列表的更新
aList[2] = 'float replacer'
print(aList)

anotherList.append(["hi i'm new here"])
print(anotherList)

# 删除列表元素或者列表本身
del aList[1]
print(aList)

aList.remove(123)
print(aList)

aList.pop()
print(aList)

del aList

# 序列类型操作符
# 切片
num_list = [43, -1.23, -2, 6.19e5]
str_list = ['jack', 'jumped', 'over', 'candlestick']
mixup_list = [4.0, [1, 'x'], 'beef', -1.9 + 6j]
num_list[1]
num_list[1:]
num_list[2:-1]
str_list[2]
mixup_list[1][1]

# 成员关系操作符
print('beef' in mixup_list)
print([1, 'x'] in mixup_list)
print('x' in mixup_list[1])

# 连接 多个列表
# 连接操作符+ 新建一张表
print(num_list + str_list)

# extend 向列表中添加新元素的操作
print(num_list.extend(str_list))

# 新增元素
num_list.append('some')

# 重复操作符
print(num_list * 2)

# 列表类型操作符和列表解析
print([i * 2 for i in [8, -2, 5]])
print([i for i in range(8) if i % 2 == 0])

# 内建函数
# 序列类型函数
print(len(num_list))

max(num_list)
min(num_list)

# reversed
s = ['They', 'stamp', 'them', "they're", 'small']
for t in reversed(s):
    print(t)

# sorted
# 字典序
print(sorted([2, 10, 1, 3, 'ab', 'abc', 'a', ]))

# enumerate
albums = ['tales', 'robot', 'pyramid']
for i, album in enumerate(albums):
    print("%d,%s" % (i, album))

# zip
fn = ['ian', 'stuart', 'david']
ln = ['bairnson', 'elliott', 'paton']
print(zip(fn, ln))

# sum
a = [6, 4, 5]
sum(a)

# list tuple
aList = ['tao', 93, 99, 'time']

aTuple = tuple(aList)
print(aTuple)
anotherList = list(aTuple)
print(aList == anotherList)
print(aList is anotherList)

# 列表对象的内建函数
"""
命令行中 dir(list) 来查看 
list.append(obj)
list.count(obj) obj出现的次数
list.extend(seq) 将seq内容添加到列表中
list.index(obj,i=0,j=len(list))
list.insert(index,obj)
list.pop(index = -1) 默认是最后一个对象
list.remove(obj)
list.reverse() 原地反转泪飙
list.sort()
"""
music_media = [45]
music_media.insert(0, 'compact disc')
music_media.append('long playing record')
music_media.insert(2, '8-track tape')
print(music_media)

'cassete' in music_media
music_media.index(45)

"""
sort(),reverse()直接作用于原对象 
sorted(),reversed()返回一个新对象
"""
music_media.sort()
print(music_media)
music_media.reverse()
print(music_media)


