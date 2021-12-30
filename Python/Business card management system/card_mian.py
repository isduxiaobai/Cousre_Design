# 名片管理系统
"""
**************************************************
             欢迎使用名片管理系统【V1.0】
                 1. 新增名片
                 2. 显示全部
                 3. 查询名片
                 0. 退出系统
**************************************************

"""
import card_tools

while True:
    # 显示主界面
    card_tools.show_meun()
    # 接受用户输入
    action_user = input("请输入您的选择：")

    if action_user in ["1","2","3"]:
        if action_user == "1":  # 新增名片
            card_tools.new_card()
        elif action_user == "2":  # 显示全部
            card_tools.show_all()
        elif action_user == "3": # 查询名片
            card_tools.search_card()

    elif action_user == "0":
        print("欢迎再次使用名片管理系统！！")
        # 结束循环
        break
    else:
        print("输入错误，请重新输入！！")



