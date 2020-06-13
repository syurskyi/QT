#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import sys

__author__ = 'syurskyi'
__appname__ = "Dumb dialogs"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")
        self.main_spinbox = QSpinBox()
        self.main_checkbox = QCheckBox("Main Checkbox Value")

        layout = QVBoxLayout()
        layout.addWidget(self.main_spinbox)
        layout.addWidget(self.main_checkbox)
        layout.addWidget(btn)
        self.setLayout(layout)

        self.connect(btn, SIGNAL("clicked()"), self.dialog_open)

    def dialog_open(self):
        init_values = {"mainSpinBox": self.main_spinbox.value(), "mainCheckBox": self.main_checkbox.isChecked()}
        dialog = Dialog(init_values)
        if dialog.exec_():
            self.main_spinbox.setValue(dialog.spinBox.value())
            self.main_checkbox.setChecked(dialog.checkBox.isChecked())


class Dialog(QDialog):

    def __init__(self, init_values, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog.")

        self.checkbox = QCheckBox("Check me out!")
        self.spinbox = QSpinBox()
        button_ok = QPushButton("OK")
        button_cancel = QPushButton("Cancel")

        layout = QGridLayout()
        layout.addWidget(self.spinbox, 0, 0)
        layout.addWidget(self.checkbox, 0, 1)
        layout.addWidget(button_cancel)
        layout.addWidget(button_ok)
        self.setLayout(layout)

        self.spinbox.setValue(init_values["mainSpinBox"])
        self.checkbox.setChecked(init_values["mainCheckBox"])

        self.connect(button_ok, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(button_cancel, SIGNAL("clicked()"), self, SLOT("reject()"))

    def accept(self):

        class GreaterThanFive(Exception):
            pass

        class IsZero(Exception):
            pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive, ("The SpinBox value cannot be greater than 5")
            elif self.spinBox.value() == 0:
                raise IsZero, ("The SpinBox value cannot be equal to 0")
            else:
                QDialog.accept(self)

        except GreaterThanFive, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return

        except IsZero, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return













app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()


