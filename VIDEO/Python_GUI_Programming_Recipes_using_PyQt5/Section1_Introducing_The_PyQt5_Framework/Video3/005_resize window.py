# class inheriting from QMainWindow
# resize window


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class GUI(QMainWindow):             # inherit from QMainWindow
    def __init__(self):
        super().__init__()          # initialize super class, which creates the Window

        self.initUI()

    def initUI(self):                       # set properties and add widgets
        self.setWindowTitle('PyQt5 GUI')    # refer to Window as self

        self.resize(400, 300)                # resize window (width, height)


if __name__ == '__main__':
    app = QApplication(sys.argv)        # create Application
    gui = GUI()                         # create instance of class
    gui.show()                          # show the constructed PyQt window
    sys.exit(app.exec_())               # execute the application
