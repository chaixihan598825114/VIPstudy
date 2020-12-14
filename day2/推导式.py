'''
# for循环实现
list1 = []
for  i in range(10):
    list1.append(i)
print(list1)

# while循环实现
list2 = []
n = 0
while n < 10:
    list2.append(n)
    n += 1
print(list2)

#列表推导式实现
list3 = [m for m in range(10)]
print(list3)


# list1 = [(i,j) for i in range (1,3) for j in range(3)]
# print(list1)

list1 = []
for i in range (1,3):
    for j in range(3):
        list1.append((i,j))
print(list1)
'''

# 字典推导式
dict1 = {i:i ** 2 for i in range(1,5)}
print(dict1)

i = i ** 2
for i in range(1,5):
    print(dict1)



list1 = ['name','age','gender']
list2 = ['Tom',20,'man']
dict2 = {list1[i]:list2[2] for i in range (len(list1))}
print(dict2)

counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'Lenovo': 199, 'acer': 99}
count1 = {key:value for key,value in counts.items() if value >= 200}
print(count1)

