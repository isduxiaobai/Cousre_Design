import pygame
from pygame.locals import *
from sys import exit
import random

# 初始化 专业_小鸟
pygame.init()

# 常量
MAX_I = 34  # 让地图预留4行作为放入方块的地方
MAX_J = 15
SIZE = 15

COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 255, 255)]

gameMap = [[0 for j in range(MAX_J + 3)] for i in range(MAX_I + 3)]  # 全局地图
tetrisHeight = 0  # 塔高

# 基本方块
tetrises = [
    [
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],
    [
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
]

# 分数
score = 0

# 等级
level = 1

# 音乐开关
isMusic = True

# 游戏暂停
isPause = False


# 播放音乐
def playMyMusic(src):
    if isMusic:
        sound = pygame.mixer.Sound(src)
        sound.play()


# 方块类
class Tetris:
    __i = 0
    __j = 0
    __color = 0
    __nextColor = 0
    __nextType = 0

    def __init__(self):
        self.__nextColor = random.randint(0, 3) + 1  # 一共四种颜色
        self.__nextType = random.randint(0, 6)  # 一共七种类型
        self.createTetris()

    def createTetris(self):
        # 根据类型调整一下快出现的位置
        if self.__nextType == 0:
            self.__i = 1
            self.__j = 7
        else:
            self.__i = 2
            self.__j = 6

        self.__color = self.__nextColor

        # 根据方块模板，放置整个到地图
        for i in range(4):
            for j in range(4):
                if tetrises[self.__nextType][i][j] == 1:
                    if gameMap[self.__i + i][self.__j + j] == 0:
                        gameMap[self.__i + i][self.__j + j] = self.__color
                    else:
                        print('游戏失败！')
                        exit()
                        return -1

        # 产生下一种类型和颜色
        self.__nextColor = random.randint(0, 3) + 1  # 一共四种颜色
        self.__nextType = random.randint(0, 6)  # 一共七种类型

        playMyMusic('music/get.wav')

    def moveDown(self):
        global gameMap

        # 判断是否可以下移
        for j in range(4):
            for i in range(3, -1, -1):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    # 判断是否到底
                    if self.__i + i + 1 > MAX_I:
                        return 1

                    # 判断前面是否有东西
                    if gameMap[self.__i + i + 1][self.__j + j] != 0:
                        return 1

                    break

        # 下移
        for j in range(4):
            for i in range(3, -1, -1):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    gameMap[self.__i + i][self.__j + j], gameMap[self.__i + i + 1][self.__j + j] = \
                        gameMap[self.__i + i + 1][self.__j + j], gameMap[self.__i + i][self.__j + j]

        self.__i += 1

    def stopTetris(self):
        global tetrisHeight

        flag = True

        for i in range(4):
            for j in range(4):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    gameMap[self.__i + i][self.__j + j] += 10

                    # 找到第一个颜色方块
                    if flag:
                        tetrisHeight = MAX_I - self.__i if tetrisHeight < MAX_I - self.__i else tetrisHeight
                        flag = False

        self.deleteRow()

    def moveLeft(self):
        # 判断是否能够左移
        for i in range(4):
            for j in range(4):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    if self.__j + j - 1 < 0:
                        return 1
                    if gameMap[self.__i + i][self.__j + j - 1] != 0:
                        return 1

                    break

        # 左移
        for i in range(4):
            for j in range(4):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    gameMap[self.__i + i][self.__j + j], gameMap[self.__i + i][self.__j + j - 1] = \
                        gameMap[self.__i + i][self.__j + j - 1], gameMap[self.__i + i][self.__j + j]

        self.__j -= 1

    def moveRight(self):
        # 判断是否能右移
        for i in range(4):
            for j in range(3, -1, -1):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    if self.__j + j + 1 >= MAX_J:
                        return 1
                    if gameMap[self.__i + i][self.__j + j + 1] != 0:
                        return 1

                    break

        # 右移
        for i in range(4):
            for j in range(3, -1, -1):
                if gameMap[self.__i + i][self.__j + j] == self.__color:
                    gameMap[self.__i + i][self.__j + j], gameMap[self.__i + i][self.__j + j + 1] = \
                        gameMap[self.__i + i][self.__j + j + 1], gameMap[self.__i + i][self.__j + j]

        self.__j += 1

    def change(self):
        tMap = [[0 for j in range(4)] for i in range(4)]

        # 将所有方块顺时针旋转90度赋值到 tMap 中
        i = 0
        k = 3
        while i < 4:
            for j in range(4):
                if MAX_I > self.__i + j >= 0 and MAX_J > self.__j + k >= 0 and gameMap[self.__i + j][
                    self.__j + k] == 0 or \
                        gameMap[self.__i + j][self.__j + k] == self.__color:
                    tMap[j][k] = gameMap[self.__i + i][self.__j + j]

                else:
                    return

            i += 1
            k -= 1

        # 赋值
        for i in range(4):
            for j in range(4):
                gameMap[self.__i + i][self.__j + j] = tMap[i][j]

        playMyMusic('music/change.wav')

    def deleteRow(self):
        # 找到有方块的最后一行
        lastRow = 0
        t = False
        for i in range(3, -1, -1):
            for j in range(4):
                if gameMap[self.__i + i][self.__j + j] == self.__color + 10:
                    lastRow = self.__i + i
                    t = True
                    break
            if t:
                break

        for i in range(lastRow, MAX_I - tetrisHeight - 1, -1):
            for j in range(MAX_J):
                if gameMap[i][j] == 0:
                    break
            else:
                global score
                score += 10
                playMyMusic('music/delete.wav')

                # 删除行
                gameMap.pop(i)
                gameMap.insert(0, [0 for j in range(MAX_J + 3)])

                # 增加等级
                global level
                level += score // 1000

                # 再次调用删除行函数操作删行
                self.deleteRow()

    def nextTetris(self):
        return self.__nextType, self.__nextColor


# 全局变量
screen = ''  # 屏幕
gameTetris = Tetris()


# 绘制游戏地图
def drawMap():
    # 画上边框
    for i in range(MAX_I - 4):
        # 画右边
        myRect(screen, COLORS[2], [0, i * SIZE, SIZE, SIZE])
        # 画左边
        myRect(screen, COLORS[2], [(MAX_J + 1) * SIZE, i * SIZE, SIZE, SIZE])

    # 画下面
    for i in range(MAX_J + 2):
        myRect(screen, COLORS[2], [i * SIZE, (MAX_I - 4) * SIZE, SIZE, SIZE])

    # 给地图涂色
    for i in range(4, MAX_I):
        for j in range(MAX_J):
            t = gameMap[i][j] - 10 if gameMap[i][j] > 10 else gameMap[i][j]

            myRect(screen, COLORS[t], [(j + 1) * SIZE, (i - 4) * SIZE, SIZE, SIZE])

    # 文字内容，下一个方块
    drawMyText(screen, "下一块：", 305, 18, 15, (255, 255, 255))

    # 绘制下一块方块
    startX = 270
    startY = 30

    nextType, nextColor = gameTetris.nextTetris()

    # 显示下一个方块的背景
    pygame.draw.rect(screen, COLORS[5], [startX, startY, SIZE * 4, SIZE * 4], 1)
    mySize = SIZE * 0.8  # 缩小下一个方块大小

    # 根据形状，修改方块的位置（居中）
    if nextType == 0:
        startX += (SIZE * 4 - mySize) / 2
        startY += (SIZE * 4 - mySize * 4) / 2
    elif nextType == 2 or nextType == 3:
        startX += (SIZE * 4 - mySize * 2) / 2
        startY += (SIZE * 4 - mySize * 3) / 2
    elif nextType == 4 or nextType == 5 or nextType == 6:
        startX += (SIZE * 4 - mySize * 3) / 2
        startY += (SIZE * 4 - mySize * 2) / 2
    elif nextType == 1:
        startX += (SIZE * 4 - mySize * 4) / 2
        startY += (SIZE * 4 - mySize * 4) / 2

    # 绘制下一个方块
    for i in range(4):
        for j in range(4):
            # 绘制有图形地方
            if tetrises[nextType][i][j] == 1:
                # 根据不同的
                myRect(screen, COLORS[nextColor], [startX + j * mySize, startY + i * mySize, mySize, mySize])

    color = (255, 0, 0)
    # 绘制分数
    scoreText = "分数：{}".format(score)
    drawMyText(screen, scoreText, 300, 120, 15, color)

    # 等级
    drawMyText(screen, "等级：{}".format(level), 300, 140, 15, color)

    color = (255, 0, 255)
    # 绘制音乐
    textMusic = "音乐："

    if isMusic:
        textMusic += "开"
    else:
        textMusic += '关'

    drawMyText(screen, textMusic, 300, 220, 15, color)

    # 绘制游戏暂停
    textPause = "暂停："

    if isPause:
        textPause += "开"
    else:
        textPause += '关'

    drawMyText(screen, textPause, 300, 240, 15, color)


    # 绘制键值
    color = (130, 205, 255)
    drawMyText(screen, "↑ 旋转90度", 300, 300, 15, color)
    drawMyText(screen, "← 向左移动", 300, 320, 15, color)
    drawMyText(screen, "→ 向右移动", 300, 340, 15, color)
    drawMyText(screen, "↓ 快速向下", 300, 360, 15, color)

    # 绘制背景
    startY = 410
    color = (255, 255, 0)
    flower = "★"
    drawMyText(screen, flower, 300, startY + 0, 15, color)
    flower = "★★"
    drawMyText(screen, flower, 300, startY + 20, 15, color)
    flower = "★★★"
    drawMyText(screen, flower, 300, startY + 40, 15, color)


# 游戏初始化
def initGame():
    # 将地图倒数对大行全部赋值为-1
    for j in range(MAX_J):
        gameMap[MAX_I][j] = -1

    # 将地图倒数最大列全部赋值为-1
    for i in range(MAX_I):
        gameMap[i][MAX_J] = -1

    # 分数初始化
    score = 0

    # 加载背景音乐文件
    pygame.mixer.music.load('music/bgm.mp3')

    if isMusic:
        # 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
        pygame.mixer.music.play(-1, 0.0)


# 绘制有边框矩形
def myRect(screen, colorRect, pos, lineColor=COLORS[0], bold=1):
    pygame.draw.rect(screen, colorRect, pos)
    pygame.draw.rect(screen, lineColor, pos, bold)


# 绘制我的文字
def drawMyText(screen, text, x, y, bold, fColor, bColor=None):
    # 通过字体文件获得字体对象
    fontObj = pygame.font.Font('font/SIMYOU.TTF', bold)

    # 配置要显示的文字
    textSurfaceObj = fontObj.render(text, False, fColor, bColor)

    # 获得要显示的对象的rect
    textRectObj = textSurfaceObj.get_rect()

    # 设置显示对象的坐标
    textRectObj.center = (x, y)

    # 绘制字体
    screen.blit(textSurfaceObj, textRectObj)


# 游戏主体
def my_game():
    # 得到屏幕
    global screen, isMusic, isPause
    screen = pygame.display.set_mode((350, 465))

    # 设置标题
    pygame.display.set_caption('俄罗斯方块')

    # 初始化游戏
    initGame()

    # 用于控制下落速度
    count = 0

    while True:

        if count == 3 + level * 2:
            if not isPause:  # 只有暂停是 False 才能下移
                if gameTetris.moveDown() == 1:
                    gameTetris.stopTetris()
                    gameTetris.createTetris()

            count = 0

        # 事件判断
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 停止播放背景音乐
                pygame.mixer.music.stop()

                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 控制音乐开关
                if 270 < event.pos[0] < 330 and 210 < event.pos[1] < 225:
                    # 处理音乐开关
                    if isMusic:
                        # 停止播放背景音乐
                        pygame.mixer.music.stop()
                    else:
                        # 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
                        pygame.mixer.music.play(-1, 0.0)

                    isMusic = not isMusic

                # 处理游戏暂停开关
                if 270 < event.pos[0] < 327 and 233 < event.pos[1] < 248:
                    isPause = not isPause

                    if isPause:
                        pygame.display.set_caption('俄罗斯方块：已暂停')
                    else:
                        pygame.display.set_caption('俄罗斯方块')

            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    gameTetris.change()

        keyPressList = pygame.key.get_pressed()

        if keyPressList[K_DOWN]:
            gameTetris.moveDown()
        elif keyPressList[K_LEFT]:
            gameTetris.moveLeft()
        elif keyPressList[K_RIGHT]:
            gameTetris.moveRight()

        screen.fill((0, 0, 0))
        drawMap()
        pygame.display.update()
        count += 1

        pygame.time.Clock().tick(10)


if __name__ == '__main__':
    my_game()
