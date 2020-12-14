'''
def sum_num(a,b,f):
    return f(a)+f(b)

result = sum_num(-1,2,abs)
print(result)



def sum_num1(c,d,e):
    return e(c)+e(d)

result1 = sum_num1(-1.3,4.2,round)
print(result1)

# map(func, lst)，将传⼊的函数变量func作⽤到lst变量的每个元素中，并将结果组成新的列表返回
list1 = [1,2,3,4,5,6,7,8]
def func(x):
    return x ** 2
result = map(func,list1)
print(result)
print(list(result))

# reduce(func，lst)，其中func必须有两个参数。每次func计算的结果继续和序列的下⼀个元素做累积计算

import functools
list2 = [1,2,3,4,5,6,7,8,9]
def func1(a,b):
    return a + b
result = functools.reduce(func1,list2)
print(result)
'''

# filter(func, lst)函数⽤于过滤序列, 过滤掉不符合条件的元素, 返回⼀个 filter 对象。如果要转换为列表,可以使⽤ list() 来转换
list1 = [1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x ** 2
result = map(func,list1)
print(result)
print(list(result))