'''
# 可变类型：
    # 列表
    # 字典
    # 集合

# 不可变类型：
    # 整型
    # 浮点型
    # 字符串
    # 元组

# python中，值是靠引用来传递的
# 我们可以⽤id()来判断两个变量是否为同⼀个值的引⽤。 我们可以将id值理解为那块内存的地址标识。

# 1. int类型
a = 1
b = a
print(b) # 1
print(id(a)) # 140708464157520
print(id(b)) # 140708464157520
a = 2
print(b) # 1,说明int类型为不可变类
print(id(a)) # 140708464157552，此时得到是的数据2的内存地址
print(id(b)) # 140708464157520

# 2. 列表
aa = [10, 20]
bb = aa
print(id(aa)) # 2325297783432
print(id(bb)) # 2325297783432
aa.append(30)
print(bb) # [10, 20, 30], 列表为可变类型
print(id(aa)) # 2325297783432
print(id(bb)) # 2325297783432

# 例题
def test1(a):
    print(a)
    print(id(a))

    a += a

    print(a)
    print(id(a))

# int:计算前后id不同，int为不可变数据类型
b = 100
test1(b)
# list列表：计算前后id相同，列表为可变数据类型
c = [11,22]
test1(c)
'''

