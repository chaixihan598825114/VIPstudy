# 带参数的__init__
class Washer():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    # def __str__(self):
    #     return '这是美的洗衣机的说明书'

    def wash(self):
        print(f'洗衣机的宽度是{self.width},高度是{self.height}')
    def use_old(self):
        print(f'洗衣机的使用寿命是{medi.old}年')

    def __del__(self):
        print(f'{self}已经被删除了')



# 在创建类的对象的时候就开始传参
medi = Washer(100,200)
medi1 = Washer(200,400)

# medi.old = 20
#
# medi.wash()
# medi.use_old()
del medi

print(medi)