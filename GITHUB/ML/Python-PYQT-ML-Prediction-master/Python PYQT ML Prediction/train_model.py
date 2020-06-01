# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'train_model.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import train_result
fname=None
file=None
class Ui_Form(object):
     
    he=None
    def back(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.aMainWindow = QtWidgets.QMainWindow()
        try:
                     from Main_Menu import Ui_Form1
                     self.qMainWindow = QtWidgets.QMainWindow()
                     self.ui = Ui_Form1()
                     self.ui.setupUi(self.qMainWindow)
                     self.qMainWindow.show()
                     self.he.setVisible(False)

        except Exception as e:
                print(e)
    def clear(self):
        global file
        file=None
    def predict(self):
        try:
                    if file ==None:
                         self.label_3.setText('Please Select a file first')
                    else :
                        print(file)
                        train_result.putinfo(file)
        except Exception as e:
                print(e)
       
    def openfile(self):   
          global fname
          global file
          fname= QFileDialog.getOpenFileName()
          try:
                       file=fname[0]
                       print(fname)
                       self.label_3.setText(fname[0])
          except Exception as e:
                print(e)
    def setupUi(self, Form):
        self.he=Form
        Form.setObjectName("Form")
        Form.resize(684, 432)
        Form.setStyleSheet("#Form\n"
"{\n"
"background:url(img/bg1.jpg)  no-repeat center center fixed;\n"
"}\n"
"#frame{\n"
"background:#f1f1f1;\n"
"border-radius:30px;\n"
"}\n"
"#frame_2{\n"
"background:#a1a1a1;\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:10px;\n"
"border: 2px solid black;\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"background:dodgerblue;\n"
"border-radius:15px;\n"
"font-size:20px;\n"
"\n"
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
"font-size:22px;\n"
"}\n"
"#label_2{\n"
"color:black;\n"
"font-size:25px;\n"
"font-style:bold;\n"
"}\n"
"#label_3{\n"
"color:green;\n"
"font-size:13px;\n"
"font-style:bold;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 40, 571, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 30, 511, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 441, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(280, 140, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 140, 201, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 190, 501, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 270, 180, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 270, 180, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 270, 90, 41))
        self.pushButton_4.setObjectName("pushButton_3")

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 491, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(self.lineEdit.clear)
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.predict)
        self.pushButton_3.clicked.connect(self.label_3.clear)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.back)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Train Model"))
        self.label_2.setText(_translate("Form", "TRAIN MACHINE LEARNING MODEL"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Enter Company Name"))
        self.label.setText(_translate("Form", "Comapany Name :-"))
        self.pushButton.setText(_translate("Form", "SELECT FILE"))
        self.pushButton_2.setText(_translate("Form", "TRAIN MODEL"))
        self.pushButton_3.setText(_translate("Form", "RESET"))
        self.pushButton_4.setText(_translate("Form", "BACK"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    win=MainWindow
    MainWindow.show()
    sys.exit(app.exec_())

    

