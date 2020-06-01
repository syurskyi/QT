# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateScore.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def __init__(self):
        self.finalScore=0

        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 489)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(130, 30, 331, 17))
        self.label1.setObjectName("label1")
        self.box1 = QtWidgets.QComboBox(Form)
        self.box1.setGeometry(QtCore.QRect(70, 70, 151, 25))
        self.box1.setObjectName("box1")
        self.box2 = QtWidgets.QComboBox(Form)
        self.box2.setGeometry(QtCore.QRect(360, 70, 151, 25))
        self.box2.setObjectName("box2")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(30, 110, 521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 150, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 150, 67, 17))
        self.label_2.setObjectName("label_2")
        self.list1 = QtWidgets.QListWidget(Form)
        self.list1.setGeometry(QtCore.QRect(50, 180, 201, 231))
        self.list1.setObjectName("list1")
        self.list2 = QtWidgets.QListWidget(Form)
        self.list2.setGeometry(QtCore.QRect(310, 180, 256, 231))
        self.list2.setObjectName("list2")
        self.score = QtWidgets.QPushButton(Form)
        self.score.setGeometry(QtCore.QRect(230, 434, 121, 31))
        self.score.setObjectName("score")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #code added
        self.box1.setToolTip('Select Team')
        self.box2.setToolTip('Select Match')
        self.addItemsInCombox()
        self.addItemsinList()
        self.box1.currentIndexChanged.connect(self.addItemsinList)
        self.box2.currentIndexChanged.connect(self.addItemsinList)
        self.score.clicked.connect(self.dreamLeaguePoints)

        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dream League"))
        self.label1.setText(_translate("Form", "Evaluate the performance of your Fantasy Team"))
        self.label.setText(_translate("Form", "Players"))
        self.label_2.setText(_translate("Form", "Points"))
        self.score.setText(_translate("Form", "Calculate Score"))


    def getPoints(self,player):
        import sqlite3
        Cricket=sqlite3.connect('cricket.db')
        curCricket=Cricket.cursor()
        match=self.box2.currentText()
        
        #check if player played the match
        sql='Select scored from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        if record==None:
            Cricket.close()
            return 0
        
        points=0
        
        # batting points

        #points for runs
        sql='Select scored from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        runs=int(record[0])
        points=points+runs//2

        #points for century
        if runs>=50 and runs< 100:
            points = points + 5
        if runs>= 100:
            points = points + 10


        #points for strike rate
        
        sql='Select faced from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        balls=int(record[0])
        try:
            strikeRate=runs/balls
        except:
            strikeRate=0

        if strikeRate>=80 and strikeRate <100:
            points=points+2
        if strikeRate>=100:
            points=points+4

        #points for boundaries
        sql='Select fours from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        fours=int(record[0])

        sql='Select sixes from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        sixes=int(record[0])

        points=points+ fours + 2*sixes

        #bowling points

        #points for wkts
        sql='Select wkts from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        wkts=int(record[0])

        points= points+ 10*wkts

        #additional points
        if wkts>=3 and wkts <5:
            points = points + 5
        if wkts>=5:
            points = points + 10

        #points for economy rate
        sql='Select given from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        given=int(record[0])

        sql='Select bowled from {} where player = "{}" ;'.format(match,player)
        curCricket.execute(sql)
        record=curCricket.fetchone()
        bowled=int(record[0])
        
        try:
            economyRate=given/(bowled/6)
        except:
            economyRate=100#no points

        if economyRate>=3.5 and economyRate<4.5:
            points=points+5

        if economyRate>=2 and economyRate<3.5:
            points=points+7
            
        if economyRate<2:
            points=points+10

        Cricket.close()
        return points
   
      
        


        
    def addItemsInCombox(self):
        import sqlite3

        Cricket=sqlite3.connect('cricket.db')
        curCricket=Cricket.cursor()
        sql='Select teamName from teams ;'
        curCricket.execute(sql)
        record=curCricket.fetchall()

        for i in record:
            self.box1.addItem(i[0])

        sql='Select matchName from matches ;'
        curCricket.execute(sql)
        record=curCricket.fetchall()

        for i in record:
            self.box2.addItem(i[0])

        Cricket.close()


    def addItemsinList(self):
        import sqlite3
        Cricket=sqlite3.connect('cricket.db')
        curCricket=Cricket.cursor()
        #initialization
        self.list1.clear()
        self.list2.clear()
        self.finalScore=0
        
        team=self.box1.currentText()
        sql='Select * from {} ;'.format(team)

        curCricket.execute(sql)
        record=curCricket.fetchall()
        
        for i in record:
            self.list1.addItem(i[0])
            #calculate points for i[0] player
            point=self.getPoints(i[0])
            self.list2.addItem(str(point))
            self.finalScore=self.finalScore+point


    def dreamLeaguePoints(self):
        from PyQt5.QtWidgets import QMessageBox,QWidget
        w=QWidget()
        QMessageBox.about(w,"Result","Points are {}".format(self.finalScore))

        
            
        
        

if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


