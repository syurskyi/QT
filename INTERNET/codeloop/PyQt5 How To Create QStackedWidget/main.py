from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QStackedWidget, QLabel, QPushButton
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui


class StackedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 StackedWidget"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 200
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.stackedWidget()
        self.show()
    def stackedWidget(self):
        vbox = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        vbox.addWidget(self.stackedWidget)
        for x in range(0,8):
            label = QLabel("Stacked Child: " + str(x))
            label.setFont(QtGui.QFont("sanserif", 15))
            label.setStyleSheet('color:red')
            self.stackedWidget.addWidget(label)
            self.button = QPushButton("Stack" + str(x))
            self.button.setStyleSheet('background-color:green')
            self.button.page = x
            self.button.clicked.connect(self.btn_clicked)
            vbox.addWidget(self.button)
        self.setLayout(vbox)
    def btn_clicked(self):
        self.button = self.sender()
        self.stackedWidget.setCurrentIndex(self.button.page - 1)


App = QApplication(sys.argv)
window = StackedWidget()
sys.exit(App.exec())