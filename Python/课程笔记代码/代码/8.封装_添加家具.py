"""
需求
1. 房子(House) 有 户型、总面积 和 家具名称列表
    新房子没有任何的家具
2. 家具(HouseItem) 有 名字 和 占地面积，其中
    席梦思(bed) 占地 4 平米
    衣柜(chest) 占地 2 平米
    餐桌(table) 占地 1.5 平米
3. 将以上三件 家具 添加 到 房子 中
4. 打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表

# 当出现 对象间的引用问题的时候  一定记住 被包含的对象先有。
"""
class House_item:
    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return " %s 占地 %.2f"%(self.name,self.area)

class House:
    # 1.初始化
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.item_list = []
        self.free_area = area

    #2. 添加家具  item代表家具
    def add_item(self,item):
        # 1.判断房屋的剩余面积是否可以添加家具
        if self.free_area < item.area:
            print("空间不够~~~")
            return
        # 2. 将家具添加到 家具列表
        self.item_list.append(item.name)

        # 3.计算剩余面积
        self.free_area -= item.area

    # 3.打印输出对象时 输出对象的属性
    def __str__(self):
        return "房屋类型：%s ,房屋面积：%.2f,家具列表：%s,剩余面积：%.2f"%(
            self.house_type,self.area,self.item_list,self.free_area)


# 1.创建家具
bed = House_item("席梦思",5)
table = House_item("餐桌",1.5)
chest = House_item("衣柜",2)

# 2.创建房子
house = House("三室两厅",6)
# 3.将家具添加到房子中
house.add_item(bed)
house.add_item(table)
house.add_item(chest)
# 4.打印房子
print(house)

