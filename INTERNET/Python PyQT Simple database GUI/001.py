import sqlite3 as db
from PyQt5 import QtCore, QtGui
import sys

con = db.connect('results.db', isolation_level=None)
cur = con.cursor()
cur.execute("SELECT * FROM Results")
all_data = cur.fetchall()


class UiDialog(object):
    def setupUi(self, datadb):
        datadb.setObjectName("Dialog")
        datadb.resize(404, 304)
        datadb.setWindowTitle("Database results")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(datadb.sizePolicy().hasHeightForWidth())
        datadb.setSizePolicy(sizePolicy)
        datadb.setMinimumSize(QtCore.QSize(404, 304))
        datadb.setMaximumSize(QtCore.QSize(404, 304))
        self.table = QtGui.QTableWidget(datadb)
        self.table.setGeometry(QtCore.QRect(2, 2, 400, 261))
        self.table.setObjectName("table")
        self.show = QtGui.QPushButton(datadb)
        self.show.setGeometry(QtCore.QRect(2, 270, 400, 31))
        self.show.setObjectName("show")
        self.show.setText("Show results")
        QtCore.QObject.connect(self.show, QtCore.SIGNAL("clicked()"), self.populate)
        QtCore.QMetaObject.connectSlotsByName(datadb)

    def populate(self):
        self.table.setRowCount(len(all_data))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Number', 'Keys', 'Time', 'Tries'])
        for i, item in enumerate(all_data):
            number = QtGui.QTableWidgetItem(str(item[0]))
            keys = QtGui.QTableWidgetItem(item[1])
            time = QtGui.QTableWidgetItem(str(item[2]))
            tries = QtGui.QTableWidgetItem(str(item[3]))
            self.table.setItem(i, 0, number)
            self.table.setItem(i, 1, keys)
            self.table.setItem(i, 2, time)
            self.table.setItem(i, 3, tries)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_conf = QtGui.QDialog()
    ui = UiDialog()
    ui.setupUi(main_conf)
    main_conf.show()
    ret = app.exec_()
    sys.exit(ret)