import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
import add_product
import add_member
import sellings
import style
from PIL import Image

con = sqlite3.connect("products.db")

# con.execute('''CREATE TABLE products
#          (product_id INTEGER PRIMARY KEY     AUTOINCREMENT,
#          product_name           TEXT,
#          product_manufacturer   TEXT,
#          product_price        INTEGER ,
#          product_qouta        INTEGER ,
#          product_img          TEXT ,
#          product_availability   TEXT  DEFAULT 'Available');''')
#
# con.execute('''CREATE TABLE members
#          (member_id INTEGER PRIMARY KEY     AUTOINCREMENT,
#          member_name           TEXT,
#          member_surname        TEXT,
#          member_phone          TEXT );''')
#
# con.execute('''CREATE TABLE sellings
#          (selling_id INTEGER PRIMARY KEY     AUTOINCREMENT,
#          selling_product_id           INTEGER,
#          selling_member_id   INTEGER,
#          selling_quantity       INTEGER ,
#          selling_amount        INTEGER );''')


cur = con.cursor()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 1350, 750)
        self.setFixedSize(self.size())

        self.UI()
        self.show()

    def ui(self):
        self.toolbar()
        self.tab_wigdet()
        self.widgets()
        self.layouts()
        self.display_products()
        self.display_members()
        self.get_statistics()

    def toolbar(self):
        self.tb = self.add_tool_bar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # ####################Toolbar Buttons############
        # ###################Add Product################
        self.add_product = QAction(QIcon('icons/add.png'), "Add Product", self)
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
        self.sell_product.triggered.connect(self.func_sell_products)
        self.tb.addSeparator()

    def tab_wigdet(self):
        self.tabs = QTabWidget()
        self.tabs.blockSignals(True)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.setCentralWidget(self.tabs)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1, "Products")
        self.tabs.addTab(self.tab2, "Members")
        self.tabs.addTab(self.tab3, "Statistics")

    def widgets(self):
        # ######################Tab1 Widgets###############
        # ###################Main left layout widget##########
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
        self.products_table.doubleClicked.connect(self.selected_product)

        # #######################Right top layout widgets#######################
        self.search_text = QLabel("Search")
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("Search For Products")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_products)
        self.search_button.setStyleSheet(style.search_button_style())

        # #########################Right middle layout widgets###########
        self.all_products = QRadioButton("All Products")
        self.avaialable_products = QRadioButton("Available")
        self.not_avaialable_products = QRadioButton("Not Available")
        self.list_button = QPushButton("List")
        self.list_button.clicked.connect(self.list_products)
        self.list_button.setStyleSheet(style.list_button_style())

        # #######################Tab2 Widgets#########################
        self.members_table=QTableWidget()
        self.members_table.setColumnCount(4)
        self.members_table.setHorizontalHeaderItem(0, QTableWidgetItem("Member ID"))
        self.members_table.setHorizontalHeaderItem(1, QTableWidgetItem("Member Name"))
        self.members_table.setHorizontalHeaderItem(2, QTableWidgetItem("Member Surname"))
        self.members_table.setHorizontalHeaderItem(3, QTableWidgetItem("Phone"))
        self.members_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.members_table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.members_table.doubleClicked.connect(self.selected_member)
        self.member_search_text = QLabel("Search Members")
        self.member_search_entry = QLineEdit()
        self.member_search_button = QPushButton("Search")
        self.member_search_button.clicked.connect(self.search_members)

        # #########################Tab3 widgets#####################
        self.total_productsLabel = QLabel()
        self.total_member_label = QLabel()
        self.sold_products_label = QLabel()
        self.total_amount_label = QLabel()

    def layouts(self):
        # #####################Tab1 layouts##############
        self.main_layout = QHBoxLayout()
        self.main_left_layout = QVBoxLayout()
        self.main_right_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_middle_layout = QHBoxLayout()
        self.top_groupbox = QGroupBox("Search Box")
        self.top_groupbox.setStyleSheet(style.search_box_style())
        self.middle_groupbox = QGroupBox("List Box")
        self.middle_group_box.setStyleSheet(style.list_box_style())
        self.bottom_groupbox = QGroupBox()

        # ################Add widgets###################
        # ###############Left main layout widget###########
        self.main_left_layout.addWidget(self.products_table)

        # #######################Right top layout widgets#########
        self.right_top_layout.addWidget(self.search_text)
        self.right_top_layout.addWidget(self.search_entry)
        self.right_top_layout.addWidget(self.search_button)
        self.top_groupbox.setLayout(self.right_top_layout)

        # ################Right middle layout widgets##########
        self.right_middle_layout.addWidget(self.all_products)
        self.right_middle_layout.addWidget(self.avaialable_products)
        self.right_middle_layout.addWidget(self.not_avaialable_products)
        self.right_middle_layout.addWidget(self.list_button)
        self.middle_groupbox.setLayout(self.right_middle_layout)

        self.main_right_layout.addWidget(self.top_groupbox, 20)
        self.main_right_layout.addWidget(self.middle_groupbox, 20)
        self.main_right_layout.addWidget(self.bottom_groupbox, 60)
        self.mainLayout.addLayout(self.main_left_layout, 70)
        self.mainLayout.addLayout(self.main_right_layout, 30)
        self.tab1.setLayout(self.main_layout)

        # #####################Tab2 Layouts#####################
        self.memberMainLayout=QHBoxLayout()
        self.memberLeftLayout=QHBoxLayout()
        self.memberRightLayout=QHBoxLayout()
        self.memberRightGroupBox=QGroupBox("Search For Members")
        self.memberRightGroupBox.setContentsMargins(10,10,10,600)
        self.memberRightLayout.addWidget(self.memberSearchText)
        self.memberRightLayout.addWidget(self.memberSearchEntry)
        self.memberRightLayout.addWidget(self.memberSearchButton)
        self.memberRightGroupBox.setLayout(self.memberRightLayout)

        self.memberLeftLayout.addWidget(self.membersTable)
        self.memberMainLayout.addLayout(self.memberLeftLayout,70)
        self.memberMainLayout.addWidget(self.memberRightGroupBox,30)
        self.tab2.setLayout(self.memberMainLayout)

        #####################Tab3 layouts########################
        self.statisticsMainLayout=QVBoxLayout()
        self.statisticsLayout=QFormLayout()
        self.statisticsGroupBox=QGroupBox("Statistics")
        self.statisticsLayout.addRow("Total Products:",self.totalProductsLabel)
        self.statisticsLayout.addRow("Total Member:",self.totalMemberLabel)
        self.statisticsLayout.addRow("Sold Products:",self.soldProductsLabel)
        self.statisticsLayout.addRow("Total Amount:",self.totalAmountLabel)

        self.statisticsGroupBox.setLayout(self.statisticsLayout)
        self.statisticsGroupBox.setFont(QFont("Arial",20))
        self.statisticsMainLayout.addWidget(self.statisticsGroupBox)
        self.tab3.setLayout(self.statisticsMainLayout)
        self.tabs.blockSignals(False)



    def funcAddProduct(self):
        self.newProduct=addproduct.AddProduct()

    def funcAddMember(self):
        self.newMember=addmember.AddMember()

    def displayProducts(self):
        self.productsTable.setFont(QFont("Times",12))
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        query = cur.execute("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,product_availability FROM products")
        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        self.productsTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def displayMembers(self):
        self.membersTable.setFont(QFont("Times",12))
        for i in reversed(range(self.membersTable.rowCount())):
            self.membersTable.removeRow(i)

        members=cur.execute("SELECT * FROM members")
        for row_data in members:
            row_number = self.membersTable.rowCount()
            self.membersTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.membersTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

        self.membersTable.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def selectedProduct(self):
        global productId
        listProduct=[]
        for i in range(0,6):
            listProduct.append(self.productsTable.item(self.productsTable.currentRow(),i).text())

        productId=listProduct[0]
        self.display=DisplayProduct()
        self.display.show()

    def selectedMember(self):
        global memberId
        listMember=[]
        for i in range(0,4):
            listMember.append(self.membersTable.item(self.membersTable.currentRow(),i).text())

        memberId=listMember[0]
        self.displayMember=DisplayMember()
        self.displayMember.show()

    def searchProducts(self):
        value=self.searchEntry.text()
        if value == "":
            QMessageBox.information(self,"Warning","Search query cant be empty!!!")

        else:
            self.searchEntry.setText("")

            query=("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,product_availability FROM products WHERE product_name LIKE ? or product_manufacturer LIKE ?")
            results=cur.execute(query,('%' + value + '%','%' + value + '%')).fetchall()
            print(results)

            if results == []:
                QMessageBox.information(self,"Warning","There is no such a product or manufacturer")

            else:
                for i in reversed(range(self.productsTable.rowCount())):
                    self.productsTable.removeRow(i)

                for row_data in results:
                    row_number = self.productsTable.rowCount()
                    self.productsTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.productsTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def searchMembers(self):
        value = self.memberSearchEntry.text()
        if value == "":
            QMessageBox.information(self,"Warning","Search query can not be empty")

        else:
            self.memberSearchEntry.setText("")
            query=("SELECT * FROM members WHERE member_name LIKE ? or member_surname LIKE ? or member_phone LIKE ?")
            results=cur.execute(query,('%' + value + '%', '%' + value + '%', '%' + value + '%')).fetchall()
            if results == []:
                QMessageBox.information(self,"Warning","There is no such a member")
            else:
                for i in reversed(range(self.membersTable.rowCount())):
                    self.membersTable.removeRow(i)

                for row_data in results:
                    row_number = self.membersTable.rowCount()
                    self.membersTable.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.membersTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))



    def listProducts(self):
        if self.allProducts.isChecked() == True:
            self.displayProducts()

        elif self.avaialableProducts.isChecked():
            query=("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,"
                   "product_availability FROM products WHERE product_availability='Available'")
            products=cur.execute(query).fetchall()
            print(products)

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        elif self.notAvaialableProducts.isChecked():
            query = ("SELECT product_id,product_name,product_manufacturer,product_price,product_qouta,"
                     "product_availability FROM products WHERE product_availability='UnAvailable'")
            products = cur.execute(query).fetchall()
            print(products)

            for i in reversed(range(self.productsTable.rowCount())):
                self.productsTable.removeRow(i)

            for row_data in products:
                row_number = self.productsTable.rowCount()
                self.productsTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))


    def funcSellProducts(self):
        self.sell = sellings.SellProducts()


    def getStatistics(self):
        countProducts=cur.execute("SELECT count(product_id) FROM products").fetchall()
        countMembers = cur.execute("SELECT count(member_id) FROM members").fetchall()
        soldProducts = cur.execute("SELECT SUM(selling_quantity) FROM sellings").fetchall()
        totalAmount = cur.execute("SELECT SUM(selling_amount) FROM sellings").fetchall()
        totalAmount = totalAmount[0][0]
        soldProducts = soldProducts[0][0]
        countMembers = countMembers[0][0]
        countProducts = countProducts[0][0]
        self.totalProductsLabel.setText(str(countProducts))
        self.totalMemberLabel.setText(str(countMembers))
        self.soldProductsLabel.setText(str(soldProducts))
        self.totalAmountLabel.setText(str(totalAmount)+" $")

    def tabChanged(self):
        self.getStatistics()
        self.displayProducts()
        self.displayMembers()



class DisplayMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Member Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,350,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.memberDetails()
        self.widgets()
        self.layouts()


    def memberDetails(self):
        global memberId
        query=("SELECT * FROM members WHERE member_id=?")
        member=cur.execute(query,(memberId,)).fetchone()
        self.memberName=member[1]
        self.memberSurname=member[2]
        self.memberPhone=member[3]

    def widgets(self):
        ###############Widgets of top layout############
        self.memberImg=QLabel()
        self.img=QPixmap('icons/members.png')
        self.memberImg.setPixmap(self.img)
        self.memberImg.setAlignment(Qt.AlignCenter)
        self.titleText=QLabel("Display Member")
        self.titleText.setAlignment(Qt.AlignCenter)
        ###################widgets of bottom layout#########
        self.nameEntry=QLineEdit()
        self.nameEntry.setText(self.memberName)
        self.surnameEntry=QLineEdit()
        self.surnameEntry.setText(self.memberSurname)
        self.phoneEntry=QLineEdit()
        self.phoneEntry.setText(self.memberPhone)
        self.updateBtn=QPushButton("Update")
        self.updateBtn.clicked.connect(self.updateMember)
        self.deleteBtn=QPushButton("Delete")
        self.deleteBtn.clicked.connect(self.deleteMember)



    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.topFrame.setStyleSheet(style.memberTopFrame())
        self.bottomFrame=QFrame()
        self.bottomFrame.setStyleSheet(style.memberBottomFrame())
        ##############add widgets######3
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.memberImg)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel("Name: "),self.nameEntry)
        self.bottomLayout.addRow(QLabel("Surname: "),self.surnameEntry)
        self.bottomLayout.addRow(QLabel("Phone: "),self.phoneEntry)
        self.bottomLayout.addRow(QLabel(""),self.updateBtn)
        self.bottomLayout.addRow(QLabel(""),self.deleteBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)


    def deleteMember(self):
        global memberId
        mbox=QMessageBox.question(self,"Warning","Are you sure to delete this member",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)

        if mbox == QMessageBox.Yes:
            try:
                query="DELETE FROM members WHERE member_id=?"
                cur.execute(query,(memberId,))
                con.commit()
                QMessageBox.information(self,"Info","Member has been deleted!")
            except:
                QMessageBox.information(self,"Info","Member has not been deleted!")


    def updateMember(self):
        global memberId
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()

        if (name and surname and phone !=""):
            try:
                query="UPDATE members set member_name=?, member_surname=?, member_phone=? WHERE member_id=?"
                cur.execute(query,(name,surname,phone,memberId))
                con.commit()
                QMessageBox.information(self,"Info","Member has been updated!")

            except:
                QMessageBox.information(self,"Info","Member has been updated!")

        else:
            QMessageBox.information(self, "Info", "Fields can not be empty!")

class DisplayProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Details")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450,150,350,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
      self.productDetails()
      self.widgets()
      self.layouts()


    def productDetails(self):
        global productId
        query=("SELECT * FROM products WHERE product_id=?")
        product=cur.execute(query,(productId,)).fetchone()#single item tuple=(1,)
        self.productName=product[1]
        self.productManufacturer=product[2]
        self.productPrice=product[3]
        self.productQouta=product[4]
        self.productImg=product[5]
        self.productStatus=product[6]

    def widgets(self):
        #################Top layouts wigdets#########
        self.product_Img=QLabel()
        self.img=QPixmap('img/{}'.format(self.productImg))
        self.product_Img.setPixmap(self.img)
        self.product_Img.setAlignment(Qt.AlignCenter)
        self.titleText=QLabel("Update Product")
        self.titleText.setAlignment(Qt.AlignCenter)

        ##############Bottom Layout's widgets###########
        self.nameEntry=QLineEdit()
        self.nameEntry.setText(self.productName)
        self.manufacturerEntry=QLineEdit()
        self.manufacturerEntry.setText(self.productManufacturer)
        self.priceEntry=QLineEdit()
        self.priceEntry.setText(str(self.productPrice))
        self.qoutaEntry=QLineEdit()
        self.qoutaEntry.setText(str(self.productQouta))
        self.availabilityCombo=QComboBox()
        self.availabilityCombo.addItems(["Available","UnAvailable"])
        self.uploadBtn=QPushButton("Upload")
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.deleteBtn=QPushButton("Delete")
        self.deleteBtn.clicked.connect(self.deleteProduct)
        self.updateBtn=QPushButton("Update")
        self.updateBtn.clicked.connect(self.updateProduct)




    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.topFrame.setStyleSheet(style.productTopFrame())
        self.bottomFrame=QFrame()
        self.bottomFrame.setStyleSheet(style.productBottomFrame())
        ###############add widgets###########
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.product_Img)
        self.topFrame.setLayout(self.topLayout)
        self.bottomLayout.addRow(QLabel("Name: "),self.nameEntry)
        self.bottomLayout.addRow(QLabel("Manufacturer: "),self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel("Price: "),self.priceEntry)
        self.bottomLayout.addRow(QLabel("Qouta: "),self.qoutaEntry)
        self.bottomLayout.addRow(QLabel("Status: "),self.availabilityCombo)
        self.bottomLayout.addRow(QLabel("Image: "),self.uploadBtn)
        self.bottomLayout.addRow(QLabel(""),self.deleteBtn)
        self.bottomLayout.addRow(QLabel(""),self.updateBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)


        self.setLayout(self.mainLayout)



    def uploadImg(self):
        size =(256,256)
        self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
        if ok:
            self.productImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("img/{0}".format(self.productImg))

    def updateProduct(self):
        global productId
        name = self.nameEntry.text()
        manufacturer=self.manufacturerEntry.text()
        price=int(self.priceEntry.text())
        qouta=int(self.qoutaEntry.text())
        status=self.availabilityCombo.currentText()
        defaultImg=self.productImg

        if (name and manufacturer and price and qouta !=""):

            try:
                query="UPDATE products set product_name=?, product_manufacturer =?, product_price=?,product_qouta=?, product_img=?, product_availability=? WHERE product_id=?"
                cur.execute(query,(name,manufacturer,price,qouta,defaultImg,status,productId))
                con.commit()
                QMessageBox.information(self,"Info","Product has been updated!")
            except:
                QMessageBox.information(self, "Info", "Product has not been updated!")
        else:
            QMessageBox.information(self, "Info", "Fields cant be empty!")

    def deleteProduct(self):
        global productId

        mbox=QMessageBox.question(self,"Warning","Are you sure to delete this product",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)

        if(mbox==QMessageBox.Yes):
            try:
                cur.execute("DELETE FROM products WHERE product_id=?",(productId,))
                con.commit()
                QMessageBox.information(self,"Information","Product has been deleted!")
                self.close()

            except:
                QMessageBox.information(self, "Information", "Product has not been deleted!")


def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()