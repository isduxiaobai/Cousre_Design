# 名片管理系统 模块工具包
# 定义列表 用来记录所有人的信息 里面存放的是字典
import prettytable as pt

card_list = []
width = 42


# 显示主界面
def show_meun():
    print("*" * 50)
    print("欢迎使用名片管理系统【V1.0】".center(width))
    print("1. 新增名片".center(width))
    print("2. 显示全部".center(width))
    print("3. 查询名片".center(width))
    print("0. 退出系统".center(width))
    print("*" * 50)

# 新增名片
def new_card():
    print("-" * 50)
    print("功能：新增名片")

    # 1. 接受用户输入信息
    name = input("请输入要添加的姓名：")
    phone = input("请输入要添加的手机号：")
    qq = input("请输入要添加的QQ号码：")
    email = input("请输入要添加的邮箱：")

    # 2. 将接受到的个人信息 存放在字典中
    # 字典的key名字一般情况下 和 变量的名字相同；
    card_dict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }

    # 3.将 字典 存储在 列表中
    card_list.append(card_dict)

    print("添加成功%s" % card_list)


# 显示全部
def show_all():
    print("-" * 50)
    print("功能：显示全部")

    # 先判断 如果card_list 为空 结束函数
    if len(card_list) == 0:  # 为空
        print("该系统 没有数据")
        # return 结束函数  如果为空 该函数内部 以下的代码 不执行
        return

    # 0:显示  姓名		电话		QQ		邮箱

    # # print("姓名\t\t电话\t\tQQ\t\t邮箱")
    # for item in ["姓名", "电话", "QQ", "邮箱"]:
    #     print("%s\t\t" % item, end="")
    #
    # # 换行
    # print()
    #
    # # 1. 遍历列表card_list
    # for card in card_list:
    #     # card 代表的是一个字典（一个名片）
    #     print("%s\t\t%s\t\t%s\t\t%s\t\t" % (
    #         card["name"],
    #         card["phone"],
    #         card["qq"],
    #         card["email"]
    #     ))
    tb = pt.PrettyTable()
    tb.field_names = ["姓名", "电话", "QQ", "邮箱"]
    i = 0
    for card in card_list:
        info = []
        for value in card.values():
            info.append(value)
            # 每循环一条名片信息，此前的序号+1，并将新的值添加到该名片的列表中
            i += 1
        tb.add_row(info)
    print(tb)

# 对查找到的数据 进行处理
def deal_card(card):
    # 3.1 接受用户的指令
    action_str = input("请输入你选择：【1】修改、【2】删除、【3】返回")

    # 3.2 判断用户输入
    # if action_str == "1":  # 修改
    #     card["name"] = input("请输入要修改的姓名：")
    #     card["phone"] = input("请输入要修改的手机号：")
    #     card["qq"] = input("请输入要修改的QQ号码：")
    #     card["email"] = input("请输入要修改的email地址：")
    #     print("修改成功")
    if action_str == "1":
        card["name"] = input_info(card["name"], "请输入要修改的姓名： ")
        card["phone"] = input_info(card["phone"], "请输入要修改的手机号： ")
        card["qq"] = input_info(card["qq"], "请输入要修改的QQ号码：")
        card["email"] = input_info(card["email"], "请输入要修改的email地址： ")
        print("修改名片成功!")
    elif action_str == "2":  # 删除
        card_list.remove(card)
        print("删除 %s 成功" % card["name"])
    elif action_str == "3":  # 返回上一级
        return
    else:
        print("输入错误~默认返回上一级")
        return


# 查询名片
def search_card():
    print("-" * 50)
    print("功能：显示全部")

    # 1. 先判断 如果card_list 为空 结束函数
    if len(card_list) == 0:  # 为空
        print("该系统 没有数据")
        # return 结束函数  如果为空 该函数内部 以下的代码 不执行
        return

    # 接受用户输入 要查询的姓名
    find_name = input("请输入要查询的姓名：")

    # 2. 遍历列表card_list
    for card in card_list:
        # # card 代表的是一个字典（一个名片）
        # if card["name"] == find_name:  # 有这个用户
        #     # 显示查找到的用户
        #     # 2.1  print("姓名\t\t电话\t\tQQ\t\t邮箱")
        #     for item in ["姓名", "电话", "QQ", "邮箱"]:
        #         print("%s\t\t" % item, end="")
        #
        #     print()  # 换行
        #
        #     # 2.2 card 代表的是一个字典（一个名片）
        #     print("%s\t\t%s\t\t%s\t\t%s\t\t" % (
        #         card["name"],
        #         card["phone"],
        #         card["qq"],
        #         card["email"]
        #     ))
        tb = pt.PrettyTable()
        tb.field_names = ["姓名", "电话", "QQ", "邮箱"]
        info = []
        if card["name"] == find_name:  # 有这个用户
            for value in card.values():
                info.append(value)
            tb.add_row(info)
            print(tb)
            # 进行数据的处理
            deal_card(card)

            # 找到该数据 结束循环
            break

    else:
        print("没有该用户~~~")

# 细化修改名片功能
def input_info(card_value,message):
    # 1.提示用户输入
    return_str = input(message)
    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(return_str)>0:
        return return_str
    # 3. 如果用户没有输入内容，返回 `字典中原有的值`
    else:
        return card_value
    pass
