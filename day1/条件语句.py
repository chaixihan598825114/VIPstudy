# a = 1
#
# if a < 0:
#     print('对')
#
# print('不管是否成立都打印一下')
'''
age = int(input('请输出您的年龄：'))
if age >= 18:
    print(f'您的年龄是{age},已经成年，可以上网')
else:
    print(f'您的年龄是{age},未成年，不允许上网')
print('再见')
'''

age = int(input('请输入您的年龄：'))
if age < 18:
    print(f'您的年龄为{age}太小不合法')
elif 18 <= age and age <= 60:
    print(f'您的年龄为{age}合法')
else:
    print(f'您的年龄为{age}岁数太大了')