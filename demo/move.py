# 创作者 马如云
# ai移动类
from demo.point import Point
from demo.operation import Operation
from demo.screenshot import  screenshot

class Move:

    op=Operation()#获取一个操作
    If_alive=False
    If_find_Destination=False

    def __init__(self):
        return
    def findpath(self,player:Point,goal:Point):#从player到目的地goal的算法
        dir = goal-player
        if abs(dir.x)<0 and abs(dir.y)<0:
            if goal.x == 0 and goal.y == 0:
                self.op.doNothing()
            elif abs(dir.x) > abs(dir.y) and dir.x > 0:
                self.op.goRight()
            elif abs(dir.x) > abs(dir.y) and dir.x < 0:
                self.op.goLeft()
            elif abs(dir.x) < abs(dir.y) and dir.y > 0:
                self.op.goDown()
            elif abs(dir.x) < abs(dir.y) and dir.y < 0:
                self.op.goUp()
        else:
            if goal.x == 0 and goal.y == 0:
                self.op.doNothing()
            elif abs(dir.x) > abs(dir.y) and dir.x > 0:
                self.op.goRightWithSpace()
            elif abs(dir.x) > abs(dir.y) and dir.x < 0:
                self.op.goLeftWithSpace()
            elif abs(dir.x) < abs(dir.y) and dir.y > 0:
                self.op.goDownWithSpace()
            elif abs(dir.x) < abs(dir.y) and dir.y < 0:
                self.op.goUpWithSpace()

    def If_safe(self):
        return
    def AI_move(self):#移动主程序
        player,destination=self.getPosition()
        self.findpath(player,destination)#直接移动到目的地
        return
    def getPosition(self):#获取玩家和目的地坐标
        output = open('data.txt', 'w')
        img = screenshot()  # 截图
        img_array = img.load()  # 获取像素点信息
        w, h = img.size
        # 用来记录所求物体的左上像素点
        first1 = False
        first2 = False
        # 分别为左上和右下坐标
        r1 = Point(0, 0)
        r2 = Point(0, 0)
        d1 = Point(0, 0)
        d2 = Point(0, 0)
        for i in range(0, h):
            for j in range(0, w):
                pixel = img_array[j, i]
                #输出到文件


                if pixel == (0, 254, 254):
                    #print('(', end="", file=output)
                    #print(j, end="", file=output)
                    #print(',', end="", file=output)
                    #print(i, end="", file=output)
                    #print(')', end=" ", file=output)
                    #print(pixel, file=output)
                    if first1 == False:  # 第一次找到的点即为左上坐标
                        r1 = Point(j, i)
                        first1 = True
                    r2 = Point(j, i)  # 最后一次找到的即为右下坐标
                if pixel == (213, 245, 252):
                    if first2 == False:
                        d1 = Point(j, i)
                        first2 = True
                    d2 = Point(j, i)
        player = (r2 + r1).getmidpoint()
        destination = (d2 + d1).getmidpoint()
        self.If_alive=player.If_zero()
        self.If_find_Destination=destination.If_zero()
        return player,destination



