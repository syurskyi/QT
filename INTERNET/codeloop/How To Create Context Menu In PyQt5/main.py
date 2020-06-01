from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Context Menu"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction("New")
        openAct = contextMenu.addAction("Open")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            self.close()


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())