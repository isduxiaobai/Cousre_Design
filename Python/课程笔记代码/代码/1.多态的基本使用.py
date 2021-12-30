# 多态的基本使用
"""
需求
    1. 在 Dog 类中封装方法 game
        普通狗只是简单的玩耍
    2. 定义 XiaoTianDog 继承自 Dog，并且重写 game 方法
        哮天犬需要在天上玩耍
    3. 定义 Person 类，并且封装一个 和狗玩 的方法
        在方法内部，直接让 狗对象 调用 game 方法
"""
class Dog(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "狗的名称是 %s"%self.name

    def game(self):
        print("%s 简单的玩耍"%self.name)

class XiaoTianQuan(Dog):
    # def __init__(self,name,age):
    #     super().__init__(name)
    #     self.age = age

    def game(self):
        print("%s 在天上愉快的玩耍"%self.name)

class JinMao(Dog):
    def game(self):
        print("%s 在地下愉快的玩耍"%self.name)


class Person(object):
    def __init__(self,name):
        self.name = name

    def playWithDog(self,dog):
        print("%s 和 %s  一起愉快的玩耍"%(self.name,dog.name))
        dog.game()

# dog = Dog("旺财")
# print(dog)

xiaotianquan = XiaoTianQuan("哮天犬")
print(xiaotianquan)

jinmao = JinMao("金毛")


p = Person("张三")
# p.playWithDog(dog)

p.playWithDog(xiaotianquan)
p.playWithDog(jinmao)


