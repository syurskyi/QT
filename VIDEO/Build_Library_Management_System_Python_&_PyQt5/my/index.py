from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import os
import sqlite3

# ui = loadUiType('library.ui')[0]
ui,_ = loadUiType('library.ui')

# ui = loadUiType('library.ui')[0]
# ui,_ = loadUiType('library.ui')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui_changes()
        self.handle_buttons()

        self.show_author()
        self.show_category()
        self.show_publisher()

        self.show_category_combobox()
        self.show_author_combobox()
        self.show_publisher_combobox()

        self.show_all_books()

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

        self.pushButton_7.clicked.connect(self.add_new_book)

        self.pushButton_14.clicked.connect(self.add_category)
        self.pushButton_15.clicked.connect(self.add_author)
        self.pushButton_16.clicked.connect(self.add_publisher)

        self.pushButton_7.clicked.connect(self.add_new_book)
        self.pushButton_9.clicked.connect(self.search_books)
        self.pushButton_8.clicked.connect(self.edit_books)
        self.pushButton_10.clicked.connect(self.delete_books)

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

    def show_all_books(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_code,book_name,book_description,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_5.setRowCount(0)
        self.tableWidget_5.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close

    def add_new_book(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        self.cur.execute("""
        INSERT INTO book(book_name, book_description, book_code, book_category, book_author, book_publisher, book_price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (book_title, book_description, book_code, book_category, book_author, book_publisher ,book_price))

        self.db.commit()
        self.statusBar().showMessage("New Book has been added")

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')
        self.show_all_books()

    def search_books(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        sql = """SELECT * FROM book WHERE book_name = ?"""
        self.cur.execute(sql, [(book_title)])

        data = self.cur.fetchone()

        print(data)
        self.lineEdit_8.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_7.setText(data[3])
        self.comboBox_7.setCurrentText(data[4])
        self.comboBox_8.setCurrentText(data[5])
        self.comboBox_6.setCurrentText(data[6])
        self.lineEdit_6.setText(str(data[7]))

    def edit_books(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_8.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_7.currentText()
        book_author = self.comboBox_8.currentText()
        book_publisher = self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()

        search_book_title = self.lineEdit_5.text()

        self.cur.execute('''
                    UPDATE book SET book_name=%s ,book_description=%s ,book_code=%s ,book_category=%s ,book_author=%s ,book_publisher=%s ,book_price=%s WHERE book_name = %s            
                ''', (book_title, book_description, book_code, book_category, book_author, book_publisher, book_price,
                      search_book_title))

        self.db.commit()
        self.statusBar().showMessage('book updated')
        self.show_all_books()

    def delete_books(self):

        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        book_title = self.lineEdit_5.text()

        warning = QMessageBox.warning(self, 'Delete Book', "are you sure you want to delete this book",
                                      QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM book WHERE book_name = %s '''
            self.cur.execute(sql, [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.show_all_books

    # #################################################################################################################
    # ############################## Users ############################################################################

    def add_new_user(self):
        pass

    def login(self):
        pass

    def edit_user(self):
        pass

    # #################################################################################################################
    # ############################## Settings #########################################################################

    def add_category(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()
        
        category_name = self.lineEdit_19.text()
        
        self.cur.execute("""INSERT INTO category (category_name) VALUES (?)""", (category_name, ))

        self.db.commit()
        self.statusBar().showMessage("New Category Added")
        self.lineEdit_19.setText('')
        self.show_category()
        self.show_category_combobox()

    def show_category(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT category_name FROM category""")
        data= self.cur.fetchall()
        # print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    def add_author(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()

        self.cur.execute("""INSERT INTO authors (author_name) VALUES (?)""", (author_name,))

        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage("New Author Added")
        self.show_author()
        self.show_author_combobox()

    def show_author(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT author_name FROM authors""")
        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)

    def add_publisher(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()

        self.cur.execute("""INSERT INTO publisher (publisher_name) VALUES (?)""", (publisher_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage("New Publisher Added")
        self.show_publisher()
        self.show_publisher_combobox()

    def show_publisher(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT publisher_name FROM publisher""")
        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)

    # #################################################################################################################
    # ##############################  show settings data in UI ########################################################

    def show_category_combobox(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT category_name FROM category""")
        data = self.cur.fetchall()
        # print(data)

        self.comboBox_3.clear()

        for category in data:
            # print(category[0])
            self.comboBox_3.addItem(category[0])

    def show_author_combobox(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT author_name FROM authors""")
        data = self.cur.fetchall()

        self.comboBox_4.clear()

        for author in data:
            self.comboBox_4.addItem(author[0])


    def show_publisher_combobox(self):
        self.db = sqlite3.connect(resource_path("db.db"))
        self.cur = self.db.cursor()

        self.cur.execute("""SELECT publisher_name FROM publisher""")
        data = self.cur.fetchall()

        self.comboBox_5.clear()

        for publisher in data:
            self.comboBox_5.addItem(publisher[0])



def main():
    app = QApplication(sys.argv)
    window =MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()