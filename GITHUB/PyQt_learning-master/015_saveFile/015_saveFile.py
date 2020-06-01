import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Creating the menu bar")
        self.setWindowIcon(QtGui.QIcon('pondilogo.jpg'))

        #main menu

        extractAction =QtGui.QAction("&LINK UP", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)

        #add editor
        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        #open File
        openFile =QtGui.QAction("&Open File", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.open_file)

        #Save File
        saveFile =QtGui.QAction("&Save File", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.save_file)

        self.statusBar()

        mainMenu =self.menuBar()
        #File menu definition
        fileMenu =mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        #Editor menu definition
        editorMenu =mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)


        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)
        
        extractAction = QtGui.QAction('Extraction',self)
        extractAction.triggered.connect(self.close_application)
        self.toolBar =self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)


        #Font Widget
        fontChoice = QtGui.QAction('Font',self)
        fontChoice.triggered.connect(self.font_choice)
        #self.toolBar =self.addToolBar("Font")
        self.toolBar.addAction(fontChoice)

        
        #Checkbox
        checkBox = QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(300,30)
        #checkBox.toggle() is used when you want to automatically check the box
        checkBox.stateChanged.connect(self.enlarge_window)

        #progressBar
        self.progress =QtGui.QProgressBar(self)
        self.progress.setGeometry(200,80,250,20)

        self.btn =QtGui.QPushButton("Download",self)
        self.btn.move(200,120)
        self.btn.clicked.connect(self.download)

        #Drop down and Styles
        self.styleChoice = QtGui.QLabel("Wndows vista", self)
        comboBox =QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("Windows")

        comboBox.move(50,250)
        self.styleChoice.move(50,150)
        comboBox.activated[str].connect(self.style_choice)

        #Font Colors
        #color = QtGui.QColor(0,0,0)

        fontColor = QtGui.QAction('Font BG Color', self)
        fontColor.triggered.connect(self.color_picker)

        self.toolBar.addAction(fontColor)

        #Add Calendar
        cal =QtGui.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)


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

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))

    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def color_picker(self):
        color =QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget {backround-color: %s}" %color.name())

    def editor(self):
        self.textEdit =QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')

        self.editor()

        with file:
            text =file.read()
            self.textEdit.setText(text)

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text =self.textEdit.toPlainText()
        file.write(text)
        file.close()
            



def main():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()