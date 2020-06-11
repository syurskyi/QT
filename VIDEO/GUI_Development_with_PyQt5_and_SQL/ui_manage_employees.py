# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_new_employee import EmployeeDialog
from database import Database
from ui_salary_position import EmployeeInfoWindow


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(853, 718)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.upperGridLayout = QtWidgets.QGridLayout()
        self.upperGridLayout.setObjectName("upperGridLayout")
        spacerItem = QtWidgets.QSpacerItem(1098, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upperGridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.upperGridLayout, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_2.addWidget(self.toolButton, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.idLabel.setFont(font)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtWidgets.QLineEdit(self.widget)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.idLineEdit)
        self.firstNameLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.firstNameLabel.setFont(font)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.firstNameLineEdit.setObjectName("firstNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lastNameLabel.setFont(font)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.lastNameLineEdit.setObjectName("lastNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.birthdayLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.birthdayLabel.setFont(font)
        self.birthdayLabel.setObjectName("birthdayLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthdayLabel)
        self.birthdayLineEdit = QtWidgets.QLineEdit(self.widget)
        self.birthdayLineEdit.setText("")
        self.birthdayLineEdit.setObjectName("birthdayLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthdayLineEdit)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(128, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.departmentNameLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.departmentNameLabel.setFont(font)
        self.departmentNameLabel.setObjectName("departmentNameLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.departmentNameLabel)
        self.departmentNameLineEdit = QtWidgets.QLineEdit(self.widget)
        self.departmentNameLineEdit.setObjectName("departmentNameLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.departmentNameLineEdit)
        self.salaryLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.salaryLabel.setFont(font)
        self.salaryLabel.setObjectName("salaryLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.salaryLabel)
        self.salaryLineEdit = QtWidgets.QLineEdit(self.widget)
        self.salaryLineEdit.setObjectName("salaryLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.salaryLineEdit)
        self.positionLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.positionLabel.setFont(font)
        self.positionLabel.setObjectName("positionLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.positionLabel)
        self.positionLineEdit = QtWidgets.QLineEdit(self.widget)
        self.positionLineEdit.setObjectName("positionLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.positionLineEdit)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(228, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 2)
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)
        self.bottomGridLaout = QtWidgets.QGridLayout()
        self.bottomGridLaout.setObjectName("bottomGridLaout")
        spacerItem7 = QtWidgets.QSpacerItem(998, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomGridLaout.addItem(spacerItem7, 0, 0, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setObjectName("backButton")
        self.bottomGridLaout.addWidget(self.backButton, 0, 1, 1, 1)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.bottomGridLaout.addWidget(self.newButton, 0, 2, 1, 1)
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setObjectName("exportButton")
        self.bottomGridLaout.addWidget(self.exportButton, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.bottomGridLaout, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manage Empoyee"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.idLabel.setText(_translate("MainWindow", "Id"))
        self.firstNameLabel.setText(_translate("MainWindow", "First Name"))
        self.lastNameLabel.setText(_translate("MainWindow", "Last Name"))
        self.birthdayLabel.setText(_translate("MainWindow", "Birthday"))
        self.departmentNameLabel.setText(_translate("MainWindow", "Department Name"))
        self.salaryLabel.setText(_translate("MainWindow", "Salary"))
        self.positionLabel.setText(_translate("MainWindow", "Position"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.backButton.setText(_translate("MainWindow", "Back"))
        self.newButton.setText(_translate("MainWindow", "New"))
        self.exportButton.setText(_translate("MainWindow", "Export"))


class EmployeeWindow(QtWidgets.QMainWindow):

    def __init__(self, mainMenu):
        super(EmployeeWindow, self).__init__()
        self.mainMenu = mainMenu

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_table()

        self.ui.tableWidget.viewport().installEventFilter(self)

        self.ui.backButton.clicked.connect(self.on_backButton_clicked)
        self.ui.newButton.clicked.connect(self.on_newButton_clicked)

    def init_table(self):
        # pass
        self.db = Database()
        employee_list = self.db.get_employee_full_info()
        header_list = employee_list[0]
        value_list = employee_list[1]

        no_rows = len(value_list)
        print(no_rows)
        no_columns = len(header_list)
        print(no_columns)

        self.ui.tableWidget.setRowCount(no_rows)
        self.ui.tableWidget.setColumnCount(no_columns)

        self.ui.tableWidget.setHorizontalHeaderLabels(tuple(header_list))
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for row in range(no_rows):
            for col in range(no_columns):
                # print(s)
                self.ui.tableWidget.setItem(row, col, QTableWidgetItem(str(value_list[row][col])))

    def eventFilter(self, obj, event):
        if (obj == self.ui.tableWidget.viewport() and event.type() == QEvent.MouseButtonPress):

            if event.button() == Qt.RightButton:
                idx = self.ui.tableWidget.indexAt(event.pos())

                if idx.isValid():
                    deleteAction = QAction("Delete", self)
                    deleteAction.triggered.connect(self.delete_action_triggered)

                    modifyAction = QAction('Modify', self)
                    modifyAction.setObjectName(str(idx.row()))
                    modifyAction.triggered.connect(self.modify_action_triggered)

                    contextMenu = QMenu(self)
                    contextMenu.addAction(deleteAction)
                    contextMenu.addAction(modifyAction)

                    contextMenu.exec(event.globalPos())

        return QMainWindow.eventFilter(self, obj, event)

    def delete_action_triggered(self):
        print("Delete")

    def modify_action_triggered(self):
        print("Modify")
        row = int(QObject.sender(self).objectName())
        id = int(self.ui.tableWidget.item(row, 0).text())
        self.employeeInfoWindow = EmployeeInfoWindow(id)
        self.employeeInfoWindow.show()


    def on_backButton_clicked(self):
        self.hide()
        self.mainMenu.show()

    def on_newButton_clicked(self):
        self.employeeDialog = EmployeeDialog()
        result = self.employeeDialog.exec()

        if result == QtWidgets.QDialog.Accepted:
            self.db.insert_employee(self.employeeDialog.employeeInfo)



