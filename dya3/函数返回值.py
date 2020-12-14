def buy(a):
    return a+1

# 使用变量保存函数返回值
goods = buy(1)
print(goods)


code = int(input('请输入密码'))
def bank():
    """ 银行函 """
    print('-----选择功能-----')
    print('查询余额')
    print('取款')
    print('存款')
    print('-----欢迎使用-----')

bank()
help(bank())