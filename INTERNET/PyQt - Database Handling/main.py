import sys
from PyQt5 import QtCore, QtGui, QtSql
import sportsconnection


def initializeModel(model):
    model.setTable('sportsmen')
    model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")


def createView(title, model):
    view = QtGui.QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


def addrow():
    print
    model.rowCount()
    ret = model.insertRows(model.rowCount(), 1)
    print
    ret


def findrow(i):
    delrow = i.row()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('sports.db')
    model = QtSql.QSqlTableModel()
    delrow = -1
    initializeModel(model)

    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QtGui.QDialog()
    layout = QtGui.QVBoxLayout()
    layout.addWidget(view1)

    button = QtGui.QPushButton("Add a row")
    button.clicked.connect(addrow)
    layout.addWidget(button)

    btn1 = QtGui.QPushButton("del a row")
    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
    layout.addWidget(btn1)

    dlg.setLayout(layout)
    dlg.setWindowTitle("Database Demo")
    dlg.show()
    sys.exit(app.exec_())