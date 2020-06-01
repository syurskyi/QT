from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Labels"
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
        label = QLabel("This Is PyQt5 Labels")
        vbox.addWidget(label)
        label2 = QLabel("This Is PyQt5 GUI Applicaition Development, Hello")
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)
        self.setLayout(vbox)
        self.show()
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())