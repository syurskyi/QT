from PyQt5.QtWidgets import *
from Ball import SLICE
import sys
# from canvas
# from PyQt5 import
import time
import threading
import functools

from FileWidget import FileWidget
from ProcessWidget import ProcessWidget
def sync(lock):
    def syncWithLock(fn):
        def newFn(*args, **kwargs):
            lock.acquire()
            try:
                return fn(*args, **kwargs)
            finally:
                lock.release()

        newFn.func_name = fn.func_name
        newFn.__doc__ = fn.__doc__
        return newFn

    return syncWithLock


lock = threading.Lock()




def async(func):

    @functools.wraps(func)

    def wrapper(*args, **kwargs):

        my_thread = threading.Thread(target=func, args=args, kwargs=kwargs)

        my_thread.start()
    return wrapper
from math import *
from Clicked_Label import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QStackedWidget, QStackedLayout
from MainData import MainData
from Ball import Ball



# from __future__  import division 如果是python2就需要
class MyWidget(QWidget):
    clicked = pyqtSignal()

    def __init__(self):
        self.collideTimes=0
        self.score=0
        self.n1=0
        self.n2=0
        self.mesc=15
        self.step = 0.02
        super().__init__()
        self.mec=0
        self.i = 0
        self.BallList = []
        self.power = 0
        # baseX = 100
        # baseY = 200
        # for i in range(2):
        #     self.AddBall()
        # self.FormBallList( l=[[baseX, baseY], [baseX+20, baseY]])
        self.timer = QTimer(self)
        # self.timer.start(20)
        self.count = 0
        self.timer.timeout.connect(self.update)


        # self.timer.start(1000)
        self.show()

    def startCount(self):
        self.timer.start(self.mesc)

    def showNum(self):
        self.count += 1
        # print(self.count)

    def AddBall(self):
        self.BallList.append(Ball())

    def DrawBallList(self):

        # print(len(self.BallList))
        # painter.drawPixmap(0, 100.5, 20, 20, QPixmap("images\\1.png"))
        # painter.drawPixmap(0, 200, 20, 20, QPixmap("images\\1.png"))
        pass

    # def closeEvent(self, a0:QCloseEvent):
    #     a0.accept()
    def Move(self):
        ctype = 0
        step = 0
        sb1 = sb2 = None
        self.BallList[0].setProperty(x=100, y=100, vx=1, vy=0)
        self.BallList[1].setProperty(x=100, y=200, vx=-1, vy=0)
        while (step < SLICE):
            mstep = SLICE - step
            for i in range(len(self.BallList)):
                b1 = self.BallList[i]
                if b1 == None:
                    continue
                for j in range(i + 1, len(self.BallList)):
                    b2 = self.BallList[j]
                    if b2 == None:
                        continue
                    slice = b1.Cyclic_frame_test(b=b2)
                    if mstep > slice:
                        mstep = slice
                        ctype = 1
                        sb1 = b1
                        sb2 = b2
        for i in range(len(self.BallList)):
            if self.BallList[i] != None:
                self.BallList[i].update(mstep)
        if ctype == 1:
            sb1.Collision_Detection(sb2)
        step += mstep
        # print(step)
        # ctype=0
        # step=0
        # record=0
        # mstep=0
        # number=0
        # slice=0
        # request=0
        # sb1=sb2=Ball()
        # while(step<SLICE):
        #     mstep=SLICE-step
        #     ctype=0
        #     sb1=sb2=None
        #     b1=self.BallList[0]
        #     b2=self.BallList[1]
        #     slice=b1.Cyclic_frame_test(x2=b2.x,y2=b2.y)
        #     if mstep>slice:
        #         mstep=slice
        #         ctype=1
        #         sb1=b1
        #         sb2=b2
        # step+=1

    def FormBallList(self, l):  # Form the shape of balls
        for i in range(len(self.BallList)):
            self.BallList[i].setProperty(x=l[i][0], y=l[i][1], vx=l[i][2], vy=l[i][3])

    def mousePressEvent(self, ev: QMouseEvent):
        # self.clicked.emit()#signal emit
        self.dragstart = ev.pos()
        self.clicked.emit()  # signal emit

    def mouseReleaseEvent(self, ev: QMouseEvent):

        self.Pos = ev.pos()
        print('Pos:', ev.pos())

        self.startCount()
        self.clicked.emit()  # signal emit


        #以下是初始化撞击球的速度，方向
        v = self.power/5

        # print('power:-------------------#######################################---------------', self.Pos,
        #       self.BallList[0].x, self.BallList[0].y, v)
        self.px = (self.Pos.x() - self.BallList[0].x) / sqrt(
            pow(self.Pos.x() - self.BallList[0].x, 2) + pow(self.Pos.y() - self.BallList[0].y, 2))
        self.py = (self.Pos.y() - self.BallList[0].y) / sqrt(
            pow(self.Pos.x() - self.BallList[0].x, 2) + pow(self.Pos.y() - self.BallList[0].y, 2))

        # print(self.px, self.py)
        self.BallList[0].setProperty(x=self.BallList[0].x, y=self.BallList[0].y, vx=v * self.px, vy=v * self.py)
        # self.repaint()

    def closeEvent(self, a0: QCloseEvent):
        a0.accept()


    def update(self):
        ctype=0
        CWBALL=1
        CWWALL=2
        # b1=b2=None
        # print('update')
        super().update()
        self.mec+=1
        # self.BallList[0].setProperty(vx=1,vy=0)
        # self.BallList[1].setProperty(vx=-1,vy=0)
        for i in range(len(self.BallList)):
            # if self.BallList[i].Is_Stayed():
            #     continue
            for j in range(i+1,len(self.BallList)):
                # b2= self.BallList[j]

                if self.BallList[i].changesHole()==True:
                    self.BallList.remove(self.BallList[i])
                    # self.score-=1
                    if i!=0:
                        self.score += 1
                    else:
                        self.score-=1
                    return
                if self.BallList[j].changesHole()==True:
                    self.BallList.remove(self.BallList[j])
                    if j!=0:
                        self.score += 1
                    else:
                        self.score-=1
                    return
                self.BallList[i].changesWall(width=600, height=300)
                self.BallList[j].changesWall(width=600, height=300)
                # if self.BallList[j].Is_Stayed():
                #     continue
                l=sqrt(pow( self.BallList[i].x- self.BallList[j].x,2)+pow( self.BallList[i].y- self.BallList[j].y,2))
                if l<=20:

                    # print(self.collideTimes)
                    self.BallList[i].Collision_Detection(self.BallList[j])
                self.BallList[i].update(step=self.step)
                self.BallList[j].update(step=self.step)


        for i in range(len(self.BallList)):
            self.collideTimes+=self.BallList[i].collideTimes
        print(self.collideTimes)
        self.collideTimes=0
        # outer:



        # if ctype==CWBALL:
        #     self.BallList[b1].Collision_Detection(b2)

        # elif ctype==CWWALL:
        #     self.BallList[b1].changesWall(width=600, height=300)
            # self.BallList[b1].update(step=0.1)




        # self.BallList[0].update(step=5)
        # print(self.BallList[0].vx, '--------3123131-------------------------------')
        # self.BallList[0].setProperty(x=self.BallList[0].x+10, y=self.BallList[0].y,vx=0,vy=0)
        # self.BallList[1].setCoordinate(x=self.BallList[1].x-10, y=self.BallList[0].y)
        # self.Move()
        # painter = QPainter(self)
        # painter.drawPixmap(0, 78, 600, 300, QPixmap("images\\table.png"))
        # if len(self.BallList) == 0:
        #     return None
        # for i in range(len(self.BallList)):
        #     # print(self.BallList[i].x,self.BallList[i].y)
        #     painter.drawPixmap(self.BallList[i].x, self.BallList[i].y, 20, 20, QPixmap("images\\1.png"))
        #     self.show()

    def paintEvent(self, a0: QPaintEvent):
        self.i += 1
        # print("paintEvent", self.i)
        painter = QPainter(self)
        painter.drawPixmap(0, 78, 600, 300, QPixmap("images\\table.png"))
        # painter.drawPixmap(self.BallList[0].x, self.BallList[0].y, 20, 20, QPixmap("images\\1.png"))
        # print(len(self.BallList))
        if len(self.BallList) == 0:
            return None
        for i in range(len(self.BallList)):
            # painter = QPainter(self)
            # print(self.BallList[i].x, self.BallList[i].y)
            if i==0:
                painter.drawPixmap(self.BallList[i].x - 10, self.BallList[i].y - 10, 20, 20, QPixmap("images\\0.png"))
            else:
                painter.drawPixmap(self.BallList[i].x-10, self.BallList[i].y-10, 20, 20, QPixmap("images\\1.png"))
        # self.show()
        # self.BallList[i].Draw(w=painter,QP=QPixmap("images\\1.png"))


class MyLayout(QGridLayout):
    def __init__(self):
        super().__init__()
    # def addWidget(self):


class App(QMainWindow, MainData):
    """
    @
    """

    def __init__(self):
        self.action = dict()
        self.cnavas = 0
        self.data = dict()
        self.balltest = Ball()

        self.Pos = None

        QMainWindow.__init__(self)
        QToolTip.setFont(QFont('SansSerif', 10))  # 设置字体
        self.setWindowTitle('BillardBall')
        self.setGeometry(100, 100, 900, 550)

        self.actionLoad()
        self.menuBarLoad()
        self.getImage()
        self.widget = None
        self.step = 10
        self.timer = QBasicTimer()
        # self.timer.start(20, self)
        # self.show()

    def actionLoad(self):
        self.action["BillardBall"] = QAction('Billard Ball', self)
        self.action["BillardBall"].setShortcut('F3')
        self.action["BillardBall"].setStatusTip('Billard Ball')
        self.action["BillardBall"].triggered.connect(self.BillardBall)

        self.action["ProcessManager"] = QAction('ProcessManager', self)
        self.action["ProcessManager"].setShortcut('F4')
        self.action["ProcessManager"].setStatusTip('ProcessManager')
        self.action["ProcessManager"].triggered.connect(self.ProcessManager)

        self.action["FileManager"] = QAction('FileManager', self)
        self.action["FileManager"].setShortcut('F5')
        self.action["FileManager"].setStatusTip('FileManager')
        self.action["FileManager"].triggered.connect(self.FileManager)



    def FileManager(self):
        self.File_widget= FileWidget()
    def ProcessManager(self):
        self.process_widget = ProcessWidget()

    def menuBarLoad(self):
        self.statusBar()
        menubar = self.menuBar()
        statisticsMenu = menubar.addMenu('&Game')
        statisticsMenu.addAction(self.action["BillardBall"])
        statisticsMenu2= menubar.addMenu('&Explorer')
        statisticsMenu2.addAction(self.action["ProcessManager"])
        statisticsMenu2.addAction(self.action["FileManager"])
    def controlLayout(self, layout=None, name=None, var=None, position=None, signal=None):
        """
        control layout
        :param layout: GridLayout = QGridLayout()
        :param name: name of control, name is a string
        :param var: var is a dict
        :param position: position is a list with 4 numeric
        :param signal: signal function
        """
        if name == "RedBall":
            pixmap = QPixmap("./images/1.png")
            for j in range(0, len(position)):
                self.control[name].append(Ball())
                self.control[name][-1].setPixmap(pixmap)
                self.control[name][-1].setAlignment(Qt.AlignCenter)

                # self.control[name][-1].setWindowFlags(Qt.WindowStaysOnTopHint)
                # self.control[name][-1].set
                # print( self.control['Clickable_Lable'][-1])
                # noinspection PyArgumentList
                # layout.addWidget(self.control[name][-1])
                self.control[name][-1].setGeometry(position[j][0], position[j][1], position[j][2], position[j][3])
                # print(self.control[name][-1])
                # print(position[j][0])
                if signal is not None:
                    self.control[name][-1].clicked.connect(signal)
        if name == "Clickable_Lable":
            pixmap = QPixmap("./images/table.png")
            for j in range(0, len(position)):
                self.control[name].append(Clickable_QLabel())
                self.control[name][-1].setPixmap(pixmap)
                self.control[name][-1].setAlignment(Qt.AlignCenter)
                # print( self.control['Clickable_Lable'][-1])
                # noinspection PyArgumentList
                sWidget = QStackedWidget(self.control[name][-1])
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                # print(position[j][0])
                if signal is not None:
                    self.control[name][-1].clicked.connect(signal)
        # [[0, 0, 1, 1], [0, 2, 1, 1], [0, 4, 1, 1], [0, 6, 1, 1]]

        if name == "QProgressBar":
            for j in range(0, len(position)):
                self.control[name].append(QProgressBar())
                self.control[name][-1].setValue(self.step)
                self.control[name][-1].setAlignment(Qt.AlignCenter)
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                if signal is not None:
                    self.control[name][-1].clicked.connect(signal)

        if name == "QLabel":
            # var = {"text": [string]}
            for j in range(0, len(position)):
                self.control[name].append(QLabel(var["text"][j]))
                self.control[name][-1].setAlignment(Qt.AlignCenter)
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                # print(position[j][0])
        # [[0, 0, 1, 1], [0, 2, 1, 1], [0, 4, 1, 1], [0, 6, 1, 1]]
        if name == "QTabWidget":
            # var = {"text": [[string]], "widget": [[PyQt5.QtWidgets.QWidget]]}
            for j in range(0, len(position)):
                self.control[name].append(QTabWidget())
                for k in range(0, len(var["text"][j])):
                    self.control[name][-1].addTab(var["widget"][j][k], self.tr(var["text"][j][k]))
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])

        if name == "QPushButton":
            # var = {"text": [string]}
            for j in range(0, len(position)):
                self.control[name].append(QPushButton(var["text"][j]))
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])
                if signal is not None:
                    self.control[name][-1].clicked.connect(signal)

        if name == "QTextEdit":
            # var = {"text": [[string]]}
            for j in range(0, len(position)):
                self.control[name].append(QTextEdit())
                if len(var["text"]) != 0:
                    if len(var["text"][j]) != 0:
                        for line in var["text"][j]:
                            self.control[name][-1].append(line)
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[j][0], position[j][1], position[j][2], position[j][3])

        if name == "QTableWidget":
            # var = {"headerLabels": [[string]], "data": [numpy.array]}
            for i in range(0, len(position)):
                self.control[name].append(QTableWidget(1, 1))
                if len(var["headerLabels"]) != 0:
                    if len(var["headerLabels"][i]) != 0:
                        self.control[name][-1].setColumnCount(len(var["headerLabels"][i]))
                        self.control[name][-1].setHorizontalHeaderLabels(var["headerLabels"][i])
                if len(var["data"]) != 0:
                    if len(var["data"][i]) != 0:
                        row, column = var["data"][i].shape
                        self.control[name][-1].setRowCount(row)
                        self.control[name][-1].setColumnCount(column)
                        for j in range(0, row):
                            for k in range(0, column):
                                newItem = QTableWidgetItem(str(var["data"][i][j][k]))
                                self.control[name][-1].setItem(j, k, newItem)
                self.control[name][-1].resizeColumnsToContents()
                # noinspection PyArgumentList
                layout.addWidget(self.control[name][-1], position[i][0], position[i][1], position[i][2], position[i][3])

    def timerEvent(self, e):
        if self.control["QLabel"][0]!=None:
            self.control['QLabel'][0].setText(str(self.widget.score))
        self.repaint()
        # self.widget.repaint()
        # self.widget.show()
        # print("TIME EVENT APP")
        if self.step >= 100:
            # self.timer.stop()
            # self.qbtn.setText('Fuck')
            self.temp = self.timerEvent
            self.timerEvent = self.timerEvent2
        self.step += 5
        self.control['QProgressBar'][-1].setValue(self.step)
        self.widget.power = abs(self.step)
        # self.update()

    def setScores(self, val: int):
        self.control['QLabel'][0].setText('分数:' + str(val))

    def timerEvent2(self, e):
        if self.step < 0:
            self.timerEvent = self.temp
        self.step -= 5
        self.control['QProgressBar'][-1].setValue(self.step)
        self.widget.power = abs(self.step)

    def gameStart(self):
        self.step = 0
        self.control['QProgressBar'][-1].setValue(self.step)

    def ButtonClickedSignal(self):
        sender = self.sender()
        self.gameStart()
        # self.update()

    def TableSignal(self):
        if self.timer.isActive():
            self.timer.stop()
            self.control['QPushButton'][0].setText('Start')
        else:
            self.timer.start(100, self)
            self.control['QPushButton'][0].setText('Stop')
            self.step=0

    def BillardBall(self):
        self.currentImage = "BillardBall"
        self.controlClear()

        # layout
        layout = MyLayout()
        layout2 = QStackedLayout()

        layout.setSpacing(10)

        text = ['开始']
        position = [[0, 0, 1, 1]]  # , [0, 2, 1, 1], [0, 4, 1, 1], [0, 6, 1, 1]
        self.controlLayout(layout=layout, name="QPushButton", var={"text": text}, position=position,
                           signal=self.ButtonClickedSignal)

        text = ['分数:', '力量：']
        position = [[0, 2, 1, 1], [0, 4, 1, 1]]
        self.controlLayout(layout=layout, name="QLabel", var={"text": text}, position=position, signal=None)

        text = ['ProgressBar']
        position = [[0, 6, 1, 1]]
        self.controlLayout(layout=layout, name="QProgressBar", var={"text": text}, position=position, signal=None)

        position = [[100, 100], [100, 110], [110, 110], [110, 100]]
        # QWidget
        # BallTableWidget=QWidget()
        # BallTableWidget
        # layout.addWidget()

        # setBallList

        #
        # self.setObjectName("mainWindow");
        # self.setStyleSheet(r"#mainWindow{border-image:url(C:\Users\Administrator\PycharmProjects\BB2_test\images\table.png);}")
        # Table
        # text=['']
        # position=[[2,2,2,2]]
        # self.controlLayout(layout=layout, name="Clickable_Lable", var={"text": text}, position=position, signal=self.TableSignal)

        # balltest
        # text = ['']
        # position = [[243,172,20,20]]
        # self.controlLayout(layout=layout, name="RedBall", var={"text": text}, position=position,signal=None)
        # noinspection PyArgumentList
        baseX = 300
        baseY = 228
        vx = 0
        vy = 0
        self.widget = MyWidget()
        for i in range(4):
            self.widget.AddBall()
        self.widget.FormBallList(
            l=[[141, 228, 0, 0],[baseX,baseY,0,0], [baseX + 10 * sqrt(3), baseY - 10, 0, 0],[baseX + 10 * sqrt(3), baseY +10, 0, 0]])
        self.widget.setLayout(layout)
        self.widget.clicked.connect(self.TableSignal)
        self.setCentralWidget(self.widget)
        # print('Hi')
        self.statusBar().showMessage('Ready')

    def repaint(self):
        # print("MainWidget repaint")
        pass

    def paintEvent(self, a0: QPaintEvent):
        # print('app SHOW-----------')

        self.show()

        # self.widget.repaint()

    def orthogonalTableImageSignal(self):
        pass

    def showOpenDialog(self):
        pass

    def getImage(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
