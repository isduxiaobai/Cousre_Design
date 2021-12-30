# 异常类型的捕获
# 请输入一个数字
# try:
#     num = int(input("请输入一个数字:"))
#     result = 8/num
#     print(result)
# except:
#     print("除零异常 除数不能为零")
# ValueError 就是错误类型
# ZeroDivisionError 除零异常
# num = int(input("请输入一个数字:"))
# result = 8/num
# print(result)



try:
    num = int(input("请输入一个数字:"))
    result = 8/num
    print(result)
except ZeroDivisionError:
    print("除零异常 除数不能为零")
# except ValueError:
#     print("不能输入字母")
except Exception as result:
    print("未知错误：%s"%result)


