# 1.打印小猫爱吃鱼，小猫爱喝水

class Cat():
    # def __init__(self,fish,water):
    #     self.fish = fish
    #     self.water = water

    def eat(self,food):

        print(f'小猫要吃{food}')

    def drink(self,juice):
        print(f'小猫要喝{juice}')

smallCat = Cat()


smallCat.eat('鱼')
smallCat.drink('水')


