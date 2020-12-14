'''
# 拆包
# 元组
def return_num():
    return 100, 200
num1, num2 = return_num()
print(num1) # 100
print(num2) # 200

# 字典
dict1 = {'name':'Tom','age':18}
a,b = dict1
print(a)
print(b)
print(dict1[a])
print(dict1[b])
'''

# 交换变量值
# 现在 a=10 b=20，交换两个变量的值
a = 10
b = 20
c = 0
print(a,b)  #10,20
c = a
a = b
b = c
print(a,b)  #20,10

# 第二种方法，python独有
c = 50
d = 100
c,d = d,c
print(c,d)  #100,50
