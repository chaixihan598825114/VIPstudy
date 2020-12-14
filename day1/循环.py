# # 循环变量
# n = 0
# # 循环条件
# while n < 10:
# # 循环体
#     print(f'打印第{n+1}次')
#     print('打印第%d次' % (n+1))
# # 循环变量发生变化
#     n = n + 1
# print('打印结束')
#

'''
需求：1-100之前的和
分析：1+2+3+...+100
n = 1
sum = 0

sum = sum + n
n += 1


n = 1
sum = 0
while n <= 100:
    sum = sum + n
    n += 1
print(sum)


n = 1
sum = 0
while n <= 100:
    sum = sum + n
    n += 1
    # i = sum % 2
    if (sum % 2)==0:
        sum = sum + (sum+n)
print(sum)


n = 1
sum = 0
while n <= 100:
    if n%2 == 0:
        sum = sum + n
    n += 1
print(sum)
'''













n = 0
sum = 0
while n <= 10:
    if n % 2 == 0:
        sum = sum + n
    n += 1
print(f'结果为{sum}')









