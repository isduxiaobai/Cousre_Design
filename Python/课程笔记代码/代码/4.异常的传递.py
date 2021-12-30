"""
需求
    定义函数 demo1() 提示用户输入一个整数并且返回
    定义函数 demo2() 调用 demo1()
    在主程序中调用 demo2()
"""

def demo1():
    return int(input("请输入一个整数："))

def demo2():
    return demo1()


try:
    print(demo2())
except ValueError:
    print("请输入正确的数字")
except Exception as reslut:
    print("未知错误 ：%s"%reslut)





