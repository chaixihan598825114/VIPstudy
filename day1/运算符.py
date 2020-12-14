# 复合赋值运算符，先算右侧
a = 100
a += 1
# 输出101  a = a + 1
print(a)

b = 2
b *= 3
print(b)

c = 10
c += 1 + 2
print(c)

# 比较运算符,通常用来判断

a = 7
b = 5

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

# 逻辑运算符
# and 且，全真为真，否则为假
# or 或，一个真为真，全真为真，否则为假
# not 取反值

a = 1
b = 2
c = 3
print((a < b) and (b < c))
print((a > b) and (b < c))
print((a < b) or (b < c))
print(not(a > b))