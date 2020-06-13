#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'syurskyi'

from PySide.QtGui import *
from PySide.QtCore import *
import sys

import urllib


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.get_data()
        rates = sorted(self.rates.keys())

        date_label = QLabel(date)

        self.from_combobox = QComboBox()
        self.to_combobox = QComboBox()

        self.from_combobox.addItems(rates)
        self.to_combobox.addItems(rates)

        self.from_spinbox = QDoubleSpinBox()
        self.from_spinbox.setRange(0.01, 1000)
        self.from_spinbox.setValue(1.00)

        self.to_label = QLabel("1.00")

        layout = QGridLayout()
        layout.addWidget(date_label, 0, 0)
        layout.addWidget(self.from_combobox, 1, 0)
        layout.addWidget(self.to_combobox, 2, 0)
        layout.addWidget(self.from_spinbox, 1, 1)
        layout.addWidget(self.to_label, 2, 1)
        self.setLayout(layout)


        self.from_combobox.currentIndexChanged.connect(self.update_ui)
        self.to_combobox.currentIndexChanged.connect(self.update_ui)
        self.from_spinbox.valueChanged.connect(self.update_ui)



    def get_data(self):
        self.rates = {}

        try:
            date = "Unknown"

            fh = urllib.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing")):
                    continue

                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass

            return "Exchange rates date: " + date
        except Exception, e:
            return "Failued to download:\n%s" % e

    def update_ui(self):

        from_ = self.from_combobox.currentText()
        to = self.to_combobox.currentText()

        results = (self.rates[from_] / self.rates[to]) * self.from_spinbox.value()

        self.to_label.setText("%0.2f" % results)


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()






