import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, \
    QVBoxLayout

from AsteroidsGame import AsteroidsGame
from core.utils.image_helper import get_full_image_path

from entities.PlayerInput import PlayerInput


class ScoreWindow(QMainWindow):
    def __init__(self, scoreFilePath="../test.txt"):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Scores")
        self.initUI(scoreFilePath)

    def initUI(self, scoreFilePath):
        self.initWindow()
        self.read_from_file(scoreFilePath)

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def read_from_file(self, scoreFilePath):
        stara = []
        lista = []

        brojac = 0
        f = open(scoreFilePath, "r")
        for line in f:
            lista.append([i for i in line.strip("\n").split(":")])
            brojac = brojac + 1


        lista.sort(key=lambda x: int(x[1]))


        lista.reverse()
        if brojac == 0:
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
        elif brojac == 1:
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
        elif brojac == 2:
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
        elif brojac == 3:
            lista.append(" ")
            lista.append(" ")
        elif brojac == 4:
            lista.append(" ")


        print(brojac)

        self.vbox = QVBoxLayout()
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(0, 0, 250, 200)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Name "))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(" points"))
        if lista[0][0] != " " and lista[0][1] != " ":
            self.tableWidget.setItem(1, 0, QTableWidgetItem(lista[0][0]))
            self.tableWidget.setItem(1, 1, QTableWidgetItem(lista[0][1]))
        if lista[1][0] != " " and lista[1][1] != " ":
            self.tableWidget.setItem(2, 0, QTableWidgetItem(lista[1][0]))
            self.tableWidget.setItem(2, 1, QTableWidgetItem(lista[1][1]))
        if lista[2][0] != " " and lista[2][1] != " ":
            self.tableWidget.setItem(3, 0, QTableWidgetItem(lista[2][0]))
            self.tableWidget.setItem(3, 1, QTableWidgetItem(lista[2][1]))
        if lista[3][0] != " " and lista[3][1] != " ":
            self.tableWidget.setItem(4, 0, QTableWidgetItem(lista[3][0]))
            self.tableWidget.setItem(4, 1, QTableWidgetItem(lista[3][1]))
        elif lista[4][0] != " " and lista[4][1] != " ":
            self.tableWidget.setItem(5, 0, QTableWidgetItem(lista[4][0]))
            self.tableWidget.setItem(5, 1, QTableWidgetItem(lista[4][1]))

        self.vbox.addWidget(self.tableWidget)
        self.setLayout(self.vbox)
        self.tableWidget.show()

        # print(jjj)
        print(lista)


def wi():
    app = QApplication(sys.argv)
    win = ScoreWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
