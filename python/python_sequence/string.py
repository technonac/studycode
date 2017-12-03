#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
字符串
python中单引号和双引号的作用是相同的
通常意义的字符串(str)和unicode字符串实际上都是抽象类basestring的子类

索引
  0  1  2  3
  a  b  c  d
 -4 -3 -2 -1
 索引值不包括end在内的字符串
 start<=x < end
"""

aString = 'abcd'
len(aString)
# 切片操作
print(aString[0])
print(aString[-3:-1])
print(aString[1:])
print(aString[-1])
print(aString[:])

# 成员操作
print('bc' in aString)

# 连接
print('ab' + 'cd')
print('%s %s' % ('hello', 'world'))
print(''.join(('a', 'b')))
print('upcase'.upper())
# 编译时字符串连接
foo = 'hello''word'
print(foo)

print('-' * 20, 'hello world', '-' * 20)

# 原始字符串操作符,所有字符都是自己解按照字面的意思来的，没有转义特殊或者不能打印的字符,用在正则等
s = r'\n'
path = r'c:\windows\temp\readme.txt'  # \t \r都不会被转义
print(s)
print(path)

# unicode字符串操作符
s = u'\u0061\u0062\u0063'
print(s)

# 内建函数
str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'

print(cmp(str1, str2))
len(str1)
# 按照ascii值来排序
print(max(str1))
print(min(str1))

s = 'foobar'
for i, t in enumerate(s):
    print(i, t)

s, t = 'foa', 'obr'
print(zip(s, t))

print(isinstance(u'\0xab', str))
print(isinstance('foo', unicode))
print(isinstance(u'', basestring))
print(isinstance('foo', basestring))
chr(65)
ord('a')

# 字符串类型的内建方法
s = 'test'
print(s.capitalize())  # 字符串的第一个字母大写
print(s.center(10))
print(s.count('t'))  # 返回str在字符串中出现的次数
s.decode('utf-8')
s.encode('utf-8')
s.endswith('t')
s.find('t')
s.index('t')
print(s.isdigit())
print(s.isalpha())
s.isupper()
s.join('')
s.replace('', '')
s.rfind('')
s.rindex('')
s.lstrip()  # 去掉左边的空格
s.rstrip()  # 去掉右边的空格
s.strip()
s.upper()
s.lower()
print(':'.join(s.split()))

# 三引号 可以包含诸如回车，tab键等特殊字符
hi = '''hi
there'''

"""
相关模块
string
re
base64
crypt
hashlib
hma
sha
"""
