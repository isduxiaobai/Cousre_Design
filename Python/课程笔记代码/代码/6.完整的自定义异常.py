"""
定义 input_password 函数，提示用户输入密码
如果用户输入长度 <8，抛出异常
如果用户输入长度 >=8，返回输入的密码
"""
class Dog:
    pass
# 写继承Exception 使得MyException这个类所创建的对象 具备可抛性
class MyException(Exception):
    # errorInfo: 错误信息
    # currentPswLength 当前密码长度
    def __init__(self,errorInfo,currentPswLength):
        self.errorInfo = errorInfo
        self.currentPswLength = currentPswLength

    def __str__(self):
        return "%s,当前密码长度是%s"%(self.errorInfo,self.currentPswLength)


def input_password():
    # 1.接收用户输入密码
    psw = input("请输入密码")
    #2.判断密码长度 如果不合适 抛出异常
    if len(psw) >= 8:
        # 3.返回密码
        return psw
    # 证明密码小于8 抛出异常
    # ex = Exception("密码长度不可以少于8:%s"%len(psw))
    #
    # raise ex

    ex = MyException("密码长度不可以少于8",len(psw))

    raise ex

try:
    print(input_password())
except Exception as reslut:
    print("未知错误 ：%s"%reslut)