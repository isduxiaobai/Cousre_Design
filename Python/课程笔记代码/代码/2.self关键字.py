# self关键字的基本使用

class Cat:
    def eat(self):
        print("吃鱼")
        # self 指向的内存地址  指向的是Tom对象的内存地址
        # rose  指向rose对象内存地址
        # self 那一个对象调用该方法 self 就指向哪一个对象、
        print(self)

tom = Cat()
tom.eat()
print(tom)

print("*"*10)

rose = Cat()
rose.eat()
print(rose)