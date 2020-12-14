'''
# 函数
def fn1():
    return 200

print(fn1)
print(fn1())

# lambda
fn2 = lambda: 100
print(fn2)
print(fn2())

def add(a,b):
    return a+b

res = add(1,2)
print(res)

add1 = lambda a,b:a+b
print(add1(1,2))
'''
# 带判断的lambda
fn1 = lambda a,b:a if a > b else b
print(fn1(1000,500))

# 列表数据按字典key的值排序
students = [
    {'name': 'TOM', 'age': 20},
    {'name': 'ROSE', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
# 按name值升序排列
students.sort(key=lambda x:x['name'])
print(students)
# 按name值降序排列
students.sort(key=lambda x:x['name'],reverse = True)
print(students)
# 按age值升序排列
students.sort(key=lambda x:x['age'])
print(students)

