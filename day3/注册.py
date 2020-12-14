# 全局变量
list1 = [{'name':'zhangsan','age':'18'},{'name':'laowang','age':'29'},{},{},{},{},{}]

# 查询功能
def sel_user(user_name):
    global list1
    n = 0
    while n < len(list1):
        if user_name in list1[n].values():
            print(f"此用户已注册，用户名为:{user_name},年龄为:{list1[n].get('age')}")
            break
        n += 1
    else:
        print('此用户不存在')
# sel_user(user_name)

# 注册功能
def add_user(user_name,user_age):
    global list1
    n = 0
    while n < len(list1):
        if user_name in list1[n].values() and user_age in list1[n].values():
            print(f'{user_name}已被注册')
            break
        n += 1
        if user_name not in list1[n].values() and user_age not in list1[n].values():
            if not list1[n]:
                list1[n].update(name=user_name, age=user_age)
                print('注册成功')
                break
# name = input('输入名字')
# age = input('输入年龄')
# add_user(user_name, user_age)


# 界面
def start_use():
    print('----------------')
    print('*   1-新增用户')
    print('*   2-查询用户')
    print('*   3-删除用户')
    print('----------------')
start_use()

# 选择功能
def switch_func(switch):
    dict1 = {'1':'*   1-新增用户','2':'*   2-查询用户','3':'*   3-删除用户'}
    print(dict1.get(switch))
    if switch == '2':
        user_name = input('请输入查询用户:')
        sel_user(user_name)
    elif switch == '1':
        user_name = input('请输入注册名字')
        user_age = input('请输入年龄')
        add_user(user_name,user_age)
switch = input('请选择使用功能：')
switch_func(switch)

print(list1)

