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


class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):

        # ##################widgets of top layout###########
        self.add_product_image = QLabel()
        self.image = QPixmap('icons/addproduct.png')
        self.add_product_image.setPixmap(self.image)
        self.title_text = QLabel("Add Product")
        # ################widgets of bottom layot###########
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter name of product")
        self.manufacturer_entry = QLineEdit()
        self.manufacturer_entry.setPlaceholderText("Enter name of manufacturer")
        self.price_entry = QLineEdit()
        self.price_entry.setPlaceholderText("Enter price of product")
        self.qouta_entry = QLineEdit()
        self.qouta_entry.setPlaceholderText("Enter qouta of product")
        self.upload_button = QPushButton("Upload")
        self.upload_button.clicked.connect(self.upload_image)
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.add_product)

    def layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QFormLayout()
        self.top_frame = QFrame()
        self.bottom_frame = QFrame()
        # #################add widgets###################
        # ##########widgets of toplayout##############
        self.top_layout.addWidget(self.add_product_image)
        self.top_layout.addWidget(self.title_text)
        self.top_frame.setLayout(self.top_layout)
        # # ##############Widgets of form layout##########
        self.bottom_layout.addRow(QLabel("Name: "), self.name_entry)
        self.bottom_layout.addRow(QLabel("Manufacturer: "), self.manufacturer_entry)
        self.bottom_layout.addRow(QLabel("Price: "), self.price_entry)
        self.bottom_layout.addRow(QLabel("Qouta: "), self.qouta_entry)
        self.bottom_layout.addRow(QLabel("Upload: "), self.upload_button)
        self.bottom_layout.addRow(QLabel(""), self.submit_button)
        self.bottom_frame.setLayout(self.bottom_layout)
        #
        self.main_layout.addWidget(self.top_frame)
        self.main_layout.addWidget(self.bottom_frame)
        self.setLayout(self.main_layout)

    def upload_image(self):
        global default_image
        size = (256, 256)
        self.filename, ok = QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')
        if ok:
            print(self.filename)
            default_image = os.path.basename(self.filename)
            print(default_image)
            image = Image.open(self.filename)
            image = image.resize(size)
            image.save("img/{0}".format(default_image))

    def add_product(self):
        global default_image
        name = self.name_entry.text()
        manufacturer = self.manufacturer_entry.text()
        price = self.price_entry.text()
        qouta = self.qouta_entry.text()

        if (name and manufacturer and price and qouta != ''):
            try:
                query = "INSERT INTO 'products' (product_name, product_manufacturer, product_price, product_qouta, " \
                        "product_img) VALUES(?, ?, ?, ?, ?)"
                cursor.execute(query, (name, manufacturer, price, qouta, default_image))
                connect.commit()
                QMessageBox.information(self, "Info", "Product has been added")

            except:
                QMessageBox.information(self, "Info", "Product has not been added")

        else:
            QMessageBox.information(self, "Info", "Fields cant be empty!!!")
