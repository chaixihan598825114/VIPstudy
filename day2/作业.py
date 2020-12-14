'''
1、PDF中while循环的最后两个题目（1-三角形*；2-99乘法表）
2、求100以内能被3整除的数，并将作为列表输出
3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
4、求斐波那契数列 1 1 2 3 5 8 13 ……
5、求100以内的质数（只能被1和它本身整除）
6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
7、有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
9、有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
10、有一堆字符串，“aabbbcddef”，输出abcdef
'''

'''
# 2、100以内被三整除的数
# 循环
n = 0
list1 = []
while n < 100:
    if n % 3 == 0:
        list1.append(n)
    n += 1
print(list1)
# 列表推导式
list1 = [n for n in range(100) if n % 3 == 0]
print(list1)


# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
s2 = set(list1)
list3 = list(s2)
print(list3)

list1 = [1,2,3,4,3,4,2,5,5,8,9,7]
i = 0
s1 = set()
while i < len(list1):
    s1.add(list1[i])
    i += 1
list2 = list(s1)
print(list2)

# 4、求斐波那契数列 1 1 2 3 5 8 13 ……
a = 1
b = 1
list = []
for i in range(10):
    c = a + b
    a = b
    b = c
    list.append(c)
print(list)

# 6、有一堆字符串“aabbbcddef”打印出不重复的字符串结果：cef
s1 = 'a,a,b,b,b,c,d,d,e,f'
i = 0
list1 = list(s1)
# while i < len(list1):
#     if list1.count(list1[i]) == 1:
#         print(list1[i],end='')
#     i+=1
#
for list1[i] in list1:
    if list1.count(list1[i]) == 1:
        print(list1[i],end='')
    i += 1
    
    
# 8、有一堆字符串，“welocme to super&Test”，打印出tseT&repus ot ……全部单词原位置反转
s1 = 'welocme to super&Test'
print(s1[::-1])    
'''

# # 7、有一堆字符串，“welocme to super&Test”，打印出superTest，不能查字符的索引
# s1 = 'welocme to super&Test'
# # i = s1.find('s')
# s2 = []
# s3 = []
# i = 0
# n = 0
# for i in s1:
#     if i == '&':
#         continue
#     s2.append(i)
# # print(s2)
# for n in s2:
#     print(n)
#     if n != 's':
#         del s2[n]
#
#     # s2.pop(n)
#     # if n == 's':
#     #     break
#     # # print(n,end='')

# 9、有一堆字符串，“abcdef”，将收尾反转，结果：fedcba，不能使用现有的函数或方法，自己写算法实现
s1 = 'abcdef'
s2 = []
n = 0
for n in s1:
    if n == max(s1):
        s2.append(n)






