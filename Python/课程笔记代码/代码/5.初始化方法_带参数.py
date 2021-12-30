# 带参数的初始化方法

class Cat:
    # 初始化方法
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def eat(self):
        print("吃鱼")


jack = Cat("jack",10)
print(jack.name)
print(jack.weight)

print("*"*20)

rose = Cat("rose",1)
print(rose.name)
print(rose.weight)

print(jack)