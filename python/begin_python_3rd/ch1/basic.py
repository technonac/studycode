#!/usr/bin/env python

# python3中为函数
print("Hello World!")

# 获取用户输入
# name = input("what's your name : ")
# print("welcome ", name)

# 字符串
test = 'Hello\nWorld'
print(repr(test))
print(str(test))

# python3中所有的字符串都是unicode字符串

# 长字符串 三引号

print(''' hey i am 
long string
''')
# 原始字符串
print('c:\\temp')

# 不转义,加上前缀r
print(r'c:\temp')

# 打印多个表达式，使用逗号分隔
print('age', 42)

# 添加自定义分隔符
print('i', 'am', 'happy', sep='_')

# 自定义结束字符串
print('Hello,', end='')
print('World')

