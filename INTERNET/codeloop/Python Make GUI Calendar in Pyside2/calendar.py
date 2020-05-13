from PySide2.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
import sys
from PySide2.QtGui import QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Calendar")
        self.setGeometry(300,200,500,400)
        self.setIcon()
        self.createCalendar()
        self.show()

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createCalendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        vbox.addWidget(self.calendar)
        self.setLayout(vbox)


myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()