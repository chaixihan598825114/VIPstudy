print('hello word')
# 赋值
my_name = 'Tom'
print(my_name)

schoolName = '超哥测试提升'
print(schoolName)

'''
# 数据类型
a = 1
print(type(a))

b = 1.1
print(type(b))

c = True
print(type(c))

d = '12345'
print(type(d))

e = [10, 20, 30]
print(type(e))

f = (10, 20, 30)
print(type(f))

h = {10, 20, 30}
print(type(h))

g = {'name': 'Tom', 'age': 20}
print(type(g))
'''

# 输出&格式化输出
'''
%s = 字符串
%d = 有符号的十进制整数
%f = 浮点
'''

age = 18
name = 'TOM'
weight = 75.5
student_id = 1

# 我的名字是TOM
print('我的名字是%s' % name)

# 我的学号是0001
print('我的学号是%04d号' % student_id)

# 我的体重是75.50公⽄
print('我的体重是%.2f公斤' % weight)

# 我的名字是TOM，今年18岁了了
print('我的名字是%s，我今年%d岁了' % (name,age))

# 我的名字是TOM，明年19岁了了
print('我的名字是%s，明年%d岁了' % (name, age + 1))

# 我的名字是TOM，明年年19岁了了
print(f'我的名字是{name}, 明年{age + 1}岁了')


# 结束符
# \n:换行
# \t:制表符
print('输出的内容',end="\n")
