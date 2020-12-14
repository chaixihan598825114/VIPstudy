'''
# 创建字典 用大括号
dict1 = {'name':'Tom','age':'20','gender':'男'}
# 空字典
dict2 = {}
dict3 = dict()

# 增加&修改，如果有就是修改，如果没有就是增加
dict1 = {'name':'Tom','age':'20','gender':'男'}
dict1['name'] = 'Rose'
print(dict1)

# 删除 del() 或 del ：删除字典或删除字典中指定键值对
dict1 = {'name':'Tom','age':'20','gender':'男'}
del dict1['gender']
print(dict1)

# 清空 clear
dict1 = {'name':'Tom','age':'20','gender':'男'}
dict1.clear()
print(dict1)

# 查找 没有的会报错
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name'])
print(dict1['id'])

# get方法  .get(key,默认值)  找不到key时，会返回默认值
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name'))
print(dict1.get('id',110))
print(dict1.get('id'))


# keys&values  或者字典的key和values
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.keys())
print(dict1.values())

# items 获取字典的每一组key和values
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.items())

'''
