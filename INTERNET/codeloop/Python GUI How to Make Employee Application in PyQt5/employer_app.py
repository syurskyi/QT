from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon


class Window(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(574, 470)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.pushButton_edit = QtWidgets.QPushButton(Dialog)
        self.pushButton_edit.setObjectName("pushButton_edit")
        self.verticalLayout.addWidget(self.pushButton_edit)
        self.pushButton_remove = QtWidgets.QPushButton(Dialog)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.verticalLayout.addWidget(self.pushButton_remove)
        self.pushButton_up = QtWidgets.QPushButton(Dialog)
        self.pushButton_up.setObjectName("pushButton_up")
        self.verticalLayout.addWidget(self.pushButton_up)
        self.pushButton_down = QtWidgets.QPushButton(Dialog)
        self.pushButton_down.setObjectName("pushButton_down")
        self.verticalLayout.addWidget(self.pushButton_down)
        self.pushButton_sort = QtWidgets.QPushButton(Dialog)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.verticalLayout.addWidget(self.pushButton_sort)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setObjectName("pushButton_close")
        self.verticalLayout.addWidget(self.pushButton_close)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_edit.clicked.connect(self.edit)
        self.pushButton_remove.clicked.connect(self.remove)
        self.pushButton_up.clicked.connect(self.up)
        self.pushButton_down.clicked.connect(self.down)
        self.pushButton_sort.clicked.connect(self.sort)
        self.pushButton_close.clicked.connect(self.close)

        self.Employee()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Employee"))
        Dialog.setWindowIcon(QIcon("icon.png"))
        self.pushButton_add.setText(_translate("Dialog", "Add"))
        self.pushButton_edit.setText(_translate("Dialog", "Edit"))
        self.pushButton_remove.setText(_translate("Dialog", "Remove"))
        self.pushButton_up.setText(_translate("Dialog", "Up"))
        self.pushButton_down.setText(_translate("Dialog", "Down"))
        self.pushButton_sort.setText(_translate("Dialog", "Sort"))
        self.pushButton_close.setText(_translate("Dialog", "Close"))

    def Employee(self):
        self.employess = ["John", "Doe", "Tom", "Karim", "Ahmad"]
        self.listWidget.addItems(self.employess)
        self.listWidget.setCurrentRow(0)

    def add(self):
        row = self.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, "Employee Dialog", "Enter Employee Name")
        if ok and text is not None:
            self.listWidget.insertItem(row, text)

    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is not None:
            string, ok = QInputDialog.getText(self, "Employee Dialog", "Edit Employee Name",
                                              QLineEdit.Normal, item.text())
            if ok and string is not None:
                item.setText(string)

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is None:
            return

        reply = QMessageBox.question(self, "Remove Employee", "Do You Want To Remove Employee " + str(item.text()),
                QMessageBox.Yes|QMessageBox.No)


        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item

    def up(self):
        row = self.listWidget.currentRow()
        if row >= 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1, item)
            self.listWidget.setCurrentItem(item)

    def down(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1, item)
            self.listWidget.setCurrentItem(item)

    def sort(self):
        self.listWidget.sortItems()

    def close(self):
        quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Window()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())