"""
需求
    1. 小明 体重 75.0 公斤
    2. 小明每次 跑步 会减肥 0.5 公斤
    3. 小明每次 吃东西 体重增加 1 公斤
"""
class Person:
    #1. 初始化
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    # 2.吃东西
    def eat(self):
        self.weight += 1
        print("吃完体重是：%.2f"%self.weight)

    # 3.跑步
    def run(self):
        self.weight -= 0.5
        print("跑完步体重：%.2f"%self.weight)

    def __str__(self):
        return "姓名：%s,体重: %.2f"%(self.name,self.weight)

xiaoming = Person("小明",75)
print(xiaoming)

xiaoming.eat()
xiaoming.run()
print(xiaoming)
