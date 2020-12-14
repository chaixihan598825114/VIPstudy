'''
name_list = ['tom','tony','tom','rose','lily']
print(name_list.index('lily',0,5))
print(name_list.count('lily'))
print(len(name_list))
name = input('输入姓名')
if (name_list.count(name) != 1):
    print(name_list.count(name))

print('lily' not in name_list)

# ----------增加元素--------------
name_list = ['Tom', 'Lily', 'Rose']
# 结尾增加元素
name_list.append('xiaoming')
print(name_list)

name_list.append(['xiaoming','xiaohong'])
print(name_list)
# 结尾作为序列增加元素
name_list.extend('xiaoming')
print(name_list)

name_list.extend(['xiaoming','xiaohong'])
print(name_list)
# insert 指定位置 插入元素
name_list.insert(1,'xiaoli')
print(name_list)

name_list.insert(0,'   ')
print(name_list)

#----------删除------------
# 删除列表

name_list = ['Tom', 'Lily','Tom','Rose']
del name_list
print(name_list)
# 删除指定位置元素
del name_list[0]
print(name_list)

# 删除指定位置元素并返回
del_name = name_list.pop(1)
print(del_name)

# 移除列表中某个数据的第一个匹配项
name_list.remove('Tom')
print(name_list)

# clear 清空列表
name_list.clear()
print(name_list)

'''
# --------修改--------
name_list = ['Tom', 'Lily', 'Rose']
name_list[0] = 'hello'
print(name_list)

# --------逆置reverse---------
num_list = [1, 5, 2, 3, 6, 8]
num_list.reverse()
print(num_list)

# --------排序sort---------
# .sort(reverse=True)---倒序，.sort(reverse=False)---正序，不填默认正序
num_list = [1, 5, 2, 3, 6, 8]
num_list.sort(reverse=True)
print(num_list)

# --------复制copy---------
name_list = ['Tom', 'Lily', 'Rose']
name_list2 = name_list.copy()
print(name_list2)

