#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
映射类型:字典
字典是python语言中唯一的映射类型，映射类型对象里哈希值(键，key)和指向的对象(值，value)是一对多的关系
一个字典对象是可变的，它是一个容器类型，数据是无序的
字典中的键必须是可以哈希的，所以数字和字符串可以作为字典的键，但是列表和其他字典不行
"""
# 创建字典
dict1 = {}
dict2 = {'name': 'earth', 'port': 80}
fdict = dict((['x', 1], ['y', 2]))
ddict = {}.fromkeys(('x', 'y'), -1)
edict = {}.fromkeys(('foo', 'bar'))

print(dict1)
print(dict2)
print(fdict)
print(ddict)
print(edict)

# 访问字典
for key in dict2.keys():
    print("%s = %s" % (key, dict2[key]))

print(dict2['name'])
print(dict2.has_key('name'))
print('name' in dict2)
dict2.get('name')

# 更新字典
dict2['name'] = 'venus'
dict2['port'] = 1234
dict2['arch'] = 'sunos5'
print(dict2)

# 删除字典元素和字典
del dict2['arch']
# 清除字典所有条目
# dict2.clear()
# del dict2
# dict2.pop('name')


# 映射类型操作符
dict2['name']
'name' in dict2

# 内建函数
print(type(dict2))

print(str(dict2))

# 映射类型相关的函数

# dict
# 如果参数是可迭代的，即一个序列，或是一个迭代器，或是支持迭代的对象，那每个可迭代的元素必须成对出现
print(dict(zip(('x', 'y'), (1, 2))))

print(dict([['x', 1], ['y', 2]]))

print(dict(x=1, y=2))

# len 返回键值对数目
print(len(dict2))

# hash
print(hash('hash_value'))

# 内建方法
print(dict2.keys())

print(dict2.values())

# item 返回一个包含所有(键，值)元组的列表
print(dict2.items())

# sorted内建函数,它返回一个有序的迭代子

for eachKey in sorted(dict2):
    print('%s=%s' % (eachKey, dict2[eachKey]))

# update 将一个字典的内容添加到另外一个字典中
dict2 = {'host': 'earth', 'port': 80}
dict3 = {'host': 'venus', 'port': 1234}
dict2.update(dict3)
print(dict2)
dict3.clear()
print(dict3)

