import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtWidgets import QAction, QWidget, QMenuBar, QMenu, QLineEdit
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Game Launcher"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        #creating button for some unknown reason
        button = QPushButton("Exit Application", self)
        button.move(200,200)
        button.setToolTip("<h1> Please Click me, I'm Begging you") #setting up the tool tip that will show up
        button.clicked.connect(self.close_app) #setting up the on click event

        #creating menu bar
        mainMenu = self.menuBar()

        #creating menus for the menu bar
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        #creating exit action to add in file menu
        exitButton = QAction( "Exit", self)
        exitButton.setStatusTip("Exit Application")
        exitButton.setShortcut("Alt + F4")
        exitButton.triggered.connect(self.close)
        #adding action to the file menu
        fileMenu.addAction(exitButton)

        #check menu action
        viewAction = QAction("View Status Bar", self, checkable = True)
        viewAction.setStatusTip("enable/disable status bar")
        viewAction.setChecked(True)
        viewAction.triggered.connect(self.toggle_menu)
        #adding action the view menu
        viewMenu.addAction(viewAction)

        #help action 
        aboutUsAction = QAction("About Us", self)
        aboutUsAction.setStatusTip("About Us")
        aboutUsAction.triggered.connect(lambda: self.show_alert_box("This is demo application by Anim Malvat"))
        #adding it to the help menu
        helpMenu.addAction(aboutUsAction)
        
        #adding actions for toolbar
        folderIcon = QIcon("folder.png")
        openFolderAction = QAction(folderIcon, "Open Folder", self)
        openFolderAction.setToolTip("Open Folder")
        openFolderAction.setShortcut("Ctrl + O")
        openFolderAction.triggered.connect(lambda: self.show_alert_box("Open Folder clicked"))

        #creating another action for toolbar
        editFolderAction = QAction(folderIcon, "Edit File", self)
        editFolderAction.setToolTip("Edit File")

        #create toolbar and add the tool into it
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(openFolderAction)
        self.toolbar.addAction(editFolderAction)
        
        #adding line edit
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(500, 100)

        self.showTextButton = QPushButton("Show Text", self)
        self.showTextButton.move(500, 130)
        self.showTextButton.clicked.connect(self.show_button_click)

        #initializing the window using those variable
        self.init_window()
        
    #initializing the window with methods associated with main window
    def init_window(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowTitle(self.title)
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Message is ready")
        self.statusbar.show()
        self.show()

    #this function is called when exit from the menu is clicked
    def close_app(self):
        reply = QMessageBox().question(self, "Warning", "Are you sure ?", 
                                        QMessageBox.Yes | QMessageBox.No, 
                                        QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

    #this is called when view status is checked or unchecked
    def toggle_menu(self, state):
        if state:
            self.statusbar.show()
        else: 
            self.statusbar.hide()

    #adding context menu to the application
    def contextMenuEvent(self, event):
        #creating the menu
        contextMenu = QMenu(self)
        #adding actions to the menu
        newAction = contextMenu.addAction("New")
        viewAction = contextMenu.addAction("View")
        exitAction = contextMenu.addAction("Exit")
        #adding the action to the window
        action = contextMenu.exec(self.mapToGlobal(event.pos()))
        #setting up the functionality
        if action == exitAction: #use the same name as the action
            self.close_app()
        elif action == newAction:
            self.show_alert_box("new action is clicked") #click functionality for the new action
        elif action == viewAction: 
            self.show_alert_box("view action is clicked")

    #this function shows an alert box with message
    def show_alert_box(self, message):
        alert = QMessageBox(self)
        alert.setWindowTitle("Information")
        alert.setText(message)
        alert.show()

    #function for clicking show button
    def show_button_click(self):
        txt = self.lineEdit.text()
        self.show_alert_box(txt)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())