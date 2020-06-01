# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'earlyaccess_display.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        # Load the custom font
        self.font_db = QFontDatabase()
        self.font_id = self.font_db.addApplicationFont("Glasstown.ttf")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.round_counter = QtWidgets.QLabel(self.centralwidget)
        self.round_counter.setGeometry(QtCore.QRect(20, 0, 711, 41))

        font = QtGui.QFont('Glasstown NBP')
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)

        self.round_counter.setFont(font)
        self.round_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.round_counter.setObjectName("round_counter")

        self.graphic_frame = QtWidgets.QFrame(self.centralwidget)
        self.graphic_frame.setGeometry(QtCore.QRect(20, 40, 711, 391))
        self.graphic_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graphic_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graphic_frame.setObjectName("graphic_frame")

        self.player1_label = QtWidgets.QLabel(self.centralwidget)
        self.player1_label.setGeometry(QtCore.QRect(20, 440, 111, 21))

        font.setPointSize(16)

        self.player1_label.setFont(font)
        self.player1_label.setObjectName("player1_label")
        self.player2_label = QtWidgets.QLabel(self.centralwidget)
        self.player2_label.setGeometry(QtCore.QRect(590, 440, 111, 21))

        self.player2_label.setFont(font)
        self.player2_label.setObjectName("player2_label")

        self.player1_hp = QtWidgets.QProgressBar(self.centralwidget)
        self.player1_hp.setGeometry(QtCore.QRect(20, 470, 351, 23))
        self.player1_hp.setProperty("value", 24)
        self.player1_hp.setObjectName("player1_hp")

        self.player2_hp = QtWidgets.QProgressBar(self.centralwidget)
        self.player2_hp.setGeometry(QtCore.QRect(390, 470, 351, 23))
        self.player2_hp.setProperty("value", 24)
        self.player2_hp.setObjectName("player2_hp")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 540, 681, 151))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(339)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(49)
        self.tableWidget.verticalHeader().setHighlightSections(False)

        self.player1_stamina = QtWidgets.QLabel(self.centralwidget)
        self.player1_stamina.setGeometry(QtCore.QRect(20, 495, 161, 41))

        font.setPointSize(15)

        self.player1_stamina.setFont(font)
        self.player1_stamina.setObjectName("player1_stamina")

        self.player2_stamina = QtWidgets.QLabel(self.centralwidget)
        self.player2_stamina.setGeometry(QtCore.QRect(390, 500, 161, 31))


        self.player2_stamina.setFont(font)
        self.player2_stamina.setObjectName("player2_stamina")

        self.light_attack_button = QtWidgets.QPushButton(self.centralwidget)
        self.light_attack_button.setGeometry(QtCore.QRect(20, 540, 341, 51))
        self.light_attack_button.setObjectName("light_attack_button")

        self.heavy_attack_button = QtWidgets.QPushButton(self.centralwidget)
        self.heavy_attack_button.setGeometry(QtCore.QRect(360, 540, 341, 51))
        self.heavy_attack_button.setObjectName("heavy_attack_button")

        self.block_button = QtWidgets.QPushButton(self.centralwidget)
        self.block_button.setGeometry(QtCore.QRect(20, 590, 341, 51))
        self.block_button.setObjectName("block_button")

        self.dodge_button = QtWidgets.QPushButton(self.centralwidget)
        self.dodge_button.setGeometry(QtCore.QRect(360, 590, 341, 51))
        self.dodge_button.setObjectName("dodge_button")

        self.taunt_button = QtWidgets.QPushButton(self.centralwidget)
        self.taunt_button.setGeometry(QtCore.QRect(20, 640, 341, 51))
        self.taunt_button.setObjectName("taunt_button")

        self.sleep_button = QtWidgets.QPushButton(self.centralwidget)
        self.sleep_button.setGeometry(QtCore.QRect(360, 640, 341, 51))
        self.sleep_button.setObjectName("sleep_button")

        self.player_indicator = QtWidgets.QLabel(self.centralwidget)
        self.player_indicator.setGeometry(QtCore.QRect(30, 10, 161, 31))

        font.setPointSize(14)

        self.player_indicator.setFont(font)
        self.player_indicator.setObjectName("player_indicator")
        self.player_indicator.setStyleSheet("color: red;")

        self.game_actions_informer = QtWidgets.QLabel(self.centralwidget)
        self.game_actions_informer.setGeometry(QtCore.QRect(24, 705, 671, 71))
        self.game_actions_informer.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.game_actions_informer.setObjectName("game_actions_informer")

        self.sprite_background = QPixmap('images/background.png')
        self.background_image = QtWidgets.QLabel(self.graphic_frame)
        self.background_image.setGeometry(QtCore.QRect(4, 5, 701, 381))
        self.background_image.setObjectName("background_image")

        self.sprite1 = QPixmap('images/cloud.png')
        self.player1_sprite = QtWidgets.QLabel(self.graphic_frame)
        self.player1_sprite.setGeometry(QtCore.QRect(70, 160, 191, 221))
        self.player1_sprite.setObjectName("player1_sprite")

        self.sprite2 = QPixmap('images/sephiroth.png')
        self.player2_sprite = QtWidgets.QLabel(self.graphic_frame)
        self.player2_sprite.setGeometry(QtCore.QRect(430, 160, 191, 221))
        self.player2_sprite.setObjectName("player2_sprite")

        self.player1_action_icon = QtWidgets.QLabel(self.graphic_frame)
        self.player1_action_icon.setGeometry(QtCore.QRect(180, 180, 64, 64))
        self.player1_action_icon.setObjectName("player1_action_icon")

        self.player2_action_icon = QtWidgets.QLabel(self.graphic_frame)
        self.player2_action_icon.setGeometry(QtCore.QRect(400, 180, 64, 64))
        self.player2_action_icon.setObjectName("player2_action_icon")

        self.restart_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(620, 10, 93, 28))
        self.restart_button.setObjectName("restart_button")

        self.attack1_icons = [QPixmap('images/light1.png'), QPixmap('images/heavy1.png')]
        self.attack2_icons = [QPixmap('images/light2.png'), QPixmap('images/heavy2.png')]
        self.action_icons = [QPixmap('images/block.png'), QPixmap('images/dodge.png'),
                             QPixmap('images/taunt.png'), QPixmap('images/sleep.png')]

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.round_counter.setText(_translate("MainWindow", "TextLabel"))
        self.player1_label.setText(_translate("MainWindow", "Player 1"))
        self.player2_label.setText(_translate("MainWindow", "Player 2"))
        self.player1_stamina.setText(_translate("MainWindow", "TextLabel"))
        self.player2_stamina.setText(_translate("MainWindow", "TextLabel"))
        self.light_attack_button.setText(_translate("MainWindow", "Light Attack"))
        self.heavy_attack_button.setText(_translate("MainWindow", "Heavy Attack"))
        self.block_button.setText(_translate("MainWindow", "Block"))
        self.dodge_button.setText(_translate("MainWindow", "Dodge"))
        self.taunt_button.setText(_translate("MainWindow", "Taunt"))
        self.sleep_button.setText(_translate("MainWindow", "Sleep"))
        self.player_indicator.setText(_translate("MainWindow", "TextLabel"))
        self.game_actions_informer.setText(_translate("MainWindow", ""))
        self.background_image.setText(_translate("MainWindow", ""))
        self.player1_sprite.setText(_translate("MainWindow", ""))
        self.player2_sprite.setText(_translate("MainWindow", ""))
        self.player1_action_icon.setText(_translate("MainWindow", ""))
        self.player2_action_icon.setText(_translate("MainWindow", ""))
        self.restart_button.setText(_translate("MainWindow", "Restart"))

