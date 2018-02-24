# 判断某个对象是否可以调用，内置函数callable
print(callable(max))


# 定义函数
def hello(name):
    """say hello to name"""
    return 'Hello, ' + name + '!'


print(hello('world'))
print(hello.__doc__)
