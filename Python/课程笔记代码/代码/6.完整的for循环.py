# 完整的for循环
# 查找班级中是否存在 张三 这个同学
# 如果存在 输出该生信息
# 如果不存在 提示没有该学生
students = [
    {"name": "阿土", "age": 20, "gender": True, "height": 1.7, "weight": 75.0},
    {"name": "小美", "age": 19, "gender": False, "height": 1.6, "weight": 45.0}, ]

for item in students:
    # print(item["name"])
    if item["name"] == "阿aa土":
        print("阿土存在")
        break
    # print("张三不存在")
    # else:
    #     print("张三不存在")
else:
    print("阿aa土不存在")