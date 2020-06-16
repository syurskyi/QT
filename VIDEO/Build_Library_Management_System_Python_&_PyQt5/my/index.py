from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

# ui = loadUiType('library.ui')[0]
ui,_ = loadUiType('library.ui')

# ui = loadUiType('library.ui')[0]
# ui,_ = loadUiType('library.ui')


class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui_changes()
        self.handle_buttons()

    def handel_ui_changes(self):
        self.hidding_themes()
        self.tabWidget.tabBar().setVisible(False)

    def handle_buttons(self):
        self.pushButton_5.clicked.connect(self.show_themes)
        self.pushButton_17.clicked.connect(self.hidding_themes)

        self.pushButton.clicked.connect(self.open_day_to_day_tab)
        self.pushButton_2.clicked.connect(self.open_books_tab)
        self.pushButton_26.clicked.connect(self.open_clients_tab)
        self.pushButton_3.clicked.connect(self.open_users_tab)
        self.pushButton_4.clicked.connect(self.open_settings_tab)


    def show_themes(self):
        self.groupBox_3.show()

    def hidding_themes(self):
        self.groupBox_3.hide()
    # #################################################################################################################
    # ############################## openning tabs ####################################################################

    def open_day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def open_clients_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(4)

    # #################################################################################################################
    # ############################## Books ############################################################################

    def add_new_book(self):
        pass

    def search_books(self):
        pass

    def edit_book(self):
        pass

    def delete_books(self):
        pass

    # #################################################################################################################
    # ############################## Users ############################################################################

    def add_new_user(self):
        pass

    def login(self):
        pass

    def edit_user(self):
        pass



def main():
    app = QApplication(sys.argv)
    window =MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()