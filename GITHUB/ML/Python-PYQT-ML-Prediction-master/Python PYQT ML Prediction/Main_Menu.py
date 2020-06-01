# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form1(object):
    he=None
    def train(self):
                     from train_model import Ui_Form
                     self.qMainWindow = QtWidgets.QMainWindow()
                     self.ui = Ui_Form()
                     self.ui.setupUi(self.qMainWindow)
                     self.he.setVisible(False)
                     self.qMainWindow.show()      

    def setupUi(self, Form):
        self.he=Form
        Form.setObjectName("Form")
        Form.resize(677, 459)
        Form.setStyleSheet("*{\n"
"font-family:centry gothic;\n"
"}\n"
"#Form\n"
"{\n"
"background:url(img/bg1.jpg)  no-repeat center center fixed;\n"
"}\n"
"#frame\n"
"{\n"
"background:#F1F1F1;\n"
"border-radius:30px;\n"
"\n"
"}\n"
"#frame_2{\n"
"border: 2px solid black;\n"
"\n"
"background:dodgerblue;\n"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"}\n"
"#label{\n"
"font-size:25px;\n"
"\n"
"}\n"
"#label_2{\n"
"font-size:30px;\n"
"font-weight: bold;\n"
"}\n"
"#label_3{\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}\n"
"QToolButton{\n"
"\n"
"background:dodgerblue;\n"
"border-radius:60px;\n"
"}\n"
"QPushButton{\n"
"border: 2px solid black;\n"
"font-size:20px;\n"
"\n"
"background:dodgerblue;\n"
"border-radius:30px;\n"
"}\n"
"#label_4{\n"
"font-size:15px;\n"
"\n"
"}\n"
"#label_5{\n"
"font-size:15px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(70, 60, 551, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 241, 341))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 191, 41))
        self.label_2.setObjectName("label_2")
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(20, 180, 201, 121))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/stock_market.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(200, 200))
        self.toolButton.setObjectName("toolButton")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(120, 110, 71, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(250, 80, 281, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 180, 281, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(250, 290, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(350, 290, 171, 31))
        self.label_5.setObjectName("label_5")

        
        self.pushButton.clicked.connect(self.train)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Main Menu"))
        self.label.setText(_translate("Form", "Stock Market"))
        self.label_2.setText(_translate("Form", "Prediction"))
        self.toolButton.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "using ML"))
        self.pushButton.setText(_translate("Form", "Train Model"))
        self.pushButton_2.setText(_translate("Form", "TEST Model"))
        self.label_4.setText(_translate("Form", "Designed by :-"))
        self.label_5.setText(_translate("Form", "Abhay Bhadouriya"))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Form1()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
     
  
