# 字典 dict
phonebook = {'Alice': '1234', 'Beth': '9102'}

# 空字典
emp_dict = {}

# 键值对序列创建字典
items = [('name', 'Gumby'), ('age', 18)]
d = dict(items)
print(d)

d1 = dict(name='Abc', age=18)
print(d1)

# 字典方法
# clear
d = {}
d['name'] = 'Tom'
d['age'] = 18
print(d)
returned_value = d.clear()
print(d)

# copy 浅复制，值为原来的
sd = d.copy()

# fromkeys 从指定键创建字典，值为None
print({}.fromkeys(['name', 'age']))
# 指定默认值
print({}.fromkeys(['name', 'age'], 'default'))

# get
print(phonebook.get('Alice'))
# 指定默认值
print(phonebook.get('Bob', 'default'))

# items 返回一个包含所有字典项的列表，返回字典视图类型，可用于迭代
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
it = d.items()
print(it)
len(it)

# 字典项转为列表
print(list(d.items()))

# keys 返回字典中的键的字典视图
print(d.keys())

# pop 获取指定键相关的值，并把键值对从字典中删除
d = {'x': 1, 'y': 2}
d.pop('x')
print(d)

# update 使用一个字典中项来更新另一个字典
old = {'x': 1, 'y': 2}
new = {'x': 100, 'y': 200}
old.update(new)
print(old)

# values 返回字典中的值组成的字典视图,会有重复
d = {1: 1, 2: 2, 3: 3, 4: 1}
print(d.values())
