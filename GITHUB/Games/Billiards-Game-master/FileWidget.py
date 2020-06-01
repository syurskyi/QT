from PyQt5.QtWidgets import *
from PyQt5  import QtCore
# from PyQt4.QtCore import *
import psutil
import os

class MyItem(QTableWidgetItem):
    # def __init__(self):
    #     super().__init__()
    #     self.dir = ""
    def __init__(self,i:str,dir:str):
        super().__init__(i)
        self.dir = dir
    def dir(self):
        return self.dir
class FileWidget(QTableWidget):
    def __init__(self):
        super().__init__()

        # #Button
        self.but = QPushButton(self)
        self.but.setText("转到")
        self.but.setGeometry(700, 0, 50, 50)
        self.doubleClicked.connect(self.DoubleClickedSignal)
        self.but.clicked.connect(self.ButtonClickedSignal)
        # # self.setGeometry(200, 200, 1000, 500)
        # self.but.setGeometry(700, 0, 50, 50)
        # # self.but.clicked.connect(self.ButtonClickedSignal)
        #
        # #TextEdit
        self.e2 = QLineEdit(self)
        self.e2.setGeometry(200,0,200,20)
        self.setColumnCount(1)
        self.setRowCount(10)
        self.count = 0
        title=['文件名']
        self.setHorizontalHeaderLabels(title)
        for filename in os.listdir(r'c:\windows'):
            # print(filename)
            self.insertRow(self.count)
            dir='c:\windows'+'\\'+str(filename)
            print(dir)
            self.setItem(self.count, 0, MyItem(str(filename),dir))
            self.count+=1
        self.count=0
        self.show()

    def ButtonClickedSignal(self):
        # print(self.e2.text())
        self.clear()
        self.dirList=list()
        for filename in os.listdir(self.e2.text()):
            print(filename)
            self.insertRow(self.count)
            dir=self.e2.text()+'\\'+str(filename)
            print(dir)
            self.setItem(self.count, 0, MyItem(str(filename),dir))
            self.dirList.append(dir)
            self.count += 1
        self.count=0
        self.hide()
        self.show()

        # self.repaint()
        pass


    def DoubleClickedSignal(self):
        # print("fuck")
        print(self.currentItem().text())
        print(self.dirList[self.currentItem().row()])

        f = open(self.dirList[self.currentItem().row()], 'r')
        pass