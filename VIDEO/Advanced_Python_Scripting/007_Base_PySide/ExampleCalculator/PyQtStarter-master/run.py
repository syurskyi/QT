#!/usr/bin/env python

# Import PyQt classes
import sys
from PyQt4.QtWidgets import QApplication

from pyqtstarter.mainwindow import MainWindow

# Create a Qt application and make a new home in settings
app = QApplication(sys.argv)
app.setApplicationName("PyQtStarter")
app.setOrganizationName("JokeyMagicApps")

# Init a widget
mainwnd = MainWindow()
mainwnd.show()

# Enter Qt application main loop
app.exec_()
sys.exit()
