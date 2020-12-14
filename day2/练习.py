name = input('请输入姓名')
className = '小明,小刚,小李,小李，小张'
res = className.find(name)
only = className.count(name)
if res == -1:
    print(f'{name}不在班级内')
elif only == 1:
    print('不重复')
elif only > 1:
    print('姓名重复',end = '')
    print(className.count(name))
