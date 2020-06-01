# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
#database
cricket=sqlite3.connect('cricket.db')
curcricket=cricket.cursor()

class Ui_MainWindow(object):
    #init method for variables
    def __init__(self):
        self.batCount=0
        self.bwlCount=0
        self.arCount=0
        self.wkCount=0
        self.currentPoints=1100
        self.pointsUsed=0
        self.totalPoints=1100


    def setvariables(self):
        self.batCount=0
        self.bwlCount=0
        self.arCount=0
        self.wkCount=0
        self.currentPoints=1100
        self.pointsUsed=0
        self.totalPoints=1100
        
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1160, 713)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(80, 60, 1001, 111))
        self.widget.setStyleSheet("\n"
"background-color: rgb(238, 238, 236);")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 131, 21))
        self.label_3.setStyleSheet("font: 75 12pt \"Droid Sans Fallback\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 30, 971, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setStyleSheet("font: 57 13pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.labelBat = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelBat.setStyleSheet("color: rgb(114, 159, 207);\n"
"font: 57 13pt \"Ubuntu\";")
        self.labelBat.setObjectName("labelBat")
        self.horizontalLayout_3.addWidget(self.labelBat)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setStyleSheet("font: 57 13pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.labelBow = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelBow.setStyleSheet("color: rgb(114, 159, 207);\n"
"font: 57 13pt \"Ubuntu\";")
        self.labelBow.setObjectName("labelBow")
        self.horizontalLayout_3.addWidget(self.labelBow)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_8.setStyleSheet("font: 57 13pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.labelAr = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelAr.setStyleSheet("color: rgb(114, 159, 207);\n"
"font: 57 13pt \"Ubuntu\";")
        self.labelAr.setObjectName("labelAr")
        self.horizontalLayout_3.addWidget(self.labelAr)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_10.setStyleSheet("font: 57 13pt \"Ubuntu\";\n"
"color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.labelWk = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelWk.setStyleSheet("color: rgb(114, 159, 207);\n"
"font: 57 13pt \"Ubuntu\";")
        self.labelWk.setObjectName("labelWk")
        self.horizontalLayout_3.addWidget(self.labelWk)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 210, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 210, 81, 17))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 240, 371, 411))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rbBat = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbBat.setObjectName("rbBat")        
        self.horizontalLayout.addWidget(self.rbBat)
        self.rbBow = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbBow.setObjectName("rbBow")
        self.horizontalLayout.addWidget(self.rbBow)
        self.rbAr = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbAr.setObjectName("rbAr")
        self.horizontalLayout.addWidget(self.rbAr)
        self.rbWk = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbWk.setObjectName("rbWk")
        self.horizontalLayout.addWidget(self.rbWk)
        self.list1 = QtWidgets.QListWidget(self.frame)
        self.list1.setGeometry(QtCore.QRect(30, 70, 311, 311))
        self.list1.setObjectName("list1")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(660, 240, 371, 411))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 351, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_16 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.labelTeamName = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelTeamName.setStyleSheet("color: rgb(114, 159, 207);")
        self.labelTeamName.setObjectName("labelTeamName")
        self.horizontalLayout_2.addWidget(self.labelTeamName)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.list2 = QtWidgets.QListWidget(self.frame_2)
        self.list2.setGeometry(QtCore.QRect(30, 70, 311, 311))
        self.list2.setObjectName("list2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(250, 210, 67, 17))
        self.label_12.setStyleSheet("color: rgb(114, 159, 207);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(750, 210, 67, 17))
        self.label_13.setStyleSheet("color: rgb(114, 159, 207);\n"
"")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(580, 440, 16, 17))
        self.label_14.setObjectName("label_14")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1160, 22))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #code added
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menufunction)
        self.rbBat.toggled.connect(self.radioButtonhandler)
        self.rbBow.toggled.connect(self.radioButtonhandler)
        self.rbAr.toggled.connect(self.radioButtonhandler)
        self.rbWk.toggled.connect(self.radioButtonhandler)
        self.list1.itemDoubleClicked.connect(self.removelist1)
        self.list2.itemDoubleClicked.connect(self.removelist2)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Your Selections"))
        self.label_4.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.labelBat.setText(_translate("MainWindow", "##"))
        self.label_6.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.labelBow.setText(_translate("MainWindow", "##"))
        self.label_8.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.labelAr.setText(_translate("MainWindow", "##"))
        self.label_10.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.labelWk.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Points Available"))
        self.label_2.setText(_translate("MainWindow", "Points Used"))
        self.rbBat.setText(_translate("MainWindow", "BAT"))
        self.rbBow.setText(_translate("MainWindow", "BOW"))
        self.rbAr.setText(_translate("MainWindow", "AR"))
        self.rbWk.setText(_translate("MainWindow", "WK"))
        self.label_16.setText(_translate("MainWindow", "Team Name"))
        self.labelTeamName.setText(_translate("MainWindow", "Displayed Here"))
        self.label_12.setText(_translate("MainWindow", "####"))
        self.label_13.setText(_translate("MainWindow", "####"))
        self.label_14.setText(_translate("MainWindow", ">"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))



    #message box if selected more players
    def messageBox(self,count,text):
        from PyQt5.QtWidgets import QMessageBox,QWidget
        w=QWidget()
        QMessageBox.about(w,"Error","Can't Select more than {} {}".format(count,text))

        
    #list addition and deletion
    def removelist1(self, item): 
        self.list1.takeItem(self.list1.row(item))        
        #self.list2.addItem(item.text())

        #get value of the player
        sql='Select value from stats where player = "'+item.text()+'" ;'
        #print(item.text())
        curcricket.execute(sql)
        record=curcricket.fetchone()
        #print(record[0])        
        points=int(record[0])
        self.currentPoints=self.currentPoints-points
        self.pointsUsed=self.pointsUsed+points

        #get player category
        flag=0
        sql='Select ctg from stats where player = "'+item.text()+'" ;'
        curcricket.execute(sql)
        record=curcricket.fetchone()
        if record[0]=='BAT':
            self.batCount=self.batCount+1
            if self.batCount > 5:
                self.messageBox(5,'Batsmen')
                self.batCount=self.batCount-1
                flag=1
                
                
        if record[0]=='BWL':
            self.bwlCount=self.bwlCount+1
            if self.bwlCount > 4:
                self.messageBox(4,'Bowlers')
                self.bwlCount=self.bwlCount-1
                flag=1
                
        if record[0]=='AR':
            self.arCount=self.arCount+1
            if self.arCount > 2:
                self.messageBox(2,'AllRounders')
                self.arCount=self.arCount-1
                flag=1
                
        if record[0]=='WK':
            self.wkCount=self.wkCount+1
            if self.wkCount > 1:
                self.messageBox(1,'Wicket-Keeper')
                self.wkCount=self.wkCount-1
                flag=1
        if flag==0:
            self.list2.addItem(item.text())
        if flag==1:
            self.list1.addItem(item.text())
            self.currentPoints=self.currentPoints+points
            self.pointsUsed=self.pointsUsed-points
            
        self.setLabels()
        
        

    def removelist2(self, item):
        self.list2.takeItem(self.list2.row(item))
        sql='Select value from stats where player = "'+item.text()+'" ;'
        #print(item.text())
        curcricket.execute(sql)
        record=curcricket.fetchone()
        #print(record[0])        
        points=int(record[0])
        self.currentPoints=self.currentPoints+points
        self.pointsUsed=self.pointsUsed-points

        #get player category
        sql='Select ctg from stats where player = "'+item.text()+'" ;'
        curcricket.execute(sql)
        record=curcricket.fetchone()
        if record[0]=='BAT':
            self.batCount=self.batCount-1
        if record[0]=='BWL':
            self.bwlCount=self.bwlCount-1
        if record[0]=='AR':
            self.arCount=self.arCount-1
        if record[0]=='WK':
            self.wkCount=self.wkCount-1
            
        self.setLabels()
        self.radioButtonhandler()
          


    #function to display contents in list1 based on selection of radio button and items not present in list2
    def radioButtonhandler(self):
        #clear the list1
        self.list1.clear()

        #check states of buttons and execute query
        if self.rbBat.isChecked()==True:
            curcricket.execute('Select player from stats where ctg = "BAT" ;')
        if self.rbBow.isChecked()==True:
            curcricket.execute('Select player from stats where ctg = "BWL" ;')
        if self.rbAr.isChecked()==True:
            curcricket.execute('Select player from stats where ctg = "AR" ;')            
        if self.rbWk.isChecked()==True:
            curcricket.execute('Select player from stats where ctg = "WK" ;')
            

        #Add items to the list 1
        while True:
            record =curcricket.fetchone()
            if record==None:
                break
            #find items returns a list of items , so it will be empty if list2 doesn't have the item
            X=self.list2.findItems(record[0],QtCore.Qt.MatchExactly)
            if len(X)==0:
                self.list1.addItem(record[0])


    #function to set all labels with values of variable they currently have
    def setLabels(self):
        self.labelBat.setText(str(self.batCount))
        self.labelBow.setText(str(self.bwlCount))
        self.labelAr.setText(str(self.arCount))
        self.labelWk.setText(str(self.wkCount))
        self.label_12.setText(str(self.currentPoints))
        self.label_13.setText(str(self.pointsUsed))

    
    #create an input dialog box to get team name
    def getTeamName(self):
        from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
        #created a QWidget object as QInputDialogBox only accepts QWidget object as its first argument
        w=QWidget()
        name,okPressed=QInputDialog.getText(w,"Team Name","Enter valid(Unique) Team Name ",QLineEdit.Normal,"")
        if okPressed and name!='':
            return name

    # function to handle NEW Team from menu
    def newTeam(self):
        #initialize things

        #clear both lists
        self.list1.clear()
        self.list2.clear()
        
        #set your selections variables to 0
        self.setvariables()
        #set all labels
        self.setLabels()
        #create a dialog box to get team name
        self.labelTeamName.setText(self.getTeamName())

        #set rbBat radio button on as default
        self.rbBat.setChecked(True)
        
    def openTeam(self):
        curcricket.execute('select teamName from teams ;')
        record=curcricket.fetchall()
        teamList=[]
        for i in record:
            #print(i[0])
            x=str(i[0])
            teamList.append(x)

        from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
        #created a QWidget object as QInputDialogBox only accepts QWidget object as its first argument
        w=QWidget()
        item,okPressed=QInputDialog.getItem(w,"Select Team Name","Teams Registered",teamList,0,False)
        if okPressed :
            return item

        
        
    def saveTeam(self,teamname,value,listPlayers):
        
        sql='INSERT INTO teams(teamName,value) values (\"{}\",{});'.format(teamname,value)
        #print(sql)
        curcricket.execute(sql)

        sql='CREATE TABLE {}(player string);'.format(teamname)
        curcricket.execute(sql)

        for i in listPlayers:
            sql='INSERT INTO {}( player ) VALUES ("{}");'.format(teamname,i)
            curcricket.execute(sql)

        cricket.commit()

    def errorBox(self):
        from PyQt5.QtWidgets import QMessageBox,QWidget
        w=QWidget()
        QMessageBox.about(w,"Error","Remove some Players")

    #this function handles menu operation
    def menufunction(self, action):
        txt= (action.text())
        if txt=='NEW Team':
            self.newTeam()
            
        if txt=='OPEN Team':
            teamname=self.openTeam()
            if teamname==None:
                return
            sql='Select player from {}'.format(teamname)
            curcricket.execute(sql)
            record=curcricket.fetchall()

            #set all variables and set labels accordingly
            self.batCount=0
            self.bwlCount=0
            self.arCount=0
            self.wkCount=0

            for i in record:
                #i[0] is the string containing player name
                curcricket.execute('select ctg from stats where player = "{}" ;'.format(i[0]))
                x=curcricket.fetchone()
                #x[0] is the category of player
                if x[0]=='BAT':
                    self.batCount=self.batCount+1
                elif x[0]=='BWL':
                    self.bwlCount=self.bwlCount+1
                elif x[0]=='AR':
                    self.arCount=self.arCount+1
                elif x[0]=='WK':
                    self.wkCount=self.wkCount+1
                    
            self.pointsUsed=0
            for i in record:
                #i[0] is the string containing player name
                curcricket.execute('select value from stats where player = "{}" ;'.format(i[0]))
                x=curcricket.fetchone()
                x=int(x[0])
                self.pointsUsed=self.pointsUsed+x

            self.currentPoints=self.totalPoints-self.pointsUsed

            

            #add items to list2
            self.list2.clear()
            for i in record:
                self.list2.addItem(i[0])

            #set labels
            self.setLabels()
            self.labelTeamName.setText(teamname)
            self.radioButtonhandler()
            

        if txt=='SAVE Team':
            teamname=self.labelTeamName.text()
            #print(teamname)

            if self.currentPoints < 0:
                self.errorBox()
                return
                
            i=0
            listPlayer=[]
            while i < self.list2.count():
                listPlayer.append(self.list2.item(i).text())
                #print(self.list2.item(i).text())
                i=i+1
            try:
                self.saveTeam(teamname,self.pointsUsed,listPlayer)
            except:
                self.labelTeamName.setText(self.getTeamName())

                cricket.rollback()
                

        if txt=='EVALUATE Team':
            from EvaluateScoreMenu import Ui_Form
            self.Form = QtWidgets.QWidget()
            self.ui= Ui_Form()
            self.ui.setupUi(self.Form)
            self.Form.show()
            #Form.exec()
               
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())

