from Clicked_Label import Clickable_QLabel
from math import *
from PyQt5.Qt import *
from PyQt5.QtCore import *

OFFSET = 12
SLICE = 120
EPS = 1


class Ball(QLabel):
    def __init__(self) -> object:
        super().__init__()
        self.collideTimes = 0
        self.x = 44
        self.y = 270
        self.vx = 0
        self.vy = 0
        self.color = 'Red'
        self.radian = 10
        # if self.color=='Red':
        #     self.setPixmap(QPixmap(".\images\1.png"))
        # else:
        #     self.setPixmap(QPixmap(".\images\0.png"))

    # def Draw(self,w:QPainter,QP:QPixmap):
    #     w.drawPixmap(self.x, self.y, 20, 20, QP)
    def timerEvent(self, e: QTimerEvent):
        self.repaint()

    # 设置坐标
    def setCoordinate(self, x: float, y: float):
        self.x = x
        self.y = y
        self.px = 0
        self.py = 0

    def setProperty(self, x: float, y: float, vx: float, vy: float):
        if x != None:
            self.x = x
        if y != None:
            self.y = y
        if vx != None:
            self.vx = vx
        if vy != None:
            self.vy = vy
        self.px = 0
        self.py = 0

    def update(self, step: int):

        vx_t = vy_t = x_t = y_t = 0.0
        if self.Is_Stayed() == True:
            self.px = self.py = 0
        else:
            self.px = self.vx / (sqrt(pow(self.vx, 2) + pow(self.vy, 2)))
            self.py = self.vy / (sqrt(pow(self.vx, 2) + pow(self.vy, 2)))

        # print("self.px:***********************************",self.px)
        # print("self.py************************************",self.py)
        vx_t = self.vx - step * self.px
        # print("vx_t:--------------------------------------------",vx_t)
        vy_t = self.vy - step * self.py
        # print("vy_t:--------------------------------------------", vy_t)
        if vx_t * self.vx <= 0:
            vx_t = 0.0
        if vy_t * self.vy <= 0:
            vy_t = 0.0
        x_t = self.x + (self.vx + vx_t) / 2.0
        y_t = self.y + (self.vy + vy_t) / 2.0
        self.setProperty(x=x_t, y=y_t, vx=vx_t, vy=vy_t)
        # self.Collision_Dectection_Wall(width=600, height=300)
        # self.BallList[j].Collision_Dectection_Wall(width=600, height=300)
    # 粘连检测
    def Is_Adhered(self, x2: float, y2: float):
        dist = sqrt(pow(self.x - x2, 2) + pow(self.y - y2, 2))
        return dist < 2 * self.radian

    # 静止检验
    def Is_Stayed(self):
        if abs(self.vx) <= EPS and abs(self.vy) <= EPS:
            self.vx = 0
            self.vy = 0
            return True
        else:
            return False

    # 循环帧检验
    def Cyclic_frame_test(self, b):
        step = 1
        if self.Is_Stayed() == True and b.Is_Stayed() == True:
            return SLICE
        if self.Is_Stayed() == True:
            self.px = 0
            self.py = 0
        else:
            px = self.vx / sqrt(pow(self.vx, 2) + pow(self.vy, 2))  # cosθ
            py = self.vy / sqrt(pow(self.vx, 2) + pow(self.vy, 2))  # sinθ
        # 客球：
        if b.Is_Stayed() == True:
            b.px = 0
            b.py = 0
        else:
            px2 = b.vx / sqrt(pow(b.vx, 2) + pow(b.vy, 2))  # cosθ
            py2 = b.vy / sqrt(pow(b.vx, 2) + pow(b.vy, 2))  # sinθ

        while (step < SLICE):
            vx_t = self.vx - step * px
            vy_t = self.vy - step * py
            if ((vx_t > 0 and self.vx < 0) or (vx_t < 0 and self.vx > 0)):  # 如果减速过头，则将速度置为0
                vx_t = 0.0
            if ((vy_t > 0 and self.vy < 0) or (vy_t < 0 and self.vy > 0)):
                vy_t = 0.0
            self.x = self.x + step * (self.vx + vx_t) / 2000  # 末位置=初始位置+位移量(平均速度*时间帧)，除以1000是为了缩小到窗口尺度下
            self.y = self.y + step * (self.vy + vy_t) / 2000
            # 客球
            vx2_t = b.vx - step * px2
            vy2_t = b.vy - step * py2
            if ((vx2_t > 0 and b.vx < 0) or (vx2_t < 0 and b.vx > 0)):
                vx2_t = 0.0
            if ((vy2_t > 0 and b.vy < 0) or (vy2_t < 0 and b.vy > 0)):
                vy2_t = 0.0
            b.x = b.x + step * (b.vx + vx2_t) / 2000
            b.x = b.y + step * (b.vy + vy2_t) / 2000

            if self.Is_Adhered(x2=b.x, y2=b.y) == True:
                break  # 如果已经触碰，则说明碰撞，跳出循环帧检验
            step += 1  # 否则进行下一帧的帧检验
        return step  # 返回两球碰撞需要的帧数

    # 碰撞检验:小球
    def Collision_Detection(self, b):
        self.collideTimes +=1
        print('fuck')
        px = (b.x - self.x) / sqrt(pow(b.x - self.x, 2) + pow(b.y - self.y, 2))
        py = (b.y - self.y) / sqrt(pow(b.x - self.x, 2) + pow(b.y - self.y, 2))
        ux1 = (px * self.vx + py * self.vy) * px  # 主球在两球圆心连线方向分速度的水平分速度
        uy1 = (px * self.vx + py * self.vy) * py  # 主球在两球圆心连线方向分速度的竖直分速度
        ux2 = self.vx - ux1  # 假设主客球质量相同 ，符合动能定理m*vx=m*ux1(客球)+m*ux2(主球),速度交换
        uy2 = self.vy - uy1

        # 同理客球
        ux3 = px * (px * b.vx + py * b.vy)
        uy3 = py * (px * b.vx + py * b.vy)
        ux4 = b.vx - ux3
        uy4 = b.vy - uy3

        self.vx = ux2 + ux3  # 矢量叠加
        self.vy = uy2 + uy3

        b.vx = ux1 + ux4
        b.vy = uy1 + uy4

        E = 10
        E2 = 200.0

        # 防止粘连：如果球心距离小于半径，则让其退回至球心距离大于或等于半径的位置
        step = 1
        while (True):
            self.x = self.x + (step * self.vx) / E
            self.y = self.y + (step * self.vy) / E
            b.x = b.x + (step * b.vx) / E
            b.y = b.y + (step * b.vy) / E
            if self.Is_Adhered(x2=b.x, y2=b.y) == False:
                break
            if self.Is_Stayed() == True and b.Is_Stayed() == True and self.Is_Adhered(x2=b.x, y2=b.y) == True:
                p1 = (self.x - b.x) / sqrt(pow(b.x - self.x, 2) + pow(b.y - self.y, 2))
                p2 = (self.y - b.y) / sqrt(pow(b.x - self.x, 2) + pow(b.y - self.y, 2))
                p3 = (b.x - self.x) / sqrt(pow(b.x - self.x, 2) + pow(b.y - self.y, 2))
                p4 = (b.y - self.y) / sqrt(pow(b.x - self.x, 2) + pow(b.y - self.y, 2))
                while (True):
                    self.x = self.x + (step * p1) / E2
                    self.y = self.y + (step * p2) / E2
                    b.x = b.x + (step * p3) / E2
                    b.y = b.y + (step * p4) / E2
                    if self.Is_Adhered(x2=b.x, y2=b.x) == False:
                        return
                    step += 1
            # step+=1

    # 碰撞检测：墙
    def Collision_Dectection_Wall(self, width: float, height: float):

        a=0
        if self.x - 5 <= 0 + OFFSET or self.x + 5 >= width - OFFSET:
            # self.vx=-self.vx
            # self.vy=self.vy
            a+=1
        if self.y - 5 <= 78 + OFFSET or self.y + 5 >= height+78 - OFFSET:
            # self.vx=self.vx
            # self.vy=-self.vy
            a+=1
        if a>0:
            return True
        else:
            return False

    def changesHole(self):
        if sqrt(pow(self.x-18,2)+pow(self.y-93,2))<=10*sqrt(2):
            return True
        elif sqrt(pow(self.x-300,2)+pow(self.y-88,2))<=10*sqrt(2):
            return True
        elif sqrt(pow(self.x-579,2)+pow(self.y-93,2))<=10*sqrt(2):
            return True
        elif sqrt(pow(self.x-21,2)+pow(self.y-361,2))<=10*sqrt(2):
            return True
        elif sqrt(pow(self.x-301,2)+pow(self.y-366,2))<=10*sqrt(2):
            return True
        elif sqrt(pow(self.x-580,2)+pow(self.y-362,2))<=10*sqrt(2):
            return True
        else:
            return False
    def changesWall(self, width: float, height: float):

        if self.x - 10 <= 0 + OFFSET or self.x +10 >= width - OFFSET:
            self.vx = -self.vx
            self.vy = self.vy
            self.collideTimes += 1
        if self.y - 10 <= 78 + OFFSET or self.y + 10 >= height + 78 - OFFSET:
            self.vx = self.vx
            self.vy = -self.vy
            self.collideTimes += 1
        # while (True):
        #     if self.x<=0+OFFSET and self.x>=0:
        #         self.x+
        #     elif self.x>=width-OFFSET and self.x<=width:
        # 以下是防止粘连在墙上
        if self.x <= 0 + OFFSET:
            while (True):
                self.x += 0.5
                if self.x > 0 + OFFSET:
                    break;
        if self.x >= width - OFFSET:
            while (True):
                self.x -= 0.5
                if self.x <= width - OFFSET:
                    break;
        if self.y <= 78 + OFFSET:
            while (True):
                self.y += 0.5
                if self.y > 78 + OFFSET:
                    break;
        if self.y >= height + 78 - OFFSET:
            while (True):
                self.y -= 0.5
                if self.y < height + 78 - OFFSET:
                    break;


    # self.px = self.vx / sqrt(pow(self.vx, 2) + pow(self.vy, 2))
    # self.py = self.vy / sqrt(pow(self.vx, 2) + pow(self.vy, 2))

    def repaint(self):
        self.balltest.setGeometry(self.x1, self.y1, 20, 20)
