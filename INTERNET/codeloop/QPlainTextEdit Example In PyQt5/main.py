from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Plain TextEdit"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        plainText = QPlainTextEdit()
        plainText.setPlaceholderText("This is some text for our plaintextedit")

        #plainText.setReadOnly(True)


        text = "Please subscribe the channel and like the videos"

        plainText.appendPlainText(text)

        plainText.setUndoRedoEnabled(False)





        vbox.addWidget(plainText)

        self.setLayout(vbox)


        self.show()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())