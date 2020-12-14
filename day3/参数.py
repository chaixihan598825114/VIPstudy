'''
#位置参数，传递和定义的参数值与顺序及个数必须一致
def user_info1(name, age, gender):
    print(f'您的名字是{name}, 年龄是{age}, 性别是{gender}')


# 关键字参数，函数调用时，通过"键=值"的形式加以指定
def user_info2(name,age,gender):
    print(f'您的名字是{name},年龄是{age}，性别是{gender}')

user_info2('rose',age=20,gender='女')
user_info2('小明',gender='男',age=18)

# 默认参数 也叫缺省参数，用于定义函数，为参数提供默认值，调用函数是可不传默认该参数的值（所有位置参数必须出现在默认参数前，包括函数定义和调用）
# 缺省参数，可传可不传，传就走传参，不传就走默认值（不传的前提是该参数必须得有默认值）
def user_info3(name,age,gender='男'):
    print(f'您的姓名是{name}年龄是{age}性别是{gender}')
user_info3('Tom',20)
user_info2('Rose',18,'女')

# 不定长参数，也叫可变参数；用于不确定调用的时候会传递多少个参数（不传参也可以，不会报错）
# 此时就可用包裹(packing)位置参数，包裹关键字参数进行传递参数

# 包裹位置传递：传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为⼀个元组(tuple)，args是一个元组类型
def user_info4(*args):
    print(args)
user_info4('Tom')       #打印结果为('Tom',)
user_info4('Rose',18)   #打印结果为('Rose',18)
list1 = [1,2,3]         #提前定义列表
user_info4(*list1)      #传入的时候必须带 * 星号
'''
# 包裹关键字传递：传进的所有参数都会被kwargs变量收集，它会根据传进参数合并为⼀个字典(dict)，kwargs是一个字典类型
def user_info5(**kwargs):
    print(kwargs)
user_info5(name = 'Tony',age = 99,gender = '男')     #打印结果为{'name': 'Tony', 'age': '99', 'gender': '男'}
dict1 = {'name':'Tony','age':99,'gender':'男'}       #提前定义字典
user_info5(**dict1)                                  #传入字典必须带**
