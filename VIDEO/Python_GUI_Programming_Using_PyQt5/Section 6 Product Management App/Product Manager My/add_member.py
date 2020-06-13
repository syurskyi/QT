import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image

connect = sqlite3.connect('products.db')
cursor = connect.cursor

default_image = 'store.png'


class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.ui()
        self.show()

    def ui(self):
        # pass
        self.widgets()
        self.layouts()

    def widgets(self):
        # ############widgets of top layout###########
        self.add_member_image = QLabel()
        self.image = QPixmap('icons/addmember.png')
        self.add_member_image.setPixmap(self.image)
        self.add_member_image.setAlignment(Qt.AlignCenter)
        self.title_text = QLabel("Add Member")
        self.title_text.setAlignment(Qt.AlignCenter)

        # # ###########widgets of bottom layout############
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter name of member")
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText("Enter surname of member")
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText("Enter phone number")
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.add_member)

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()
        # ############add widgets############
        self.top_layout.addWidget(self.title_text)
        self.top_layout.addWidget(self.add_member_image)
        self.top_frame.setLayout(self.top_layout)
        self.bottom_layout.addRow(QLabel("Name: "), self.name_entry)
        self.bottom_layout.addRow(QLabel("SurName: "), self.surname_entry)
        self.bottom_layout.addRow(QLabel("Phone: "), self.phone_entry)
        self.bottom_layout.addRow(QLabel(""), self.submit_btn)
        self.bottom_frame.setLayout(self.bottom_layout)

        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)

        self.setLayout(self.main_layout)

    def add_member(self):
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()

        if (name and surname and phone !=""):

            try:
                query = "INSERT INTO 'members' (member_name,member_surname,member_phone) VALUES(?,?,?)"
                cursor.execute(query,(name, surname, phone))
                connect.commit()
                QMessageBox.information(self, "Info", "Member has been added!")
                self.name_entry.setText("")
                self.surname_entry.setText("")
                self.phone_entry.setText("")
            except:
                QMessageBox.information(self, "Info", "Member has not been added!")

        else:
            QMessageBox.information(self, "Info", "Fields can not be empty!")

