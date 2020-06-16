# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
import sqlite3
from os import path

from PyQt5.uic import loadUiType

FORM_CLASS,_ = loadUiType(path.join(path.dirname('__file__'), "main.ui"))


class Main(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_buttons()

    def handle_buttons(self):
        self.refresh_btn.clicked.connect(self.get_data)
        self.search_btn.clicked.connect(self.search)

    def get_data(self):
        # Connect to Sqlite3 database add fill GUI table with
        db = sqlite3.connect("parts.db")
        cursor = db.cursor()
        
        command = """SELECT * from parts_table"""
        
        result = cursor.execute(command)
        
        self.table.setRowCount(0)
        
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        cursor2 = db.cursor()
        cursor3 = db.cursor()

        parts_nbr = """SELECT COUNT (DISTINCT PartName) from parts_table"""
        ref_nbr = """SELECT COUNT (DISTINCT Reference) from parts_table"""

        result_ref_nbr = cursor2.execute(ref_nbr)
        result_parts_nbr = cursor3.execute(parts_nbr)

        self.lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
        self.lbl_parts_nbr.setText(str(result_parts_nbr.fetchone()[0]))

        # Display 4 results: Min, Max Nbr of holes in addition to their respective reference names

        cursor4 = db.cursor()
        cursor5 = db.cursor()

        min_hole = """SELECT MIN(NumberOfHoles), Reference FROM parts_table"""
        max_hole = """SELECT MAX(NumberOfHoles), Reference FROM parts_table"""

        result_min_hole = cursor4.execute(min_hole)
        result_max_hole = cursor5.execute(max_hole)
        
        r1 = result_min_hole.fetchone()
        r2 = result_max_hole.fetchone()

        # Print Results in QLabels
        
        self.lbl_min_hole.setText(str(r1[0]))
        self.lbl_max_hole.setText(str(r2[0]))

        self.lbl_min_hole_2.setText(str(r1[0]))
        self.lbl_min_hole_2.setText(str(r2[0]))
        

    def search(self):

        db = sqlite3.connect("parts.db")
        cursor = db.cursor()
        nbr = int(self.count_filter_txt.text())

        command = """SELECT * from parts_table WHERE count <= ?"""

        result = cursor.execute(command, [nbr])

        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))







def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

