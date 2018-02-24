# 列表 list

# list函数, 将序列转为列表
list_from_string = list('hello')
print(list_from_string)

# 将字符列表转换为字符串
string_from_list = ''.join(list_from_string)
print(string_from_list)

# 列表基本操作

# 修改列表
x = [1, 1, 1]
x[1] = 2
print(x)

# 删除元素 del语句
names = ['A', 'B', 'C', 'D', 'E']
del names[2]
print(names)

# 给切片赋值
name = list('Perl')
print(name)
name[1:] = list('ython')
print(name)

# 插入元素
numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print(numbers)

# 清除元素
# del numbers[1:4]
numbers[1:4] = []
print(numbers)

# 列表方法
# append
lst = [1, 2, 3]
lst.append(4)
print(lst)

# clear
lst.clear()
print(lst)

# copy

# 索引指到同一个列表
a = [1, 2, 3]
b = a
b[1] = 4
print(b)

# 复制列表
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)

# count 计算指定的元素在列表中出现的次数
print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))

# extend 将多个值附加到列表末尾

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)

# index
knights = ['we', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index('who'))

# insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
# numbers[3:3] = ['four']
print(numbers)

# pop 删除末尾最后一个元素
x = [1, 2, 3]
x.pop()
print(x)

# remove 删除第一个指定的元素
x = ['to', 'be', 'or', 'not', 'to', 'be']
x.remove('be')
print(x)

# reverse
x = [1, 2, 3]
x.reverse()
print(x)

# sort 会对原来的列表进行修改
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)

# 获取排序后的列表的副本
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print(x)
print(y)

# 高级排序
x = ['xxxx', 'xx', 'xxx', 'x']
# key指定用于排序的函数
x.sort(key=len)
print(x)

# reverse 指定是否按相反的顺序排序
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)
