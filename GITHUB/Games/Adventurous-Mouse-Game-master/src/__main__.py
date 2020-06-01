# -*- coding: utf-8 -*-
from os import path
from sys import argv

from PyQt5.QtWidgets import QApplication

from include.mainwindow import MainWindow


if __name__ == '__main__':
    app = QApplication([])
    currentPath = path.dirname(path.realpath(argv[0])).replace('\\', '/') + '/'
    window = MainWindow(currentPath)
    exit(app.exec_())
