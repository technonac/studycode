# 序列解包
x, y, z = 1, 2, 3
print(x, y, z)

# 交换值
x, y = y, x
print(x, y, z)

# 星号运算符收集多余的值
a, b, *rest = [1, 2, 3, 4]
print(rest)

# 链式赋值
a = b = 1
print(a, b)

# 布尔
val = bool([])

# if else语句
if val:
    print('yes')
else:
    print('no')

# 运算符

# 是否同一个对象
print(a is b)

print(a is not b)

# 遍历
numbers = [0, 1, 2, 3]

for num in numbers:
    print(num)
print()

# 迭代字典
d = {'x': 1, 'y': 2, 'z': 3}
# 遍历方法1
for key in d:
    print(key, '=', d[key])
print()

# 遍历方法2
for key, value in d.items():
    print(key, '=', value)
print()

# 并行迭代 zip
names = ['anne', 'beth', 'george']
ages = [12, 45, 32]
res = list(zip(names, ages))
print(res)

for name, age in zip(names, ages):
    print(name, 'is', age, 'years old.')

# 迭代时获取索引 enumerate
strings = 'hello'
for index, string in enumerate(strings):
    print(index, 'is', string)

# 反向迭代
lst = [4, 3, 6, 8, 3]
sorted(lst)

# 排序后迭代
reversed(lst)

# pass语句，什么都不做
pass

# del 删除对象
x = 1
del x

# exec 将字符串作为代码执行
# 主要用于动态创建代码字符串
exec("print('hello')")

# eval 计算用字符串表示的python表达式的值，并返回结果
scope = {'x': 2, 'y': 3}
ret = eval('x*y', scope)
print(ret)
