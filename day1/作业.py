'''
# 正三角
a = 0
while a < 5:
    a += 1
    print(a * '*')


# 倒三角
b = 5
while 0 < b <= 5:
    print(b * '*')
    b -= 1


# 靠右对齐
c = 0
d = 5
while c < 5:
    c += 1
    d -= 1
    print(d * ' ' + c * '*')


# 正三角形
e = 0
f = 5
while e < 5:
    e += 1
    f -= 1
    print(f * ' ' + (2 * e-1) * '*')

# 倒三角形
m = 5
n = 0
while 0 < m <= 5:
    print(n * ' ' + (2 * m - 1) * '*')
    n += 1
    m -= 1
'''



n = 1
while n < 10:
    a = 1
    b = 1
    while b < 10:
        print(a,'*',b,'=',b,end= '  ')
        b += 1
    n += 1
    print(' ')


a = 1
b = 1
while b < 10:
    print(a,'*',b,'=',b,end= '  ')
    b += 1









