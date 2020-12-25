# 性别为男的梁超老师教测试

# class Teacher():
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#
#     def teach(self,item):
#         print(f'{self.name}老师，性别为{self.gender}，教{item}')
#
# teacher1 = Teacher('chao','nan')
#
# teacher1.teach('ceshi')


# 烤地瓜

class Potatto():
    def __init__(self):
        self.cook_time = 0
        self.cook_static = '生的'
        self.condiments = []

    def add_condiments(self,condiment):
        self.condiments.append(condiment)

    def cook(self,time):
        self.cook_time += time
        if 0 <= self.cook_time <= 3:
            self.cook_static = '生的'
        elif 3 < self.cook_time <= 5:
            self.cook_static = '半生不熟'
        elif 5 < self.cook_time <= 8:
            self.cook_static = '熟了'
        elif self.cook_time > 8:
            self.cook_static = '糊了'

    def __str__(self):
        return f'这个地瓜烤了{self.cook_time}分钟，状态是{self.cook_static}，加了{self.condiments}调料'

digua1 = Potatto()
digua1.cook(5)
digua1.add_condiments('白糖')

digua1.cook(2)
digua1.add_condiments('醋')
print(digua1)
