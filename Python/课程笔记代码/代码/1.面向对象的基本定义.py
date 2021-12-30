# 类的定义
# 类名的定义 是大驼峰

# class 类名:
#     # 功能
#     def 方法名(self,参数列表):
#         pass
# # 创建对象
# 对象名 = 类名()
# 对象名.方法名（）

"""
需求
    小猫 爱 吃 鱼，小猫 要 喝 水
"""


class Cat:
    # 吃
    def eat(self):
        print("吃鱼")
    # 喝
    def drink(self):
        print("喝水")

# # 创建对象
# tom = Cat()
# # tom.drink()
# tom.eat()
# print(id(tom))
# print(tom)
# print("内存地址 %x"%id(tom))
# print(tom)
# print("*"*20)
# # 创建第二个对象
# rose = Cat()
# rose.eat()
# print(rose)

