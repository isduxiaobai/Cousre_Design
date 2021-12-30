class Cat:
    # 初始化方法
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight

    def eat(self):
        print("吃鱼")

    # 通过print函数打印对象 输出位对象的属性值 而不是内存地址
    def __str__(self):
        return "猫的名称：%s,猫的体重是：%.2f"%(self.name,self.weight)


    def __del__(self):
        print("del 从内存中销毁 ")

jack = Cat("jack",10)
# print(jack.name)
# print(jack.weight)
print(jack)

del jack

print("*"*20)