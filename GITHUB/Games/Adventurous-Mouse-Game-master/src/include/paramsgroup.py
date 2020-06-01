# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QComboBox, QGroupBox, QLabel, QPushButton, QSpinBox

from include.gamegroup import GameGroup
from include.importcolors import importColors


class ParamsGroup(QGroupBox):
    def __init__(self, mainWindow, container):
        super().__init__(container, objectName='paramsGroup')

        self.mainWindow = mainWindow
        self.setGeometry(QRect(10, 0, 341, 191))
        self.setTitle('Parameters')

        self.colorList = importColors(self.mainWindow.path + 'include/colors.xml')

        self.beginLabel = QLabel(self, objectName='beginLabel')
        self.beginLabel.setGeometry(QRect(10, 20, 91, 21))
        self.beginLabel.setText('• Color 1 (Begin) :')

        self.endLabel = QLabel(self, objectName='endLabel')
        self.endLabel.setGeometry(QRect(10, 50, 91, 21))
        self.endLabel.setText('• Color 2 (End) :')

        self.velocityLabel = QLabel(self, objectName='velocityLabel')
        self.velocityLabel.setGeometry(QRect(10, 80, 61, 21))
        self.velocityLabel.setText('• Velocity :')

        self.levelLabel = QLabel(self, objectName='levelLabel')
        self.levelLabel.setGeometry(QRect(10, 110, 61, 21))
        self.levelLabel.setText('• Level :')

        self.beginComboBox = QComboBox(self, objectName='beginComboBox')
        self.beginComboBox.setGeometry(QRect(100, 20, 81, 22))

        self.endComboBox = QComboBox(self, objectName='endComboBox')
        self.endComboBox.setGeometry(QRect(100, 50, 81, 22))

        for color in self.colorList:
            self.beginComboBox.addItem(color['name'])
            self.endComboBox.addItem(color['name'])

        self.endComboBox.setCurrentIndex(1)

        self.velocitySpinBox = QSpinBox(self, objectName='velocitySpinBox')
        self.velocitySpinBox.setGeometry(QRect(70, 80, 91, 22))
        self.velocitySpinBox.setMaximum(5)
        self.velocitySpinBox.setValue(1)
        self.velocitySpinBox.setSuffix('  pixel/move')

        self.levelComboBox = QComboBox(self, objectName='levelComboBox')
        self.levelComboBox.setGeometry(QRect(70, 110, 81, 22))
        self.levelComboBox.addItem('Easy')
        self.levelComboBox.addItem('Medium')
        self.levelComboBox.addItem('Hard')

        self.levelSpinBox = QSpinBox(self, objectName='levelSpinBox')
        self.levelSpinBox.setGeometry(QRect(160, 110, 61, 22))
        self.levelSpinBox.setMinimum(1)
        self.levelSpinBox.setMaximum(3)

        self.actionButton = QPushButton(self, objectName='actionButton')
        self.actionButton.setGeometry(QRect(100, 150, 141, 31))
        self.actionButton.setText('Start game')

        self.velocitySpinBox.valueChanged.connect(self.changed_velocitySpinBox)
        self.actionButton.clicked.connect(self.clicked_actionButton)


    def changed_velocitySpinBox(self):
        self.mainWindow.speed = self.velocitySpinBox.value()


    def clicked_actionButton(self):
        if self.mainWindow.gameGroup:
            self.mainWindow.gameGroup.hide()
            del(self.mainWindow.gameGroup)

        self.mainWindow.gameGroup = GameGroup(self.mainWindow, self.levelComboBox.currentIndex(), self.levelSpinBox.value())
        self.actionButton.setText('Restart game')


    def getBeginColor(self):
        selectedColor = self.colorList[self.beginComboBox.currentIndex()]
        return [tuple(selectedColor['min']), tuple(selectedColor['max'])]


    def getEndColor(self):
        selectedColor = self.colorList[self.endComboBox.currentIndex()]
        return [tuple(selectedColor['min']), tuple(selectedColor['max'])]
