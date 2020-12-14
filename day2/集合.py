# 创建集合使用{}或set()，但是如果创建空集合只能使用set(),因为{}用来创建空字典
# 集合可以去重，且是无序的（每次可能都是随机打印），不支持下标
# s1 = {60,10,20,30,40,50}
# print(s1)
# print(type(s1))
# s2 = {10,30,20,10,30,50,30,50}
# print(s2)
# s3 = set('abcdefg')
# print(s3)
# s4 = set()
# print(type(s4))
# s5 = {}
# print(type(s5))

# 增加数据
# add用法
s1 = {10,20}
s1.add(100)
s1.add(10)
print(s1)


# update(),追加的数据是序列
s1.update([100,200])
s1.update('abc')
print(s1)

# 删除
# remove(),删除集合中的指定数据，如果数据不存在会报错
s1 = {10,20}
s1.remove(10)
print(s1)
s1.remove(10) #会报错
print(s1)

# discard()，删除集合中的指定数据，数据不存在也不会报错
s2 = {10,20}
s2.discard(10)
print(s2)
s2.discard(10)
print(s2)

# pop() 随机删除集合中的某个数据 并返回这个数据
s3 = {10,20,30}
s3.pop()
print(s3.pop())

# 查找集合中的数据
# in：判断数据在集合序列 & not in：判断数据不在集合序列
s4 = {10,20,30,40}
print(10 in s4)
print(10 not in s4)



