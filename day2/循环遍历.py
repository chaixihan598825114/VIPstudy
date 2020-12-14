'''
name_list = ['Tom', 'Lily', 'Rose']
# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1

for i in name_list:
    print(i)
'''
# 循环遍历字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
# 遍历字典里的key
for key in dict1.keys():
    print(key)
# 遍历字典里的value
for value in dict1.values():
    print(value)
# 遍历字典里的元素
for items in dict1.items():
    print(items)
# 遍历字典里的键对值
for key,value in dict1.items():
    print(f'{key}={value}')
