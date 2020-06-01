from PyQt5.QtWidgets import QMessageBox


class RangeException(Exception):
    def __init__(self, message):
        self.__message = message

    def get_message(self):
        return self.__message

    def get_statement(self):
        __statement = QMessageBox.question(QMessageBox(), "Message", self.__message, QMessageBox.Ok)
