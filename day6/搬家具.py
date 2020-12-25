# 将小于房子剩余面积的家具放到房子中


class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

class Home():
    def __init__(self,area):
        self.furniture = []
        self.area = area
        self.free_area = area

    def __str__(self):
        return f'房子面积为{self.area},剩余面积为{self.free_area}，放置的家具有{self.furniture}'

    def add_furnture(self,item):
        if self.free_area >= item.area:
            self.furniture.append(item.name)
            self.free_area -= item.area
        else:
            print('放不下了')

bed = Furniture('双人床',80)
chair = Furniture('椅子',30)
jia1 = Home(100)
# print(jia1)

jia1.add_furnture(bed)
# print(jia1)
jia1.add_furnture(chair)
print(jia1)