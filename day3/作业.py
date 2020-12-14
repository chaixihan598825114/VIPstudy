'''
# 九九乘法表
n = 1
while n < 10:
    m = 1
    while m <= n:
        print(f'{m}*{n}={n*m}',end=',')
        m += 1
    print()
    n+=1
---------------------------------------------------------------
# 质数判断
---------------------------------------------------------------
---------------------------------------------------------------
---------------------------------------------------------------
# 7行菱形

def diamond():
    e = 0
    f = 4
    while e < 4:
        e += 1
        f -= 1
        print(f * ' ' + (2 * e - 1) * '*')
    while 0 < e <= 4:
        e -= 1
        f += 1
        print(f * ' ' + (2 * e - 1) * '*')
diamond()
---------------------------------------------------------------
# 100以内被5整除的质数

list1 = []
list2 = []
i = 0
n = 2
m = 1
# 100以内被5整除列表
while i < 100:
    if i % 5 == 0:
        list1.append(i)
    i += 1
# 遍历列表得到质数
while m < len(list1):
    while n < list1[m]:
        if list1[m] % n == 0:
            break
        n += 1
        else:
            list2.append(list1[m])
    m += 1
print(list1)
print(f'100以内能被5整除的质数为{list2}')
---------------------------------------------------------------
# 有两个列表，一个是学生姓名，一个是学生的年龄，生成一个字典，key为姓名，value为年龄

list1 = ['xiaozhang', 'xiaoming', 'xiaoli', 'xiaowang']
list2 = ['18', '20', '25', '30']
dict1 =dict(map(lambda x,y:[x,y],list1,list2))
print(dict1)

---------------------------------------------------------------
# 注册
list1 = [{'name':'zhang','age':20},'chai','laowang']
def function1(name):
    global list1
    if list1.count(name) < 1:
        list1.append(name)
        print('注册成功')
    else:
         print('注册姓名重复了')
name = input('请输入注册姓名：')
print(function1(name))

'''
str1 = 'abcdef'
print(str1)
# list1 = list(str1)
print(str1[::-1])