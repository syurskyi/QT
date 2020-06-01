# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changemapsize.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChangeMapSize(object):
    def setupUi(self, ChangeMapSize):
        ChangeMapSize.setObjectName("ChangeMapSize")
        ChangeMapSize.resize(345, 144)
        ChangeMapSize.setMaximumSize(345,144)
        ChangeMapSize.setMinimumSize(345,144)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(ChangeMapSize)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 288, 106))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_16x9 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_16x9.setObjectName("radioButton_9x16")
        self.horizontalLayout.addWidget(self.radioButton_16x9)
        self.radioButton_12x12 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_12x12.setObjectName("radioButton_12x12")
        self.horizontalLayout.addWidget(self.radioButton_12x12)
        self.radioButton_15x15 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_15x15.setObjectName("radioButton_15x15")
        self.horizontalLayout.addWidget(self.radioButton_15x15)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.radioButton_custom = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.radioButton_custom.setObjectName("radioButton_custom")
        self.verticalLayout.addWidget(self.radioButton_custom)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.horizontalLayoutWidget_3)
        self.buttonBox.setMinimumSize(QtCore.QSize(80, 54))
        self.buttonBox.setMaximumSize(QtCore.QSize(80, 54))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(ChangeMapSize)
        # self.buttonBox.accepted.connect(ChangeMapSize.accept)
        # self.buttonBox.rejected.connect(ChangeMapSize.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangeMapSize)

    def retranslateUi(self, ChangeMapSize):
        _translate = QtCore.QCoreApplication.translate
        ChangeMapSize.setWindowTitle(_translate("ChangeMapSize", "更改棋盘大小"))
        self.label.setText(_translate("ChangeMapSize", "选择你的棋盘大小"))
        self.radioButton_16x9.setText(_translate("ChangeMapSize", "9x16"))
        self.radioButton_12x12.setText(_translate("ChangeMapSize", "12x12"))
        self.radioButton_15x15.setText(_translate("ChangeMapSize", "15x15"))
        self.radioButton_custom.setText(_translate("ChangeMapSize", "自定义大小"))
        self.label_2.setText(_translate("ChangeMapSize", "宽度:"))
        self.label_3.setText(_translate("ChangeMapSize", "长度:"))

