import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import add_product
import add_member

connect = sqlite3.connect('products.db')
print("Opened database successfully")

# connect.execute('''CREATE TABLE products
#          (product_id INTEGER PRIMARY KEY     AUTOINCREMENT,
#          product_name           TEXT,
#          product_manufacturer   TEXT,
#          product_price        INTEGER ,
#          product_qouta        INTEGER ,
#          product_img          TEXT ,
#          product_availability   TEXT  DEFAULT 'Available');''')
#
# connect.execute('''CREATE TABLE members
#          (member_id INTEGER PRIMARY KEY     AUTOINCREMENT,
#          member_name           TEXT,
#          member_surname        TEXT,
#          member_phone          TEXT );''')
#
# connect.execute('''CREATE TABLE sellings
#          (selling_id INTEGER PRIMARY KEY     AUTOINCREMENT,
#          selling_product_id           INTEGER,
#          selling_member_id   INTEGER,
#          selling_quantity       INTEGER ,
#          selling_amount        INTEGER );''')


cursor = connect.cursor


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Product Manager')
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.ui()
        self.show()

    def ui(self):
        self.toolbar()
        self.tab_widget()
        self.widgets()
        self.layouts()
        self.display_products()

    def toolbar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # ####################Toolbar Buttons############
        # ###################Add Product#################
        self.add_product = QAction(QIcon('icons/add.png'), 'Add Product', self)
        self.tb.addAction(self.add_product)
        self.add_product.triggered.connect(self.func_add_product)
        self.tb.addSeparator()

        # #####################Add Member################
        self.add_member = QAction(QIcon('icons/users.png'), "Add Member", self)
        self.tb.addAction(self.add_member)
        self.add_member.triggered.connect(self.func_add_member)
        self.tb.addSeparator()

        # #####################Sell Products###############
        self.sell_product = QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sell_product)
        # self.sellProduct.triggered.connect(self.funcSellProducts)
        self.tb.addSeparator()

    def tab_widget(self):
        self.tabs = QTabWidget()
        # self.tabs.blockSignals(True)
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

    def widgets(self):
        # ######################Tab1 Widgets###############
        # ####################Main left layout widget######
        self.products_table = QTableWidget()
        self.products_table.setColumnCount(6)
        self.products_table.setColumnHidden(0, True)
        self.products_table.setHorizontalHeaderItem(0, QTableWidgetItem("Product Id"))
        self.products_table.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.products_table.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.products_table.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.products_table.setHorizontalHeaderItem(4, QTableWidgetItem("Qouta"))
        self.products_table.setHorizontalHeaderItem(5, QTableWidgetItem("Availbility"))
        self.products_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.products_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        # #######################Right top layout widgets#######################
        self.search_text = QLabel('Search')
        self.search_entry = QLineEdit()
        self.search_button = QPushButton('Search')

        # #########################Right middle layout widgets###########
        self.all_products = QRadioButton('All Products')
        self.available_products = QRadioButton('Available')
        self.not_available_products = QRadioButton('Not Available')
        self.list_button = QPushButton('List')

        # #######################Tab2 Widgets#########################
        self.members_table = QTableWidget()
        self.members_table.setColumnCount(4)
        self.members_table.setHorizontalHeaderItem(0, QTableWidgetItem("Member ID"))
        self.members_table.setHorizontalHeaderItem(1, QTableWidgetItem("Member Name"))
        self.members_table.setHorizontalHeaderItem(2, QTableWidgetItem("Member Surname"))
        self.members_table.setHorizontalHeaderItem(3, QTableWidgetItem("Phone"))
        self.members_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)

        self.member_search_text = QLabel("Search Members")
        self.member_search_entry = QLineEdit()
        self.member_search_button = QPushButton("Search")
        # self.member_search_button.clicked.connect(self.searchMembers)

        # #########################Tab3 widgets#####################

    def layouts(self):
        # #####################Tab1 layouts##############
        self.main_layout = QHBoxLayout()
        self.main_left_layout = QVBoxLayout()
        self.main_right_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.top_groupbox = QGroupBox('Search Box')
        self.middle_groupbox = QGroupBox('List Box')
        # ################Add widgets######################
        # ###############Left main layout widget###########
        self.main_left_layout.addWidget(self.products_table)
        # #######################Right top layout widgets#########
        self.right_top_layout.addWidget(self.search_text)
        self.right_top_layout.addWidget(self.search_entry)
        self.right_top_layout.addWidget(self.search_button)
        self.top_groupbox.setLayout(self.right_top_layout)
        # ################Right middle layout widgets##########
        self.right_middle_layout.addWidget(self.all_products)
        self.right_middle_layout.addWidget(self.available_products)
        self.right_middle_layout.addWidget(self.not_available_products)
        self.right_middle_layout.addWidget(self.list_button)
        self.middle_groupbox.setLayout(self.right_middle_layout)

        self.main_right_layout.addWidget(self.top_groupbox)

        self.main_layout.addLayout(self.main_left_layout, 70)
        self.main_right_layout.addWidget(self.middle_groupbox, 20)
        self.main_layout.addLayout(self.main_right_layout, 30)
        self.tab1.setLayout(self.main_layout)

        # #####################Tab2 Layouts#####################
        self.member_main_layout = QHBoxLayout()
        self.member_left_layout = QHBoxLayout()
        self.member_right_layout = QHBoxLayout()
        self.member_right_groupbox = QGroupBox("Search For Members")
        self.member_right_groupbox.setContentsMargins(10, 10, 10, 500)
        self.member_right_layout.addWidget(self.member_search_text)
        self.member_right_layout.addWidget(self.member_search_entry)
        self.member_right_layout.addWidget(self.member_search_button)
        self.member_right_groupbox.setLayout(self.member_right_layout)

        self.member_left_layout.addWidget(self.members_table)
        self.member_main_layout.addLayout(self.member_left_layout, 70)
        self.member_main_layout.addWidget(self.member_right_groupbox, 30)
        self.tab2.setLayout(self.member_main_layout)

        # ####################Tab3 layouts########################

    def func_add_product(self):
        self.new_product = add_product.AddProduct()

    def func_add_member(self):
        self.new_member = add_member.AddMember()

    def display_products(self):
        self.products_table.setFont(QFont("Times", 12))
        for i in reversed(range(self.products_table.rowCount())):
            self.products_table.removeRow(i)

        # query = cursor.execute("SELECT product_id FROM products")
    #     for row_data in query:
    #         row_number = self.products_table.rowCount()
    #         self.products_table.insertRow(row_number)
    #         for column_number, data in enumerate(row_data):
    #             self.products_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    #
    #     self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
