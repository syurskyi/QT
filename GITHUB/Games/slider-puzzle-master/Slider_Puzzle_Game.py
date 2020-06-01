import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, \
     QVBoxLayout, QAction, qApp, QWidget, QMessageBox, QLabel, QPushButton, QTextBrowser
from PyQt5.QtGui import QDesktopServices, QFont
from PyQt5.QtCore import QUrl, QTimer
import random

m1 = (0, 80)
m2 = (80, 0)
m3 = (160, 0)
m3_1 = (-160, 0)
m4 = (0, 160)
m4_1 = (0, -160)
m5 = (240, 0)
m5_1 = (-240, 0)
m6 = (0, 240)
m6_1 = (0, -240)

coords = [(0, 0), (80, 0), (160, 0), (240, 0),
          (0, 80), (80, 80), (160, 80), (240, 80),
          (0, 160), (80, 160), (160, 160), (240, 160),
          (0, 240), (80, 240), (160, 240), (240, 240)]

rightOrder = [1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 0]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.content = PlaceButton()
        self.setCentralWidget(self.content)

        self.initMW()

    def initMW(self):
        menubar = self.menuBar()
        file = menubar.addMenu("About")

        github = QAction("Github Codes", self)
        github.triggered.connect(self.openUrl)
        github.setStatusTip("Click To Connect Github and View The Codes")
        file.addAction(github)

        exitAct = QAction("Quit", self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip("Click to quit")
        exitAct.triggered.connect(qApp.quit)
        file.addAction(exitAct)

        self.statusBar()
        self.setStyleSheet("background-color: white")
        self.move(300, 250)
        self.setFixedSize(590, 375)
        self.setWindowTitle('Slider Puzzle | Selman Y.')
        self.show()

    def openUrl(self):
        url = QUrl("https://github.com/kmnsys/slider-puzzle")
        if not QDesktopServices.openUrl(url):
            QMessageBox.warning(self, 'Open Url', 'Could not Open Url')


class PlaceButton(QWidget):

    def __init__(self):
        super().__init__()

        self.c = True

        self.emptyCooords = (240, 240)

        self.clickCount = 0
        self.initPB()

    def ctimer(self):
        self.min = 5
        self.sec = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.clock)
        self.timer.start(1000)

    def clock(self):

        if self.sec == 0:
            self.sec = 59
            self.min = self.min - 1

        if self.sec<10:
            if self.min == 0:
                self.time = "00:00"
                self.timer.stop()
            else:
                self.time = "0" + str(self.min) + ":0" + str(self.sec)
        else:
            self.time = "0" + str(self.min) + ":" + str(self.sec)

        self.textb.setText(self.time)
        #self.timeLabel.setText(self.time)
        self.sec = self.sec - 1


    def initPB(self):
        self.font = QFont()
        self.font.setPointSize(19)

        self.label = QLabel()
        self.clickCountLabel = QLabel()
        self.timeLabel = QLabel()

        hbox = QHBoxLayout()
        hbox.addWidget(self.label)
        vbox = QVBoxLayout()
        hbox.addLayout(vbox)

        vbox.addWidget(self.timeLabel)
        vbox.addWidget(self.clickCountLabel)

        self.setLayout(hbox)

        self.clickCountLabel.setMaximumWidth(210)
        self.clickCountLabel.setFont(self.font)
        self.clickCountLabel.setStyleSheet("color: #585942")

        self.timeLabel.setFont(self.font)
        self.timeLabel.setStyleSheet("color: #585942")

        self.table()

    def table(self):
        self.one = ""
        self.two = ""
        self.three = ""
        self.four = ""
        self.five = ""
        self.six = ""
        self.seven = ""
        self.eight = ""
        self.nine = ""
        self.ten = ""
        self.eleven = ""
        self.twelve = ""
        self.thirteen = ""
        self.fourteen = ""
        self.fifteen = ""

        self.newl = [self.one, self.two, self.three, self.four, self.five,
                     self.six, self.seven, self.eight, self.nine, self.ten,
                     self.eleven, self.twelve, self.thirteen, self.fourteen,
                     self.fifteen]

        self.buttonsOrder = []

        self.places = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                       10, 11, 12, 13, 14, 15]

        #random.shuffle(self.places)

        m = 0

        for i in self.places:
            self.newl[i - 1] = QPushButton(str(i), self.label)
            self.newl[i - 1].setStyleSheet("""background-color: #078ab2;
                                              color: white;
                                              border-style: outset;
                                              border-width: 4px;    
                                              border-color: beige 
                                              """)
            self.newl[i - 1].setFont(self.font)
            self.newl[i - 1].resize(77, 77)
            self.newl[i - 1].move(*coords[m])
            self.newl[i - 1].clicked.connect(self.moveButton)
            self.buttonsOrder.append(self.newl[i - 1])
            m = m + 1

        self.textb =QTextBrowser(self.label)
        self.textb.move(240, 240)
        self.textb.resize(75, 75)
        self.textb.setStyleSheet("""background-color: white;
                                    color: #cbd2db;
                                    border-style: outset;
                                    border-width: 4px;    
                                    border-color: white;
                                    font: 22px;
                                    padding-top: 14px;
                                    padding-left: 2px
                                    """)
        self.textb.setText("05:00")

        self.places.append(self.textb)
        self.buttonsOrder.append(self.textb)

    def moveButton(self):

        if self.c:
            self.ctimer()
            self.c = False
        sender = self.sender()
        self.senderC = sender
        senderText = sender.text()

        self.emptyCooords = coords[self.places.index(self.textb)]
        self.pressButtonCoords = (sender.x(), sender.y())

        diffCoords = (abs(self.emptyCooords[0] - self.pressButtonCoords[0]),
                      abs(self.emptyCooords[1] - self.pressButtonCoords[1]))

        diffTwoBlock = (self.emptyCooords[0] - self.pressButtonCoords[0],
                        self.emptyCooords[1] - self.pressButtonCoords[1])

        if diffCoords == m1 or diffCoords == m2:
            sender.move(*self.emptyCooords)
            self.organize(senderText, sender)

            self.emptyCooords = coords[self.places.index(self.textb)]
            self.textb.move(*self.emptyCooords)
            self.clickCounts()
            self.finishGame()

        elif diffTwoBlock == m3:
            self.twoBlock(sender, senderText, 1)
            # Two Block to Right

        elif diffTwoBlock == m3_1:
            self.twoBlock(sender, senderText, -1)
            # Two Block to Left

        elif diffTwoBlock == m4_1:
            self.twoBlock(sender, senderText, -4)
            # Two Block to Up

        elif diffTwoBlock == m4:
            self.twoBlock(sender, senderText, 4)
            # Two Block to Down

        elif diffTwoBlock == m5:
            self.threeBlock(sender, senderText, 1)
            # Three Block to Right

        elif diffTwoBlock == m5_1:
            self.threeBlock(sender, senderText, -1)
            # Three Block to Left

        elif diffTwoBlock == m6_1:
            self.threeBlock(sender, senderText, -4)
            # Three Block to Up

        elif diffTwoBlock == m6:
            self.threeBlock(sender, senderText, 4)
            # Three Block to Down

    def twoBlock(self, sender, senderText, slideNum):
        senderButtonIndex = self.places.index(int(senderText))
        senderButtonNext = self.buttonsOrder[senderButtonIndex + slideNum]
        senderButtonNextText = senderButtonNext.text()

        senderButtonNext.move(*self.emptyCooords)
        self.organize(senderButtonNextText, senderButtonNext)

        self.emptyCooords = coords[self.places.index(self.textb)]
        self.textb.move(*self.pressButtonCoords)

        sender.move(*self.emptyCooords)
        self.organize(senderText, sender)

        self.clickCounts()
        self.finishGame()

    def threeBlock(self, sender, senderText, slideNum):
        senderButtonIndex = self.places.index(int(senderText))
        senderButtonNext = self.buttonsOrder[senderButtonIndex + slideNum]
        senderButtonNextText = senderButtonNext.text()

        senderButtonNextToNext = self.buttonsOrder[senderButtonIndex + 2 * slideNum]
        senderButtonRightToRightText = senderButtonNextToNext.text()

        senderButtonNextToNext.move(*self.emptyCooords)
        self.organize(senderButtonRightToRightText, senderButtonNextToNext)

        self.emptyCooords = coords[self.places.index(self.textb)]

        senderButtonNext.move(*self.emptyCooords)
        self.organize(senderButtonNextText, senderButtonNext)

        self.emptyCooords = coords[self.places.index(self.textb)]
        self.textb.move(*self.pressButtonCoords)

        sender.move(*self.emptyCooords)
        self.organize(senderText, sender)

        self.clickCounts()
        self.finishGame()

    def clickCounts(self):
        self.clickCount += 1
        self.clickCountLabel.setText("Click Count: " + str(self.clickCount))

    def organize(self, stext, sbutton):
        emptyBtnPlc, pressBtnPlc = self.places.index(self.textb), self.places.index(int(stext))
        self.places[pressBtnPlc], self.places[emptyBtnPlc] = self.places[emptyBtnPlc], self.places[pressBtnPlc]

        emptyBtnPlc1, pressBtnPlc1 = self.buttonsOrder.index(self.textb), self.buttonsOrder.index(sbutton)
        self.buttonsOrder[pressBtnPlc1], self.buttonsOrder[emptyBtnPlc1] = self.buttonsOrder[emptyBtnPlc1], \
                                                                           self.buttonsOrder[pressBtnPlc1]

    def finishGame(self):
        if self.places == rightOrder:
            self.clickCountLabel.setText("GAME OVER" + "\n\n" + "Click Count: " + str(self.clickCount))
            point = (300-60*self.min + self.sec)**1.5 - self.clickCount**0.9

            self.timer.stop()
            QMessageBox.information(self, 'GAME OVER', "Click Count= " + str(self.clickCount) +
                                "\n" + "Time = " +str(self.time) + "\n\nPoint = " + str(point))

            self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pb = MainWindow()
    sys.exit(app.exec_())
