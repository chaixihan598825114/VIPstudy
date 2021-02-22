

class Dog(object):
    def work(self):
        print('指哪打哪')

class ArmDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self,dog):
        dog.work()

ad = ArmDog()
dd = DrugDog()

daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)


# 三. 类属性和实例属性
# 3.1 类属性
# 3.1.1 设置和访问类属性
# 类属性就是 类对象 所拥有的属性，它被 该类的所有实例对象 所共有。
# 类属性可以使⽤ 类对象 或 实例对象 访问。
import dog as dog
'''

class Dog(object):
    def work(self): # ⽗类提供统⼀的⽅法，哪怕是空⽅法
        print('指哪打哪...')

class ArmyDog(Dog): # 继承Dog类
    def work(self): # ⼦类重写⽗类同名⽅法
        print('追击敌⼈...')

class DrugDog(Dog):
    def work(self):
        print('追查毒品...')

class Person(object):
    def work_with_dog(self, dog): # 传⼊不同的对象，执⾏不同的代码，即不同的work函数
        dog.work()

ad = ArmyDog()
dd = DrugDog()
daqiu = Person()
daqiu.work_with_dog(ad)
daqiu.work_with_dog(dd)
'''