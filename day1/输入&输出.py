'''
password = input('请输入您的密码：')
print(f'您输入的密码是:{password}')
print(f'密码的数据类型是{type(password)}')
'''

# 强制类型转换

# 1. float() -- 转换成浮点型
num1 = 1
num1 = float(num1)
print(type(num1))

# 2. str() -- 转换成字符串类型
num2 = 10
num2 = str(num2)
print(type(num2))

# 3. tuple() -- 将⼀个序列转换成元组
list1 = [10, 20, 30]
print(tuple(list1))
print(type(tuple))

# 4. list() -- 将⼀个序列转换成列表
t1 = (100, 200, 300)
print(list(t1))
print(type(t1))

# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(type(eval(str1)))
print(type(eval(str2)))
print(type(eval(str3)))