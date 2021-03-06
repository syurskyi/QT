# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 350)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setVerticalSpacing(50)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight)

        self.firstNameLabel = QtWidgets.QLabel(Dialog)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameValueLabel = QtWidgets.QLabel(Dialog)
        self.firstNameValueLabel.setObjectName("firstNameValueLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.firstNameValueLabel)
        self.lastNameLabel = QtWidgets.QLabel(Dialog)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameValueLabel = QtWidgets.QLabel(Dialog)
        self.lastNameValueLabel.setObjectName("lastNameValueLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNameValueLabel)
        self.currentPositionLabel = QtWidgets.QLabel(Dialog)
        self.currentPositionLabel.setObjectName("currentPositionLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.currentPositionLabel)
        self.currentPositionValueLabel = QtWidgets.QLabel(Dialog)
        self.currentPositionValueLabel.setObjectName("currentPositionValueLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.currentPositionValueLabel)
        self.newPositionLabel = QtWidgets.QLabel(Dialog)
        self.newPositionLabel.setObjectName("newPositionLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.newPositionLabel)
        self.newPositionLineEdit = QtWidgets.QLineEdit(Dialog)
        self.newPositionLineEdit.setPlaceholderText("")
        self.newPositionLineEdit.setObjectName("newPositionLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.newPositionLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)

        Dialog.setStyleSheet("""
            QDialog {
                background-color: rgb(55,64,88);
            }

            QLabel {
                color: white;
                font-size: 8pt;
                font-family: Verdana;
            }

            QPushButton {
                border-radius: 5px;
                padding-left: 10px;
                padding-right: 10px;
                padding-top:4px;
                padding-bottom:4px;
                font-size: 8pt;
                font-family: Verdana;
                border: 1px solid rgb(45,52,71);
                color:white;
                background-color: rgb(94,109,148);
            }

            QPushButton:hover {
                background-color: rgb(112, 126, 164);
            }

            QPushButton:hover:pressed {
                background-color: rgb(129, 141, 175);
            }
            """)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Change Position"))
        self.firstNameLabel.setText(_translate("Dialog", "First Name:"))
        self.firstNameValueLabel.setText(_translate("Dialog", "Liviu"))
        self.lastNameLabel.setText(_translate("Dialog", "Last Name:"))
        self.lastNameValueLabel.setText(_translate("Dialog", "Bosbiciu"))
        self.currentPositionLabel.setText(_translate("Dialog", "Current position:"))
        self.currentPositionValueLabel.setText(_translate("Dialog", "TextLabel"))
        self.newPositionLabel.setText(_translate("Dialog", "New position:"))
        self.saveButton.setText(_translate("Dialog", "Save"))


class PositionDialog(QtWidgets.QDialog):

    def __init__(self, first_name, last_name, current_position):
        super(PositionDialog, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.firstNameValueLabel.setText(first_name)
        self.ui.lastNameValueLabel.setText(last_name)
        self.ui.currentPositionValueLabel.setText(current_position)

        self.ui.saveButton.clicked.connect(self.save_button_clicked)

    def save_button_clicked(self):
        self.new_position = self.ui.newPositionLineEdit.text()

        self.accept()