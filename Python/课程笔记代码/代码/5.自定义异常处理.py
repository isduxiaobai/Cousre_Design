# 自定义异常处理
"""
定义 input_password 函数，提示用户输入密码
如果用户输入长度 <8，抛出异常
如果用户输入长度 >=8，返回输入的密码
"""

def input_password():
    # 1.接收用户输入密码
    psw = input("请输入密码")
    #2.判断密码长度 如果不合适 抛出异常
    if len(psw) >= 8:
        # 3.返回密码
        return psw
    # 证明密码小于8 抛出异常
    ex = Exception("密码长度不可以少于8:%s"%len(psw))

    raise ex

try:
    print(input_password())
except Exception as reslut:
    print("未知错误 ：%s"%reslut)


