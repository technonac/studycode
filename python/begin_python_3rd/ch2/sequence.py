# 索引 index
# python没有字符类型，一个字符表示只包含一个元素的字符串
greeting = 'Hello'
print(greeting[0])

# 最后一个元素
print(greeting[-1])

# 直接对字符串操作
print('Hello'[1])

# 切片 slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 包含开始索引，不包含结尾索引
print(numbers[3:6])

print(numbers[3:])

print(numbers[:3])

# 指定步长
print(numbers[0:10:2])

print(numbers[::4])

# 步长为负数
print(numbers[::-2])

# 序列相加
print([1, 2, 3] + [4, 5, 6])
print('hello' + ' world')

# 乘法
print('python' * 5)
print([42] * 5)

# 空列表
emp_list = []

# 包含10个元素的列表
seq10 = [None] * 10
print(seq10)

# 成员运算符 in
permissions = 'rw'
print('w' in permissions)

# 内置函数
len(numbers)
max(numbers)
min(numbers)

