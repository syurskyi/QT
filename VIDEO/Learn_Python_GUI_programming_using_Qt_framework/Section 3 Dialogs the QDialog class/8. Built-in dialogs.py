#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
import sys

__author__ = 'syurskyi'
__appname__ = "__"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        open_button = QPushButton("Open")
        save_button = QPushButton("Save")
        dir_button = QPushButton("Other")
        close_button = QPushButton("Close...")

        self.connect(open_button, SIGNAL("clicked()"), self.open)
        self.connect(save_button, SIGNAL("clicked()"), self.save)

        layout = QVBoxLayout()
        layout.addWidget(open_button)
        layout.addWidget(save_button)
        layout.addWidget(dir_button)
        layout.addWidget(close_button)
        self.setLayout(layout)

    def open(self):

        dir = "."
        file_obj = QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", dir=dir,
                                               filter="Text files (*.txt)")
        print file_obj
        print type(file_obj)
        file_name = file_obj[0]
        file = open(file_name, "r")
        read = file.read()
        file.close()
        print read

    def save(self):
        dir = "."
        file_obj = QFileDialog.getSaveFileName(self, __appname__, dir=dir, filter="Text Files (*.txt)")
        print file_obj
        print type(file_obj)
        contents = "Hello from http://py.bo.vc"
        file_name = file_obj[0]
        open(file_name, mode="w").write(contents)


app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
