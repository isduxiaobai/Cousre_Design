# 异常基本介绍
# 要求用户输入一个数字  接收后打印输出

try:
    num = int(input("请输入一个数字："))
    print(num)
except:  # 有错误后 针对错误做针对性处理
    print("请输入正确的数字")

print("---------------------------------")