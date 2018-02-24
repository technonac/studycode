# 字符串不可变，不能进行切片赋值

# 字符串格式化
fm = "Hello, %s. %s enough for ya"
val = ('world', 'Hot')
print(fm % val)

# 左边指定格式字符串 % 右边指定值
print('Hello %s' % ('World'))

# format方法
print("{},{},and {}".format('first', 'second', 'third'))

print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))

print("{name} is {years} years old.".format(name='Tom', years=18))

# 冒号后面加上格式说明
print('The number is {num:f}'.format(num=42))

# 字符串方法

# center
print('I am centered'.center(40, '*'))

# find 查找子串
print('Hello Python Language'.find('Python'))

# join 合并序列元素
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

# lower
print("LOWER".lower())

# replace
print('This is a test'.replace('is', 'ezz'))

# split 将字符串拆分为序列
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))

# strip 删除字符串开通和末尾的空白
print('       whitespace     '.strip())
