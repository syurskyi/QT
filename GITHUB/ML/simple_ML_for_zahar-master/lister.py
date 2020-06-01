import sys
from PyQt5.QtWidgets import QApplication
from list_d import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
import json


class Lister(QDialog, Ui_Dialog):

    def __init__(self, list_of_user_first):
        super().__init__()
        self.setupUi(self)
        self.rules = {"pushButton": "9785090459099", "pushButton_2": "9785346038276",
                      "pushButton_3": "4680211153564"}
        self.label.setPixmap(QPixmap("data/pictures/dm_9.jpg"))
        self.label.setScaledContents(True)
        self.label_2.setPixmap(QPixmap("data/pictures/wb_phys.jpg"))
        self.label_2.setScaledContents(True)
        self.label_3.setPixmap(QPixmap("data/pictures/wb.jpeg"))
        self.label_3.setScaledContents(True)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_5.clicked.connect(self.off)
        self.pushButton_4.clicked.connect(self.delete_item)
        self.user_list_list = list_of_user_first.copy()
        for i in list_of_user_first:
            self.listWidget.addItem(i)

    def run(self):
        data = json.loads(open("data/products.json").read())
        if self.sender().objectName() in self.rules:
            if self.rules[self.sender().objectName()] in data:
                self.listWidget.addItem(data[self.rules[self.sender().objectName()]]["name"])

    def off(self):
        self.user_list_list.clear()
        self.user_list_list.extend([self.listWidget.item(i).text() for i in range(self.listWidget.count())])
        self.close()

    def delete_item(self):
        for el in self.listWidget.selectedItems():
            self.listWidget.takeItem(self.listWidget.row(el))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lister = Lister()
    lister.show()
    sys.exit(app.exec_())
