import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from auth_d import Ui_Dialog
from auth2 import Auth2
from PyQt5.QtWidgets import QDialog


class Auth(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.help)
        self.status = False

    def run(self):
        self.auth2 = Auth2()
        self.auth2.exec_()
        if self.auth2.auth_state:
            self.status = True
            self.close()

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

    def closeEvent(self, event):
        if self.status:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    auth = Auth()
    auth.show()
    sys.exit(app.exec_())
