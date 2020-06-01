#!/bin/python3
# -*- coding: utf-8 -*-
print('QTST-ADV')
print('')
import sys
# sys.path.append('$HOME/.config/qtst-adv/apprc')
import apprc as qcfg
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
        app = QApplication(sys.argv)
        w = QWidget()
        w.resize(qcfg.x, qcfg.y)
        w.setWindowTitle('ParkCity\'s Qtst Adv')
        w.setWindowIcon(QIcon('ico.png'))
        w.show()
        sys.exit(app.exec_())
