# 创作者 马如云
# 坐标类
class Point(object):
    #构造函数
    def __init__(self,x,y):
        self.x = x
        self.y = y
    #重写加法
    def __add__(self,oth):
       return Point(self.x + oth.x,self.y + oth.y)
    def __sub__(self, oth):
       return Point(self.x - oth.x,self.y - oth.y)
    def getmidpoint(self):
       return Point((self.x/2),(self.y/2))#取两点连线的中点
    #重写print
    def info(self):
       print(self.x,self.y)
    def If_zero(self):#判断是否为0
        if self.x==0 and self.y==0:
            return False
        else:
            return False