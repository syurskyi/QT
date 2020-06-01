from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,  QAction, QTextEdit
import sys
from PyQt5.QtGui import QIcon


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 QToolbar"
        self.top = 200
        self.left = 500
        self.width = 680
        self.height = 480
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createEditor()
        self.CreateMenu()
        self.show()
    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        helpMenu = mainMenu.addMenu('Help')
        copyAction = QAction(QIcon("copy.png"), 'Copy', self)
        copyAction.setShortcut("Ctrl+C")
        fileMenu.addAction(copyAction)
        saveAction = QAction(QIcon("Save.png"), 'Save', self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        pasteAction = QAction(QIcon("Paste.png"), 'Paste', self)
        pasteAction.setShortcut("Ctrl+P")
        fileMenu.addAction(pasteAction)
        exiteAction = QAction(QIcon("exit.png"), 'Exit', self)
        exiteAction.setShortcut("Ctrl+E")
        exiteAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exiteAction)
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(exiteAction)
    def exitWindow(self):
        self.close()
    def createEditor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())