import sys

from PyQt5.QtWidgets import QDialog, QApplication

from LineEditClass import *

class Student:
    name = ""
 
    def __init__(self, name):
        self.name = name
 
    def printName(self):
        return self.name

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispmessage)
        self.show()

    def dispmessage(self):
        studentObj=Student(self.ui.lineEditName.text())  
        self.ui.labelResponse.setText("Hello "+studentObj.printName())



if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main = MyForm()
    main.show()

    if app is not None:
        app.exec_()