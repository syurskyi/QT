#--------------------------------------------------

# class inheriting from QMainWindow
# add separator and Exit menu item

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.QtGui import QIcon


class GUI(QMainWindow):             # inherit from QMainWindow
    def __init__(self):
        super().__init__()          # initialize super class, which creates the Window

        self.initUI()

    def initUI(self):                       # set properties and add widgets
        self.setWindowTitle('PyQt5 GUI')    # refer to Window as self

        self.statusBar().showMessage('Text in statusbar')

        menubar = self.menuBar()                # create menu bar

        file_menu = menubar.addMenu('File')
        new_icon = QIcon('icons/new_icon.png')          # create icon
        new_action = QAction(new_icon, 'New', self)     # add icon to menu

        file_menu.addAction(new_action)         # add Action to menu
        new_action.setStatusTip('New File')     # statusBar updated

        file_menu.addSeparator()                # add separator line between menu items

        exit_icon = QIcon('icons/exit_icon.png')          # create icon
        exit_action = QAction(exit_icon, 'Exit', self)    # create Exit Action
        exit_action.setStatusTip('Click to exit the application')
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu('Edit')     # add a second menu

        self.resize(400,300)                    # resize window (width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create Application
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application

