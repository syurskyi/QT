from PyQt5.QtWidgets import QHBoxLayout, QLabel, QFrame, QVBoxLayout, QLCDNumber, QPushButton
from PyQt5 import QtGui
from Source import globals


class SettingsInterface:
    def __init__(self, variable, signals):
        self.signals = signals
        self.create_interface(variable)

    def create_interface(self, variable):
        self.__setting_box = QHBoxLayout()

        self.__setting_box.addWidget(QLabel("Settings:"))
        self.__setting_box.addWidget(QLabel('N='))
        self.__setting_box.addWidget(variable['n'])
        self.__setting_box.addWidget(QLabel('M='))
        self.__setting_box.addWidget(variable['m'])
        self.__setting_box.addWidget(QLabel('Mines='))
        self.__setting_box.addWidget(variable['mines'])
        self.__setting_box.addWidget(variable['ok_button'])
        self.__setting_box.addWidget(variable['pause_button'])

        self.__statistics_box = QHBoxLayout()

        self.time_display = QLCDNumber()
        self.time_display.setFrameShape(QFrame.NoFrame)
        self.time_display.setMaximumSize(80, 40)
        self.time_display.setMinimumSize(80, 40)
        self.bombs_display = QLCDNumber()
        self.bombs_display.setMaximumSize(80, 40)
        self.bombs_display.setMinimumSize(80, 40)
        self.bombs_display.setFrameShape(QFrame.NoFrame)
        self.signals.update_time_display.connect(self.update_time)
        self.signals.update_bombs_display.connect(self.update_bombs)

        clock = QPushButton()
        clock.setStyleSheet('border: none;')
        clock.setIcon(QtGui.QIcon('../Images/clock.png'))
        clock.setMaximumSize(40, 40)
        clock.clicked.connect(self.paint_clock)
        self.clock_click = False

        bomb = QPushButton()
        bomb.setStyleSheet('border: none;')
        bomb.setIcon(QtGui.QIcon('../Images/bomb.png'))
        bomb.setMaximumSize(40, 40)
        bomb.clicked.connect(self.paint_bomb)
        self.bomb_click = False

        self.__statistics_box.addWidget(clock)
        self.__statistics_box.addWidget(self.time_display)
        self.__statistics_box.addWidget(bomb)
        self.__statistics_box.addWidget(self.bombs_display)

    def paint_clock(self):
        if not self.clock_click:
            self.clock_click = True
            self.time_display.setStyleSheet('font-size: 12px;'
                               'font-family: Arial;color: rgb(255, 255, 255);'
                               'background-color: rgb(38,56,76);')
        else:
            self.clock_click = False
            self.time_display.setStyleSheet(None)

    def paint_bomb(self):
        if not self.bomb_click:
            self.bomb_click = True
            self.bombs_display.setStyleSheet('font-size: 12px;'
                                            'font-family: Arial;color: rgb(255, 255, 255);'
                                            'background-color: rgb(38,56,76);')
        else:
            self.bomb_click = False
            self.bombs_display.setStyleSheet(None)

    def update_time(self):
        self.time_display.display(globals.time)

    def update_bombs(self):
        self.bombs_display.display(globals.flag_bombs)

    def layout(self):
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        self.__layout = QVBoxLayout()
        self.__layout.addLayout(self.__setting_box)
        self.__layout.addLayout(self.__statistics_box)
        self.__layout.addStretch(1)
        self.__layout.setSpacing(10)
        frame.setLayout(self.__layout)
        frame.setMaximumSize(560, 126)

        layout = QVBoxLayout()
        layout.addWidget(frame)

        return layout



