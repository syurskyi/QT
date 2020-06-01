from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from time import sleep
import random
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(132, 153)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 111, 26))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 97, 26))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 100, 90, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.start)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "سیتم حدس بزنه"))
        self.radioButton_2.setText(_translate("Form", "من حدس بزنم"))
        self.pushButton.setText(_translate("Form", "submit"))
    def start(self):
        if (self.radioButton.isChecked()==True):
            self.Form1 = QtWidgets.QWidget()
            self.ui = Ui_Form1()
            self.ui.setupUi(self.Form1)
            self.Form1.show()
            Form.hide()
        if (self.radioButton_2.isChecked() == True):
            self.Form2 = QtWidgets.QWidget()
            self.ui = Ui_Form2()
            self.ui.setupUi(self.Form2)
            self.Form2.show()
            Form.hide()



class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(329, 163)
        self.lineEdit = QtWidgets.QLineEdit(Form1)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(0, 20, 57, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form1)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 90, 32))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form1)
        self.textBrowser.setGeometry(QtCore.QRect(180, 10, 111, 141))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form1)
        self.pushButton.clicked.connect(self.start_game)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "Form"))
        self.label.setText(_translate("Form1", "Number :"))
        self.pushButton.setText(_translate("Form1", "submit"))
    def start_game(self):
        a = 0
        b = 100
        num = int(self.lineEdit.text())
        rn = 50
        while(0 < num < 100):
            
            if rn > num:
                self.textBrowser.append("Bot number : %s " % str(rn))
                b = rn-1
                rn = random.randint(a, b)
                app.processEvents()
                sleep(1)

            elif(rn < num):
                a = rn+1
                self.textBrowser.append("Bot number : %s " % str(rn))
                rn = random.randint(a, b)
                app.processEvents()
                sleep(1)

            else:
                self.textBrowser.append('%s Bot Win ' % str(rn))
                app.processEvents()
                break
            


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(256, 273)
        self.pushButton = QtWidgets.QPushButton(Form2)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 90, 32))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form2)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form2)
        self.textBrowser.setGeometry(QtCore.QRect(110, 70, 111, 192))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form2)
        self.pushButton.clicked.connect(self.Start_game)
        QtCore.QMetaObject.connectSlotsByName(Form2)

    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Me"))
        self.pushButton.setText(_translate("Form2", "Submit"))
        self.label.setText(_translate("Form2", "Your Number :"))
        self.a=0
    def Start_game(self):
        num = int(self.lineEdit.text())
        rn= self.a
        if(self.a==0):
            rn = random.randint(0,100)
            self.a=rn
        if rn > num:
            self.textBrowser.append("عددت کوچیکه !!!")
            app.processEvents()
            

        elif(rn < num):
            self.textBrowser.append("عددت بزرگه!!!")
            app.processEvents()
            

        else:
            self.textBrowser.append('بررررردی!!!!!')
            app.processEvents()
            self.a=0
    



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
