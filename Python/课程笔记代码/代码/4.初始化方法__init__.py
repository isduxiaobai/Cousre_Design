# __init__初始化方法
# 给类添加属性的目的：
    # 通过类来创建 对象， 创建完对象 对象就应该已经拥有了该属性
    # 就要用到初始化方法

class Cat:

    # 该方法是创建对象过程中 自动调用
    def __init__(self):
        self.age = 10
        self.name = "tom"

    def eat(self):
        print("吃鱼 %d"%self.age)

tom = Cat()
print(tom.age)
print(tom.name)
# tom.eat()

rose = Cat()
rose.name = "jack"
print(rose.age)
print(rose.name)