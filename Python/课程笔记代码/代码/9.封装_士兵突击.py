"""
需求
    1. 士兵 许三多 有一把 AK47
    2. 士兵 可以 开火
    3. 枪 能够 发射 子弹
    4. 枪 装填 装填子弹 —— 增加子弹数量
"""
import time
class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    # 添加子弹
    def add_bullet(self,count):
        self.bullet_count += count

    # 发射
    def shoot(self):
        # 1.先判断是否有子弹
        if self.bullet_count <= 0:  # 没子弹
            print("没子弹 你打个毛线~~")
            return
        # 2.有子弹进行射击
        # self.bullet_count -= 1

        # 3.喊个口号
        while self.bullet_count >0:
            time.sleep(0.5)
            print("冲~~~【%d】"%self.bullet_count)
            self.bullet_count -= 1

class Soldier:
    def __init__(self,name):
        self.name = name
        self.gun = None   # 对象类型的空 使用None   Python中没有Null

    def fire(self):
        # 1.先判断是否有枪
        if self.gun is None:
            print("你没枪 ")
            return
        # 装子弹
        self.gun.add_bullet(10)

        # 2.开火

        self.gun.shoot()


ak47 = Gun("ak47")

xusanduo = Soldier("许三多")
xusanduo.gun = ak47

xusanduo.fire()