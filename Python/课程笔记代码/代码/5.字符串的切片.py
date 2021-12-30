# 字符串切片
str = "python"
print(str[-1])
print(str[-6])
# IndexError: string index out of range
# print(str[-100])

str = "0123456789"
# 字符串[开始索引:结束索引:步长]
# 截取从 2~5 位置 的字符串
print(str[2:6:1])

#截取从 2~ 末尾 的字符串
print(str[2::])

# 截取从 开始 ~5 位置 的字符串
# print(str[0:6:1])
# print(str[:6])

# 截取完整的字符串
# print(str[0:len(str):1])
# print(str[:])

# 从开始位置，每隔一个字符截取字符串
# print(str[0:len(str):2])
# print(str[::2])

# 从索引 1 开始，每隔一个取一个
# print(str[1::2])

#  截取从 2 ~ `末尾 - 1` 的字符串
# -1 和 9 是同一个位置
# print(str[2:-1:1])


# 截取字符串末尾两个字符
# print(str[8:])
print(str[-2:])

# 字符串的逆序（面试题)
# print(str[::-1])

# 内置函数
# list = [23,45,11,66,88]
# print(max(list))
# print(min(list))

# print("*"*5
user =  input("1 剪刀 2 石头 3 布")
if user in ("1","2","3"):
    print("输入正确")
    int(user)
else:
    print("输入错误")