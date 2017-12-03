# -*- coding: utf-8 -*-

# 程序输出
print('===== input =====')

print 'Hello World!'  # print statement
print("%s number is %d" % ("Python", 1))  # print function
logfile = open('log.txt', 'a')
# print >> logfile, 'Fatal:error:invalid input'
logfile.close()

# 程序输入
print('===== output =====')


# user = raw_input("Enter your name: ")

# 注释
# 文档字符串,模块，类或者函数


def foo():
    """This is a doc string."""
    return True


# 操作符 / 传统除法 ,//浮点除法,**乘方,与 and 或 or 非 not
print('===== operator =====')

print(1 // 2)
print(3 ** 2)
print(2 < 4)
print(2 > 3 and (2 != 4 or 2 == 2))

# 变量 大小写敏感
print('===== var =====')

miles = 1000.0
kilometers = 1.609 * miles
print('%f miles is the same as %f km' % (miles, kilometers))

# 字符串 +:连接字符串 *:字符串重复
print('===== string =====')
pystr = 'Python'
iscool = 'is cool!'
print(pystr[0])
print(pystr[2:5])
print(iscool[:2])
print(iscool[3:])
print(iscool[-1])  # 最后一个字符索引为-1
print(pystr + ' ' + iscool)
print('''python
is cool''')
print('-' * 20)

# 列表和元组(只读列表)  任意数量，任意类型的python对象
print('===== list and tuple =====')
aList = [1, 2, 3, 4]
print(aList)
print(aList[0])
print(aList[2:])
aList[1] = 5
print(aList)

aTuple = ('robots', 77, 93, 'try')
print(aTuple)
print(aTuple[:3])

# 字典
print('===== dict =====')
aDict = {'host': 'earth'}
print(aDict)
aDict['port'] = 80  # add to dict
print(aDict)
print(aDict.keys())
print(aDict['host'])
for key in aDict:
    print("%s -> %s" % (key, aDict[key]))

# if语句
print('===== if =====')
if 1 > 2:
    pass
else:
    pass
# if elif
if 1 > 2:
    pass
elif 1 > 3:
    pass
else:
    pass

# while循环
print('===== while =====')
counter = 0
while counter < 3:
    print("loop #%d" % counter)
    counter += 1

print('===== for =====')
for item in ['e-mail', 'net', 'homework', 'chat']:
    print item,  # 带都好的print语句输出的元素之间会自动添加一个空格

print
print 'hello', 'world'

for eachNum in range(3):
    print(eachNum)
lestr = 'abc'
for letter in lestr:
    print(letter)

for i, ch in enumerate(lestr):
    print('%c(%d)' % (ch, i))

# 列表解析
print('===== list parse =====')

squared = [x ** 2 for x in range(4)]
print(squared)

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
print(sqdEvens)

# 错误和异常
print('===== error and exception =====')
try:
    pass
except IOError, e:
    print(e)

# 函数 通过引用调用的
print('===== function =====')


def addMe2Me(x):
    """apply + operation to argument"""
    return x + x


print(addMe2Me(2))
print(addMe2Me([-1, 'abc']))


def f(debug=True):
    if debug:
        print('in debug mode')
    else:
        print('done')


f()

# 类
print('===== class =====')


# self是类实例自身的引用，其他面向对象语言用this
class FooClass(object):
    """
    optional documentation string
    """
    # static member declaration
    version = 0.1  # class attribute

    # method declaration
    def __init__(self, nm='John Doe'):
        """constructor"""
        self.name = nm  # class instance (data)attribute 类实例的属性
        print('created a class instance for', nm)

    def showname(self):
        """display instance attribute and class name"""
        print("your name is %s" % self.name)
        print('my name is', self.__class__.__name__)

    def showver(self):
        """display class(static) attribute"""
        print(self.version)  # reference to FooClass.version

    def addMe2Me(self, x):
        return x + x


foo1 = FooClass()
foo1.showname()
foo1.showver()

# 模块
"""
import module_name
module.function
module.name
"""
print('===== module =====')
import sys

sys.stdout.write(sys.version)
sys.stdout.write('\n')
sys.stdout.write(sys.platform)
