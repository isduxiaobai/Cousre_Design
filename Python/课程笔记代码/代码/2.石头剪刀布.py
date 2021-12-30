import random

"""
石头剪刀布
    1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
    2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
    3. 比较胜负
"""


# 1.接受用户输入
player = int(input("请出拳：石头（1）／剪刀（2）／布（3）"))
# 2.存储电脑的出拳
computer = random.randint(1,3)
print("computer:%d"%computer)
# 3.判断结果
# 3.1 赢
if ((player == 1 and computer == 2) or
        (player == 2 and computer == 3) or
        (player == 3 and computer == 1)):
    print("赢")
elif player == computer:
    print("平局")
else:
    print("输")