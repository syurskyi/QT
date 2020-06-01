import sys
import os
import json

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog, QMessageBox

from cart_d import Ui_Dialog
from auth import Auth
from codereader import CodeReader
from lister import Lister
from voice_handler import VoiceHandler
from predict_emotion import recognition_emotion_from_voice


class Cart(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.warning()
        self.start()
        self.exit_from_account.clicked.connect(self.exit_from_acc)
        self.add_to_cart.clicked.connect(self.append_product)
        self.product_cost.clicked.connect(self.cost_of_product)
        self.add_to_cart_2.clicked.connect(self.delete_product)
        self.create_list.clicked.connect(self.create_list_user)
        self.audio_request.clicked.connect(self.use_microphone)
        self.list_of_items = []
        self.deleted_items = []
        self.call_a_shopman.clicked.connect(self.help)

    def warning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.resize(300, 300)
        msg.move(self.x(), self.y())
        msg.setWindowTitle("Warning")
        msg.setText("В публичной версии некоторые функции работают некорректно."
                    " Требуются приватные ключи авторизации в API")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def start(self):
        self.main_menu = Auth()
        self.main_menu.exec_()

    def append_product(self):
        reader = CodeReader()
        reader.exec_()
        if reader.info_product:
            self.user_cart.addItem(reader.info_product["name"])
            if reader.info_product["name"] in self.list_of_items:
                self.user_list.takeItem(self.list_of_items.index(reader.info_product["name"]))
                self.deleted_items.append(self.list_of_items[self.list_of_items.index(
                    reader.info_product["name"])])
                del self.list_of_items[self.list_of_items.index(reader.info_product["name"])]

    def delete_product(self):
        for el in self.user_cart.selectedItems():
            self.user_cart.takeItem(self.user_cart.row(el))

    def use_microphone(self):
        VoiceHandler().exec_()

    def exit_from_acc(self):
        self.main_menu.status = False
        self.main_menu.auth2.auth_state = False
        self.start()

    def cost_of_product(self):
        reader = CodeReader()
        reader.exec_()
        if reader.info_product:
            self.cost_msg_box(reader.info_product['cost'])

    def cost_msg_box(self, cost):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(300, 300)
        msg.move(self.x(), self.y())
        msg.setText("Цена:")
        msg.setWindowTitle("Цена этого продукта")
        msg.setText("{}₽".format(cost))
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.exec_()

    def help(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.resize(300, 300)
        msg.move(self.x(), self.y())
        msg.setText("Ошибка")
        msg.setWindowTitle("Ошибка")
        msg.setText("В публичной версии эта функция не работает."
                    " Требуются приватные ключи авторизации в API")
        msg.setStandardButtons(QMessageBox.Cancel)
        msg.exec_()

    def create_list_user(self):
        lister = Lister(self.list_of_items.copy())
        lister.exec_()
        self.list_of_items = lister.user_list_list.copy()
        self.user_list.clear()
        for el in self.list_of_items:
            self.user_list.addItem(el)
        cost = 0
        cost_data = json.loads(open("data/products2.json").read())
        for el in self.list_of_items:
            cost += cost_data[el]
        for el in self.deleted_items:
            cost += cost_data[el]
        if cost <= 9999:
            self.label_2.setText("Итого: {}₽".format(cost))
        else:
            self.label_2.setText("Итого: 9999₽+".format(cost))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cart = Cart()
    cart.show()
    sys.exit(app.exec_())
