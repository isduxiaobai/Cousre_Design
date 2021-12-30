# -*- coding:utf-8 -*-
import pygame
import random,sys,os
import time
import datetime
from pygame import *

#初始化pygame
pygame.init()
pygame.font.init()
pygame.mixer.quit()

#窗口定位
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (160,26)

#设置一个窗口
canvas = pygame.display.set_mode((1200,700))
canvas.fill((255,255,255))

#窗口标题
pygame.display.set_caption("夺宝奇兵")
pygame.key.set_repeat(10,10)

#游戏状态
state = 'START'


try:
    #素材
    bg = pygame.image.load("./images/bg.png")
    bg1 = pygame.image.load("./images/bg1.png")
    lose = pygame.image.load("./images/lose.png")
    win = pygame.image.load("./images/win.png")
    h = pygame.image.load("./images/hero.png")
    f = pygame.image.load("./images/fire.png")
    m = pygame.image.load("./images/menu.png")
    s = pygame.image.load("./images/screen.png")
except error as e:
    #判断图片素材是否存在
    # easygui.msgbox("【ERROR】找不到图片素材，请检查./images/文件夹。\n点击Ok退出程序！",e)
    print("【ERROR】找不到图片素材，请检查./images/文件夹。")
    print(e)
    pygame.quit()
    sys.exit()

#游戏时间
gametime = 0

#新年倒计时
'''
def newYear(x,y):
    spring=datetime.datetime(2021,2,12,0,0,0)   #春节日期
    today=datetime.datetime.now()       #今天是几月几号
    day=(spring-today).days         #得到还有几天
    second=(spring-today).seconds       #得到还有几秒
    sec=second%60               #根据秒数得到还有几秒
    minute=second/60%60     #根据秒得到分钟数
    hour=second/60/60            #根据秒数得到小时
    if hour>24:
        hour=hour-24    #如果超过24小时，就要算超过1天，所以要减去24
    newyear = "距离2021还有 %d 天 %d 小时 %d 分钟 %d 秒"  %(day,hour,minute,sec)
    fillText(newyear,x,y)
'''

#写文字
def fillText(text,x,y):
    ziti1 = pygame.font.Font('happy.ttf',20)
    Text = ziti1.render(text, True, (0, 0, 0))
    Text1 = ziti1.render(text, True, (255, 255, 255))
    canvas.blit(Text,(x, y))




#玩家
class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.img = h
        self.width = 107
        self.height = 121
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def move(self):
        #键盘控制人物移动
        if event.key == K_UP:
            self.y -= 10
        if event.key == K_DOWN:
            self.y += 10
        if event.key == K_LEFT:
            self.x -= 10
        if event.key == K_RIGHT:
            self.x += 10
        #限制移动范围（碰边停止）
        if self.x >= 1200 - 107:
            self.x = self.x - 10
        if self.x <= 0:
            self.x = self.x + 10
        if self.y >= 700 - 121:
            self.y = self.y -10
        if self.y <= 0:
            self.y = self.y +10

hero = Player(50,350)

#岩浆类
class Magma():
    def __init__(self,x,y,sign):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 500
        self.img = f
        self.sign = sign
        self.speed = random.randint(5,10)
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def move_d(self):
        #向下移动
        self.y += self.speed
    def move_u(self):
        #向下移动
        self.y -= self.speed
    def out_d(self):
        #向下碰边反弹
        if self.y>=-100:
            self.speed = random.randint(-10,-5)
        elif self.y<=-400:
            self.speed = random.randint(5,10)
    def out_u(self):
        #向上碰边反弹
        if self.y <= 400:
            self.speed = random.randint(-10,-5)
        elif self.y >= 600:
            self.speed = random.randint(5,10)
    def hit(self,c):
        return self.x + self.width >= c.x + c.width/4\
            and self.x <= c.x + (c.width/4)*3\
            and c.y + (c.height/4)*3 > self.y\
            and c.y + c.height/4 < self.y + self.height

#Magma类实例化
Magma1 = Magma(210,600,'u')
Magma2 = Magma(350,-400,'d')
Magma3 = Magma(580,600,'u')
Magma4 = Magma(720,-400,'d')
Magma5 = Magma(910,600,'u')
#Magmas列表
Magmas = [Magma1, Magma2, Magma3, Magma4, Magma5]

#画组件
def comPaint():
    #画背景
    canvas.blit(bg,(0,0))
    #画人物
    hero.paint()
    #岩浆
    for m in Magmas:
        m.paint()
    #画喷口
    canvas.blit(bg1,(0,0))
def comMove():
    #岩浆移动
    for m in Magmas:
        if m.sign == 'd':
            m.move_d()
        if m.sign == 'u':
            m.move_u()

def comOut():
    #岩浆反弹
    for m in Magmas:
        if m.sign == 'd':
            m.out_d()
        if m.sign == 'u':
            m.out_u()

def checkHit():
    global state
    for m in Magmas:
        if m.hit(hero):
            state = 'LOSE'
#开始界面的按钮
def button():
    global state
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #获取鼠标坐标
            pos = pygame.mouse.get_pos()
            mouseX = pos[0]
            mouseY = pos[1]
            print(mouseX)
            print(mouseY)
        #判定鼠标是否在按钮范围内点击
        if event.type == MOUSEBUTTONDOWN and\
           40 <= mouseX <= 206 and\
           269 <= mouseY <= 309:
            state = 'RUNNING'#游戏开始
            print("点击了开始键...")
        if event.type == MOUSEBUTTONDOWN and\
           40 <= mouseX <= 206 and\
           318 <= mouseY <= 357:
            print("点击了退出键...")
            pygame.quit()
            sys.exit()#退出游戏

#游戏结束
def end():
    global state
    for event in pygame.event.get():
        #获取鼠标坐标
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            mouseX = pos[0]
            mouseY = pos[1]
            print(mouseX)
            print(mouseY)
        #重新开始游戏
        if event.type == MOUSEBUTTONDOWN and 109 <= mouseX <= 384 and 458 <= mouseY <= 523 or (event.type == KEYDOWN and event.key == K_RETURN):
            state = 'RUNNING'
            hero.x = 50
            hero.y = 350
        #退出
        if event.type == QUIT or (event.type == KEYDOWN and\
        event.key == K_ESCAPE) or\
        event.type == MOUSEBUTTONDOWN and 109 <= mouseX <= 388 and 549 <= mouseY <= 689:#可通过点击关闭按钮或按下ESC退出
                pygame.quit()
                sys.exit()
#开始界面
def Start():
    canvas.blit(m,(0,0))
    button()
    #新年倒计时
    #newYear(18,618)
    canvas.blit(s,(495,0))
    fillText("游戏截图",1028,2)

while True:
    gametime += 0.1
    #判断游戏状态
    if state == 'RUNNING':
        comPaint()
        comMove()
        comOut()
        checkHit()
        if hero.x > 1025:
            state = 'WIN'
    if state == 'START':
        Start()
    if state == 'LOSE':
        canvas.blit(lose,(0,0))
        end()
    if state == 'WIN':
        canvas.blit(win,(0,0))
        end()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):#可通过点击关闭按钮或按下ESC退出
                pygame.quit()
                sys.exit()
        if event.type == KEYDOWN:
            hero.move()
    #刷新屏幕
    pygame.display.update()
    pygame.time.delay(10)
