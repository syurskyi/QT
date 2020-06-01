import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Creating the menu bar")
        self.setWindowIcon(QtGui.QIcon('pondilogo.jpg'))

        extractAction =QtGui.QAction("&LINK UP", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu =self.menuBar()
        fileMenu =mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu =mainMenu.addMenu('&Faith')
        fileMenu.addAction(extractAction)


        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        
        extractAction = QtGui.QAction(QtGui.QIcon('pondilogo.png'),'flee the scene',self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar =self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        
        #Checkbox
        checkBox = QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(100,25)
        #checkBox.toggle() is used when you want to automatically check the box
        checkBox.stateChanged.connect(self.enlarge_window)

        #progressBar
        self.progress =QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn =QtGui.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)


        self.show()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print('Extracting now......')
            sys.exit()
        else:
            pass

    def enlarge_window(self, state):
        if state ==QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()