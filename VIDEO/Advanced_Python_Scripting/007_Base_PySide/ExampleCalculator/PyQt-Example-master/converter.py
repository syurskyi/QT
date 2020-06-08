#!/usr/bin/python

import sys
import atexit
from PyQt4 import QtGui, QtCore
from interface import Ui_MainWindow


# Cargar nuestro archivo .ui
# Ui_MainWindow = uic.loadUiType("interface.ui")[0]

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.actionExit.setShortcut("Ctrl+Q")
        self.error_msg = 'Please insert valid a Temperature.'

    @QtCore.pyqtSignature('')
    def on_btn_celcius_clicked(self):
        try:
            result = float(self.input_temp.text()) * 9 / 5.0 + 32 + 0.5
            self.set_result(str(round(result, 2)) + ' F°')
        except:
            self.set_result(self.format_output(self.error_msg, 'red'))

    @QtCore.pyqtSignature('')
    def on_btn_faren_clicked(self):
        try:
            result = ((float(self.input_temp.text()) - 32) * 5) / 9
            self.set_result(str(round(result, 2)) + ' C°')
        except:
            self.set_result(self.format_output(self.error_msg, 'red'))

    @QtCore.pyqtSignature('')
    def on_actionExit_triggered(self):
        sys.exit()

    def set_result(self, message):
        self.text_result.setText(self.format_output(message))

    def format_output(self, text, color="blue"):
        styled_text = '<html><body><p align="center"><span style=" font-size:26pt; font-weight:600; color: %s">%s</span></p></body></html>' % (color, text)
        return styled_text


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.png'))
    MyApp = MyWindowClass()
    MyApp.show()
    sys.exit(app.exec_())
