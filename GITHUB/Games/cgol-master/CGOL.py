import sys
import timeit
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication,QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt

#board input should be a list of living cells
class Board(QWidget): #implements game rules
     #create a list of life forms and give them a location on the 2d grid
    def __init__(self,i,j,currentGen):
        self.lifelist = []
        self.currentGen = currentGen
        self.i = i
        self.j = j
        self.nextGen = []
        super(Board,self).__init__()
        layout = QtWidgets.QGridLayout()
        layout.setSpacing(1)
        for i in range(self.i):
            row = []
            for j in range(self.i):
                lifeform = LifeForm()
                lifeform.x = i
                lifeform.y = j
                row.append(lifeform)
                layout.addWidget(lifeform,i,j)
            self.lifelist.append(row)
        #self.lifelist[self.i][self.j].alive = True

        for x in range(self.i):
            for y in range(self.j):
                self.lifelist[x][y].alive = currentGen[x][y]
        self.setGeometry(0,0,QDesktopWidget().screenGeometry().height(),QDesktopWidget().screenGeometry().height())
        self.setLayout(layout)

        self.show()
        print(self.numNeighbors(self.lifelist[2][2],self.lifelist))
        #print(self.numNeighbors(self.lifelist[3][3]))
        #self.aliveNext()
        time = QtCore.QTimer(self)
        time.timeout.connect(self.createNextGen)
        time.start(1000)


#"""The previous part of the program deals with initially painting the cells onto the board and dealing with
#the input values in the initial program. The next part of the program deals with updating the cells based on the rules
#of conways game"""

    def numNeighbors(self,lifeform,lifelist):
     # def numNeighbors(self.x, self.y)
        numNalive = 0
        y = lifeform.y
        x = lifeform.x
        #print(x,y)
        neighbors = (
            (-1,-1),(-1,0),(-1,1),
            (0,-1),   (0,1),
            (1,-1),(1,0),(1,1)
        )
        adjacent = 0
        for dx,dy in neighbors:
             #if the piece is on the board 0<piece<size
                #and x+dx, y+dy.alive is true then
                    #numalive +=1
            if 0 <= x+dx < self.i and 0 <=y+dy< self.j and lifelist[x+dx][y+dy].alive == True:
                numNalive+=1
        return numNalive

#conways if statement
    def nextState(self,currentState, n):#def nextState(state, numNalive)
        nextState = True
        if currentState == True:#if cell is alive
            if n < 2 or n > 3:
        #if numNalive < 2 or numNalive > 3
            #cell = dead
                nextState = False
            elif n ==2 or n == 3: nextState = True
        elif currentState == False:
            #print(currentState)
            if n == 3:
                nextState = True
            else:
                nextState = False
        return nextState

    def createNextGen(self): #find the newstate of all the pieces on the board

        #iterate thru each piece
         for row in range(0,self.i-1,1):
             for col in range(0,self.j-1,1):
            #find the number of neighbors for the piece
                numAlive = self.numNeighbors(self.lifelist[row][col],self.lifelist)
                print(self.lifelist[row][col].x,self.lifelist[row][col].y,numAlive)

                self.currentGen[row][col] = self.nextState(self.lifelist[row][col].alive, numAlive)
                print(self.lifelist[row][col].alive)
            #change its state
         self.animateNextGen()
        #call animation function
    def animateNextGen(self): #take pieces and repaint all of them
        for row in range(0,self.i-1,1):
            for col in range(0,self.j-1,1):
                self.lifelist[row][col].alive = self.currentGen[row][col]
                self.lifelist[row][col].repaint()
        #iterate thru all the pieces and repaint them
class LifeForm(QWidget): #creates and controls anything related to lifeform also paints life form on screen
    def __init__(self):
        super().__init__()
        self.alive = False
        self.x
        self.y
    def paintEvent(self,e):
        if self.alive == False:
            SCREENW = QDesktopWidget().screenGeometry(-1).width()
            SCREENH = QDesktopWidget().screenGeometry(-1).height()
            painter = QPainter(self)
            brush = QBrush()
            brush.setColor(QColor('black'))
            brush.setStyle(Qt.SolidPattern)
            rect = QtCore.QRect(0,0,SCREENH,SCREENH)
            painter.fillRect(rect,brush)
        else:
            SCREENW = QDesktopWidget().screenGeometry(-1).width()
            SCREENH = QDesktopWidget().screenGeometry(-1).height()
            painter = QPainter(self)
            brush = QBrush()
            brush.setColor(QColor('white'))
            brush.setStyle(Qt.SolidPattern)
            rect = QtCore.QRect(0, 0, SCREENH, SCREENH)
            painter.fillRect(rect, brush)


if __name__ == "__main__":
#GLOBALS FIRST
    N = 50

    #When i create a board it should create all the lifeforms for me and tell them to print themselves on the screen

    app = QApplication(sys.argv)
   # print('no')
    x = True
    i=0
    currentGen = [[False, False, False, False,False,False],[False,False,False, True, False, False],[False,False,False,True,False,False],[False,False,False,True,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False]]
    b = Board(6, 6, currentGen)
    sys.exit(app.exec_())

#the lifeform alive statuses must be updated when the current gen is being shown. then the timer is activated and the lifeforms
#will get repainted
