# # 类的创建
#
# class Washer():
#     def wash(self):
#         print('洗衣服')
#     def wash1(self):
#         print('晾衣服')
#
# # 创建实例（创建对象）
# medi1 = Washer()
# medi2 = Washer()
#
# # 类的外面添加属性
# medi1.width = 100
# medi1.height = 300
#
# print(f'美的宽是{medi1.width}')
# print(f'美的长是{medi1.height}')


class Washer():
    def __init__(self):
        self.width = 500
        self.height = 800


    def wash(self):
        print(f'洗衣机的宽度是{self.width},高度是{self.height}')
    def use_old(self):
        print(f'洗衣机的使用寿命是{medi.old}年')

medi = Washer()

medi.old = 20

medi.wash()
medi.use_old()