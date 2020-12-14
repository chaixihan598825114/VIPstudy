t1 = (1,2,3)
print(t1)

t2 = (1,)
print(type(t1))

# 错误示范
t3 = (1)
t4 = ('nihao')

print(type(t3))
# t3是int
print(type(t4))
# t4是str

# 元组不可修改，但元组里的列表可以修改
t5 = (1,2,[11,22,33],3,4)
t5[2][0] = 111
print(t5[2][0])
print(t5)