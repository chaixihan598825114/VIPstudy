'''
# 局部变量：只在函数内生效，函数调用完成后则销毁
def testA():
    a = 100
    print(a)
testA()
# print(a)
# 全局变量：函数内外都生效
a = 100
def testB():
    print(a)
testB()
print(a)

# 在函数内修改全局变量 global
b = 100
def testC():
    print(b)

def testD():
    global b    #声明此时用的变量b为全局变量
    b = 150     #此时全局变量被修改为150（如果不用global说明，只是定义一个局部变量b，全局变量值不会发生改变 ）
    print(b)
testC()
testD()
print(f'此时全局变量改为{b}')
'''
# 共用全局变量
a = 1000
def sum_num():
    global a
    a = 500
def sum_num2():
    print(a)
sum_num()   #先调用函数sum_num，执行函数内代码：声明全局变量并修改为1000
sum_num2()  #再调用函数sum_num2，执行函数内代码：打印全局变量num

# 返回值作为参数传递
def test1():
    return 50
def test2(num):
    print(num)
result = test1()
print(result)

