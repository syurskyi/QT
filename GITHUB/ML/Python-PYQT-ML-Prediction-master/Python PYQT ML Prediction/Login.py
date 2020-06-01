# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Main_Menu import Ui_Form1



class Ui_Form(object):
    
      
    def chkPassword(self):
        txt=self.lineEdit_2.text()
        pwd=self.lineEdit.text()
        if txt=='Admin' and pwd=='123':
                     self.qMainWindow = QtWidgets.QMainWindow()
                     self.ui = Ui_Form1()
                     self.ui.setupUi(self.qMainWindow)
                     MainWindow.hide()
                     self.qMainWindow.show()      

        else:
            self.lineEdit_2.setText('')
            self.lineEdit.setText('')
           

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(575, 529)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/bg1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(100.0)
        Form.setStyleSheet("*{\n"
"font-family:centry gothic;\n"
"font-size:24px;\n"
"}\n"
"#Form\n"
"{\n"
"background:url(img/bg1.jpg)  no-repeat center center fixed;\n"
"}\n"
"QFrame\n"
"{\n"
"background:#F1F1F1;\n"
"border-radius:30px;\n"
"\n"
"}\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"border: 2px solid black;\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"background:dodgerblue;\n"
"border-radius:15px;\n"
"border: 2px solid black;\n"
"box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0\n"
"        rgba(0, 0, 0, 0.19);\n"
"}\n"
"QToolButton{\n"
"border: 1px solid black;\n"
"\n"
"background:dodgerblue;\n"
"border-radius:60px;\n"
"}\n"
"QLabel{\n"
"color:black;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 100, 451, 371))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 70, 171, 41))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 290, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 290, 161, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 131, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 151, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(190, 210, 231, 31))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 140, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(220, 40, 121, 121))
        self.toolButton.setStyleSheet("")
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/profile_pic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(128, 128))
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.lineEdit_2.clear)
        self.pushButton.clicked.connect(self.chkPassword)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGIN FORM"))
        self.label.setText(_translate("Form", "USER LOGIN"))
        self.pushButton.setText(_translate("Form", "LOGIN"))
        self.pushButton_2.setText(_translate("Form", "RESET"))
        self.label_2.setText(_translate("Form", "USER ID :-"))
        self.label_3.setText(_translate("Form", "PASSWORD :-"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  ENTER PASSWORD"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  ENTER USER-ID"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
