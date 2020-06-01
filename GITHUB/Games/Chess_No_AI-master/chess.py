import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon
import os




class ChetoTam(QMainWindow):
    whiteKingTurn , blackKingTurn = False,False
    rocks=[False,False,False,False]
    way = os.getcwd().replace("\\","/")
    last = 0
    numb = 0
    turn = 0
    nations = ['white', 'black']
    chosen = False
    initialData = [
        ['blackrock', 'blackkon', 'blackofic', 'blackquin', 'blackking', 'blackofic', 'blackkon', 'blackrock', ],
        ['blackwar', 'blackwar', 'blackwar', 'blackwar', 'blackwar', 'blackwar', 'blackwar', 'blackwar', ],
        ['', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', ],
        ['', '', '', '', '', '', '', '', ],
        ['whitewar', 'whitewar', 'whitewar', 'whitewar', 'whitewar', 'whitewar', 'whitewar', 'whitewar', ],
        ['whiterock', 'whitekon', 'whiteofic', 'whitequin', 'whiteking', 'whiteofic', 'whitekon', 'whiterock', ]
        ]
    gameData = initialData
    whereCouldGo = [[False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False],
                    [False, False, False, False, False, False, False, False]
                    ]
    btn = []
    names=['rock','kon','ofic','quin','king']
    posibleTurns=\
    [
        [
            [
                [1, 0],
                [2, 0],
                [3, 0],
                [4, 0],
                [5, 0],
                [6, 0],
                [7, 0]
            ],
            [
                [-1, 0],
                [-2, 0],
                [-3, 0],
                [-4, 0],
                [-5, 0],
                [-6, 0],
                [-7, 0]
            ],
            [
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [0, 6],
                [0, 7]
            ],
            [
                [0, -1],
                [0, -2],
                [0, -3],
                [0, -4],
                [0, -5],
                [0, -6],
                [0, -7]
            ]
        ],
        [

                [[2, -1]],
                [[2, 1]],
                [[-2, -1]],
                [[-2, 1]],
                [[-1, 2]],
                [[1, 2]],
                [[-1, -2]],
                [[1, -2]],

        ],
        [
            [
                [1, 1],
                [2, 2],
                [3, 3],
                [4, 4],
                [5, 5],
                [6, 6],
                [7, 7]
            ],
            [
                [-1, 1],
                [-2, 2],
                [-3, 3],
                [-4, 4],
                [-5, 5],
                [-6, 6],
                [-7, 7]
            ],
            [
                [1, -1],
                [2, -2],
                [3, -3],
                [4, -4],
                [5, -5],
                [6, -6],
                [7, -7]
            ],
            [
                [-1, -1],
                [-2, -2],
                [-3, -3],
                [-4, -4],
                [-5, -5],
                [-6, -6],
                [-7, -7]
            ]


        ],
        [
            [
                [1, 1],
                [2, 2],
                [3, 3],
                [4, 4],
                [5, 5],
                [6, 6],
                [7, 7]
            ],
            [
                [-1, 1],
                [-2, 2],
                [-3, 3],
                [-4, 4],
                [-5, 5],
                [-6, 6],
                [-7, 7]
            ],
            [
                [1, -1],
                [2, -2],
                [3, -3],
                [4, -4],
                [5, -5],
                [6, -6],
                [7, -7]
            ],
            [
                [-1, -1],
                [-2, -2],
                [-3, -3],
                [-4, -4],
                [-5, -5],
                [-6, -6],
                [-7, -7]
            ],
            [
                [1, 0],
                [2, 0],
                [3, 0],
                [4, 0],
                [5, 0],
                [6, 0],
                [7, 0]
            ],
            [
                [-1, 0],
                [-2, 0],
                [-3, 0],
                [-4, 0],
                [-5, 0],
                [-6, 0],
                [-7, 0]
            ],
            [
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [0, 5],
                [0, 6],
                [0, 7]
            ],
            [
                [0, -1],
                [0, -2],
                [0, -3],
                [0, -4],
                [0, -5],
                [0, -6],
                [0, -7]
            ]
        ],
        [
            [[1, -1]],
            [[1, 1]],
            [[1, 0]],
            [[-1, 1]],
            [[-1, -1]],
            [[-1, 0]],
            [[0, -1]],
            [[0, 1]],
        ]

    ]
    whiteWarDoubleTurn,blackWarDoubleTurn=0,0
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(300, 300, 900, 900)
        self.setWindowTitle('chess v 0.01 pre-alpha')

        for i in range(64):
            self.btn.append(QPushButton(self))
            self.btn[-1].setGeometry((i % 8) * 100, (i // 8) * 100, 100, 100)
            self.btn[-1].clicked.connect(self.btnClicked)
            self.btn[-1].Numb = i
            a = self.way+'/img/black' + self.initialData[i // 8][i % 8] + '.png'
            b = self.way+'/img/white' + self.initialData[i // 8][i % 8] + '.png'
            if ((i % 2) + i // 8) % 2 == 1:
                self.btn[-1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % a)
            else:
                self.btn[-1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
        self.show()

    def btnClicked(self):
        sender = self.sender()
        numb = sender.Numb
        if (not self.chosen and self.gameData[sender.Numb // 8][sender.Numb % 8].find(self.nations[self.turn % 2]) != -1):
            self.vhereCouldWeGo(sender.Numb)
            self.last=sender.Numb
            self.chosen = True
        elif (self.chosen and self.whereCouldGo[sender.Numb // 8][sender.Numb % 8]):
            self._turn(sender.Numb)
            self.chosen = False
            self.turn += 1
        elif (self.chosen and self.last == sender.Numb):
            self.deleteTurn()
            self.chosen = False

    def vhereCouldWeGo( self,numb):
        a = self.way+'/img/blue' + self.gameData[numb // 8][numb % 8] + '.png'
        self.btn[numb].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % a)
        if self.gameData[numb // 8][numb % 8] == 'blackwar':
            if (numb // 8) + 1 < 8:
                if self.gameData[(numb // 8) + 1][numb % 8] == '' and self.CouldWeGoWithoutChah([1,0],numb,self.gameData)==True :
                    self.btn[numb + 8].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
                    self.whereCouldGo[(numb // 8) + 1][numb % 8]=True
            if numb // 8 ==1 :
                if self.gameData[(numb // 8) + 2][numb % 8] == '' and self.gameData[(numb // 8) + 1][numb % 8] == '' and self.CouldWeGoWithoutChah([2,0],numb,self.gameData)==True :
                    self.btn[numb + 16].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
                    self.whereCouldGo[(numb // 8) + 2][numb % 8] = True
            if (numb // 8) + 1 < 8 and (numb % 8) - 1 >= 0:
                if self.gameData[(numb // 8) + 1][(numb % 8) - 1].find('white') != -1 and self.CouldWeGoWithoutChah([1, -1],numb,self.gameData)==True :
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) + 1][(numb % 8) - 1] + '.png'
                    self.btn[numb + 8 - 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) + 1][(numb % 8)-1] = True
            if (numb // 8) + 1 < 8 and (numb % 8) + 1 < 8:
                if self.gameData[(numb // 8) + 1][(numb % 8) + 1].find('white') != -1  and self.CouldWeGoWithoutChah([1,1],numb,self.gameData)==True:
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) + 1][(numb % 8) + 1] + '.png'
                    self.btn[numb + 8 + 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) + 1][(numb % 8) + 1] = True
            if (numb // 8) + 1 < 8 and (numb % 8) - 1 >= 0:
                if self.whiteWarDoubleTurn==numb + 8 - 1 and self.CouldWeGoWithoutChah([1, -1],numb,self.gameData)==True :
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) + 1][(numb % 8) - 1] + '.png'
                    self.btn[numb + 8 - 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) + 1][(numb % 8)-1] = True
            if (numb // 8) + 1 < 8 and (numb % 8) + 1 < 8:
                if self.whiteWarDoubleTurn==numb + 8 + 1  and self.CouldWeGoWithoutChah([1,1],numb,self.gameData)==True:
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) + 1][(numb % 8) + 1] + '.png'
                    self.btn[numb + 8 + 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) + 1][(numb % 8) + 1] = True
        elif self.gameData[numb // 8][numb % 8] == 'whitewar':
            if (numb // 8) - 1 >= 0:
                if self.gameData[(numb // 8) - 1][numb % 8] == '' and self.CouldWeGoWithoutChah([-1, 0],numb,self.gameData)==True :
                    self.btn[numb - 8].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
                    self.whereCouldGo[(numb // 8) - 1][(numb % 8)] = True

            if numb // 8 == 6:
                if self.gameData[(numb // 8) - 2][numb % 8] == '' and self.gameData[(numb // 8) - 1][numb % 8] == '' and self.CouldWeGoWithoutChah([-2, 0],numb,self.gameData)==True :
                    self.btn[numb - 16].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
                    self.whereCouldGo[(numb // 8) - 2][(numb % 8) ] = True

            if (numb // 8) - 1 >= 0 and (numb % 8) - 1 >= 0:
                if self.gameData[(numb // 8) - 1][(numb % 8) - 1].find('black') != -1 and self.CouldWeGoWithoutChah([-1, -1],numb,self.gameData)==True:
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) - 1][(numb % 8) - 1] + '.png'
                    self.btn[numb - 8 - 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) - 1][(numb % 8) - 1] = True
            if (numb // 8) - 1 >= 0 and (numb % 8) + 1 < 8:
                if self.gameData[(numb // 8) - 1][(numb % 8) + 1].find('black') != -1 and self.CouldWeGoWithoutChah([-1,1],numb,self.gameData)==True:
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) - 1][(numb % 8) + 1] + '.png'
                    self.btn[numb - 8 + 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) - 1][(numb % 8) + 1] = True
            if (numb // 8) - 1 >= 0 and (numb % 8) - 1 >= 0:
                if self.blackWarDoubleTurn==numb - 8 - 1 and self.CouldWeGoWithoutChah([-1, -1],numb,self.gameData)==True:
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) - 1][(numb % 8) - 1] + '.png'
                    self.btn[numb - 8 - 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) - 1][(numb % 8) - 1] = True
            if (numb // 8) - 1 >= 0 and (numb % 8) + 1 <8 :
                if self.blackWarDoubleTurn==numb - 8 + 1 and self.CouldWeGoWithoutChah([-1, +1],numb,self.gameData)==True:
                    b = self.way+'/img/blue' + self.gameData[(numb // 8) - 1][(numb % 8) + 1] + '.png'
                    self.btn[numb - 8 + 1].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
                    self.whereCouldGo[(numb // 8) - 1][(numb % 8) + 1] = True

        else:
            chessType = 0
            for m in range(5):
                if self.gameData[numb // 8][numb % 8].find(self.names[m])!=-1:
                    chessType=m
                    break
            for m in range(len(self.posibleTurns[chessType])):
                for n in range(len(self.posibleTurns[chessType][m])):
                    if (numb//8)+self.posibleTurns[chessType][m][n][0]<8 and (numb//8)+self.posibleTurns[chessType][m][n][0] >=0 and (numb%8)+self.posibleTurns[chessType][m][n][1]<8 and(numb%8)+self.posibleTurns[chessType][m][n][1]>=0:
                        if self.gameData[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] == '' and self.CouldWeGoWithoutChah([self.posibleTurns[chessType][m][n][0],self.posibleTurns[chessType][m][n][1]],numb,self.gameData)==True:
                            self.whereCouldGo[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] = True
                            b = self.way+'/img/blue' + self.gameData[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] + '.png'
                            self.btn[((numb // 8) + self.posibleTurns[chessType][m][n][0])*8+(numb % 8) + self.posibleTurns[chessType][m][n][1]].setStyleSheet('''background-image:url("%s");background-repeat:no-repeat''' % b)
                        elif self.gameData[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]].find('white') and self.CouldWeGoWithoutChah([self.posibleTurns[chessType][m][n][0],self.posibleTurns[chessType][m][n][1]],numb,self.gameData)==True:
                            if self.gameData[numb // 8][numb % 8].find('white'):
                                break
                            else:
                                self.whereCouldGo[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] = True
                                b = self.way+'/img/blue' + self.gameData[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] + '.png'
                                self.btn[((numb // 8) + self.posibleTurns[chessType][m][n][0]) * 8 + (numb % 8) +
                                self.posibleTurns[chessType][m][n][1]].setStyleSheet('''background-image:url("%s");background-repeat:no-repeat''' % b)
                                break
                        else:
                            if self.gameData[numb // 8][numb % 8].find('black'):
                                break
                            elif  self.CouldWeGoWithoutChah([self.posibleTurns[chessType][m][n][0],self.posibleTurns[chessType][m][n][1]],numb,self.gameData)==True:
                                self.whereCouldGo[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] = True
                                b = self.way+'/img/blue' + self.gameData[(numb // 8) + self.posibleTurns[chessType][m][n][0]][(numb % 8) + self.posibleTurns[chessType][m][n][1]] + '.png'
                                self.btn[((numb // 8) + self.posibleTurns[chessType][m][n][0]) * 8 + (numb % 8) +
                                self.posibleTurns[chessType][m][n][1]].setStyleSheet('''background-image:url("%s");background-repeat:no-repeat''' % b)
                                break
                            break
        if self.gameData[numb // 8][numb % 8] == 'blackking' and self.blackKingTurn==False and(self.rocks[0]==False or self.rocks[1]==False):
            if(self.chachOrNo(numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, 1],numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, 2],numb,self.gameData)==True and self.rocks[1]==False  and (self.gameData[(numb // 8)][(numb % 8)+1] == '' and self.gameData[(numb // 8)][(numb % 8)+2] == '' )):

                self.whereCouldGo[(numb // 8) ][(numb % 8) + 2] = True
                self.btn[numb+2].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
            if (self.chachOrNo(numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, -1],numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, -2],numb,self.gameData)==True and self.rocks[0]==False  and self.gameData[(numb // 8)][(numb % 8)-3] == ''   and (self.gameData[(numb // 8)][(numb % 8)-1] == '' and self.gameData[(numb // 8)][(numb % 8)-2] == '') ):
                self.whereCouldGo[(numb // 8)][(numb % 8) - 2] = True
                self.btn[numb - 2].setStyleSheet('''background-image:url("%s");
                                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
        if self.gameData[numb // 8][numb % 8] == 'whiteking' and self.whiteKingTurn==False and(self.rocks[2]==False or self.rocks[3]==False) :
            if(self.chachOrNo(numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, 1],numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, 2],numb,self.gameData)==True and self.rocks[3]==False  and (self.gameData[(numb // 8)][(numb % 8)+1] == '' and self.gameData[(numb // 8)][(numb % 8)+2] == '' )):
                self.whereCouldGo[(numb // 8)][(numb % 8) + 2] = True
                self.btn[numb + 2].setStyleSheet('''background-image:url("%s");
                                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')
            if (self.chachOrNo(numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, -1],numb,self.gameData)==True and self.CouldWeGoWithoutChah([0, -2],numb,self.gameData)==True and self.rocks[2]==False and self.gameData[(numb // 8)][(numb % 8)-3] == '' and(self.gameData[(numb // 8)][(numb % 8)-1] == '' and self.gameData[(numb // 8)][(numb % 8)-2] == '') ):
                self.whereCouldGo[(numb // 8)][(numb % 8) - 2] = True
                self.btn[numb - 2].setStyleSheet('''background-image:url("%s");
                                                       background-repeat:no-repeat''' % self.way+'/img/blue.png')




    def CouldWeGoWithoutChah(self,mimi,numb,checkDataMasiv):
        a=checkDataMasiv[(numb // 8) +mimi[0]][ (numb % 8) +mimi[1]]
        checkDataMasiv[(numb // 8) +mimi[0]][ (numb % 8) +mimi[1]] = checkDataMasiv[numb // 8][numb % 8]
        checkDataMasiv[numb // 8][numb % 8] = ''
        for figureNumb in [0,2,3]:
            for numbFindedUnitToCheck in range(64):
                if checkDataMasiv[numbFindedUnitToCheck//8][numbFindedUnitToCheck%8].find(self.names[figureNumb])!=-1:
                    if(self.turn%2==0 and checkDataMasiv[numbFindedUnitToCheck//8][numbFindedUnitToCheck%8].find('black')!=-1):
                        for m in range(len(self.posibleTurns[figureNumb])):
                            for n in range(len(self.posibleTurns[figureNumb][m])):
                                if (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]<8 and (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0] >=0 and (numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]<8 and(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]>=0:
                                    if checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('white')!=-1:
                                        if(checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('king')!=-1):
                                            checkDataMasiv[numb // 8][numb % 8]=checkDataMasiv[(numb // 8) +mimi[0]][ (numb % 8) +mimi[1]]
                                            checkDataMasiv[(numb // 8) + mimi[0]][(numb % 8) + mimi[1]]=a
                                            return False
                                        else:
                                            break

                    elif self.turn%2==1 and checkDataMasiv[numbFindedUnitToCheck//8][numbFindedUnitToCheck%8].find('white')!=-1 :
                        for m in range(len(self.posibleTurns[figureNumb])):
                            for n in range(len(self.posibleTurns[figureNumb][m])):
                                if (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]<8 and (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0] >=0 and (numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]<8 and(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]>=0:
                                    if checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('black')!=-1:
                                        if(checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('king')!=-1):
                                            checkDataMasiv[numb // 8][numb % 8] = checkDataMasiv[(numb // 8) + mimi[0]][
                                                (numb % 8) + mimi[1]]
                                            checkDataMasiv[(numb // 8) + mimi[0]][(numb % 8) + mimi[1]] = a
                                            return False
                                        else:
                                            break
        checkDataMasiv[numb // 8][numb % 8] = checkDataMasiv[(numb // 8) + mimi[0]][(numb % 8) + mimi[1]]
        checkDataMasiv[(numb // 8) + mimi[0]][(numb % 8) + mimi[1]] = a
        return True

    def chachOrNo (self,numb,checkDataMasiv):
        for figureNumb in [0,2,3]:
            for numbFindedUnitToCheck in range(64):
                if checkDataMasiv[numbFindedUnitToCheck//8][numbFindedUnitToCheck%8].find(self.names[figureNumb])!=-1:
                    if(self.turn%2==0 and checkDataMasiv[numbFindedUnitToCheck//8][numbFindedUnitToCheck%8].find('black')!=-1):
                        for m in range(len(self.posibleTurns[figureNumb])):
                            for n in range(len(self.posibleTurns[figureNumb][m])):
                                if (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]<8 and (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0] >=0 and (numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]<8 and(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]>=0:
                                    if checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('white')!=-1:
                                        if(checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('king')!=-1):
                                            return False
                                        else:
                                            break

                    elif self.turn%2==1 and checkDataMasiv[numbFindedUnitToCheck//8][numbFindedUnitToCheck%8].find('white')!=-1 :
                        for m in range(len(self.posibleTurns[figureNumb])):
                            for n in range(len(self.posibleTurns[figureNumb][m])):
                                if (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]<8 and (numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0] >=0 and (numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]<8 and(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]>=0:
                                    if checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('black')!=-1:
                                        if(checkDataMasiv[(numbFindedUnitToCheck//8)+self.posibleTurns[figureNumb][m][n][0]][(numbFindedUnitToCheck%8)+self.posibleTurns[figureNumb][m][n][1]].find('king')!=-1):
                                            return False
                                        else:
                                            break

        return True


    def _turn(self,to):
        if(self.gameData[self.last // 8][self.last % 8].find('king')!=-1):
            if to%8==(self.last%8)+2:
                if self.gameData[self.last // 8][self.last % 8].find('white')!=-1:
                    self.gameData[self.last // 8][(self.last % 8)+1] = self.gameData[7][7]
                    self.gameData[7][7]=''
                    self.btn[30].setText('1')
                else:
                    self.gameData[self.last // 8][(self.last % 8) + 1] = self.gameData[0][7]
                    self.gameData[0][7] = ''
                    self.btn[30].setText('2')
            elif to%8==(self.last%8)-2:
                if self.gameData[self.last // 8][self.last % 8].find('white')!=-1:
                    self.gameData[self.last // 8][(self.last % 8)-1] = self.gameData[7][0]
                    self.gameData[7][0]=''
                    self.btn[30].setText('3')
                else:
                    self.gameData[self.last // 8][(self.last % 8) - 1] = self.gameData[0][0]
                    self.gameData[0][0] = ''
                    self.btn[30].setText('4')
            if self.gameData[self.last // 8][self.last % 8].find('white')!=-1:
                self.whiteKingTurn=True
            else:
                self.blackKingTurn=True
        if self.last==0:
            self.rocks[0] = True
        elif self.last==7:
            self.rocks[1] = True
        elif self.last == 54:
            self.rocks[2] = True
        elif self.last == 63:
            self.rocks[3] = True
        if(self.gameData[self.last//8][self.last%8]=='whitewar' and to==self.last-16):
            self.whiteWarDoubleTurn=self.last-8
        elif(self.gameData[self.last//8][self.last%8]=='blackwar' and to==self.last+16):
            self.blackWarDoubleTurn = self.last + 8
        if self.gameData[self.last//8][self.last%8]=='whitewar' and to==self.blackWarDoubleTurn:
            self.gameData[(self.blackWarDoubleTurn//8)+1][self.last % 8]=''
        if self.gameData[self.last // 8][self.last % 8] == 'blackwar' and to == self.blackWarDoubleTurn:
            self.gameData[(self.whiteWarDoubleTurn // 8) - 1][self.last % 8] = ''
        if(self.turn%2==0):
            self.blackWarDoubleTurn==0
        if(self.turn%2==1):
            self.whiteWarDoubleTurn==0
        self.gameData[to//8][to%8]=self.gameData[self.last//8][self.last%8]
        self.gameData[self.last // 8][self.last % 8]=''
        self.deleteTurn()




    def deleteTurn(self):
        for i in range(64):

            a = self.way+'/img/black' + self.gameData[i // 8][i % 8] + '.png'
            b = self.way+'/img/white' + self.gameData[i // 8][i % 8] + '.png'
            if ((i % 2) + i // 8) % 2 == 1:
                self.btn[i].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % a)
            else:
                self.btn[i].setStyleSheet('''background-image:url("%s");
                                       background-repeat:no-repeat''' % b)
            self.whereCouldGo[i//8][i%8]=False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChetoTam()
    sys.exit(app.exec_())
