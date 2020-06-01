from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
import sys
import MySQLdb as mdb


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Insert Data"
        self.top = 100
        self.left = 100
        self.width = 300
        self.height = 100


        self.InitWindow()


    def InitWindow(self):

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        vbox = QVBoxLayout()

        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Please Enter Your Name')
        self.name.setStyleSheet('background:yellow')
        self.name.setFont(QtGui.QFont("Sanserif", 15))

        vbox.addWidget(self.name)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText('Please Enter Your Email')
        self.email.setFont(QtGui.QFont("Sanserif", 15))
        self.email.setStyleSheet('background:yellow')

        vbox.addWidget(self.email)

        self.button = QPushButton("Insert Data", self)
        self.button.setStyleSheet('background:green')

        self.button.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.InsertData)

        self.setLayout(vbox)

        self.show()


    def InsertData(self):
        con = mdb.connect('localhost', 'root', '', 'pyqt5')
        with con:
            cur = con.cursor()

            cur.execute("INSERT INTO data(name, email)"
                        "VALUES('%s', '%s')" % (''.join(self.name.text()),
                                                  ''.join(self.email.text())))


            QMessageBox.about(self,'Connection', 'Data Inserted Successfully')
            self.close()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())