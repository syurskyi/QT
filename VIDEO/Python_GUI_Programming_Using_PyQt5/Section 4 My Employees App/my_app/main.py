from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sys
import os
import sqlite3
from PIL import Image


connection = sqlite3.connect('employees.db')
cursor = connection.cursor()
default_image = "person.png"
person_id = None


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450, 150, 750, 600)
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layouts()
        self.get_employees()
        self.display_first_record()

    def main_design(self):
        self.setStyleSheet("font-size:14pt; font-family:Arial Bold;")
        self.employee_list = QListWidget()
        self.employee_list.itemClicked.connect(self.single_click)
        self.btn_new = QPushButton("New")
        self.btn_new.clicked.connect(self.add_employee)
        self.btn_update = QPushButton("Update")
        self.btn_update.clicked.connect(self.update_employee)
        self.btn_delete = QPushButton("Delete")
        self.btn_delete.clicked.connect(self.delete_employee)

    def layouts(self):
        # ###############################Layouts#####################################################################

        self.main_layout = QHBoxLayout()
        self.left_layout = QFormLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        self.right_bottom_layout = QHBoxLayout()

        # ###############################Adding child layouts to main layout#########################################

        self.right_main_layout.addLayout(self.right_top_layout)
        self.right_main_layout.addLayout(self.right_bottom_layout)
        self.main_layout.addLayout(self.left_layout, 40)
        self.main_layout.addLayout(self.right_main_layout, 60)

        # ###############################adding widgets to layouts###################################################

        self.right_top_layout.addWidget(self.employee_list)
        self.right_bottom_layout.addWidget(self.btn_new)
        self.right_bottom_layout.addWidget(self.btn_update)
        self.right_bottom_layout.addWidget(self.btn_delete)

        # ###############################Setting main window layout##################################################

        self.setLayout(self.main_layout)

    def add_employee(self):
        self.new_employee = AddEmployer()
        self.close()

    def get_employees(self):
        query = "SELECT id, name, surname FROM employees"
        employees = cursor.execute(query).fetchall()
        for employee in employees:
            print(employee)
            self.employee_list.addItem(str(employee[0]) + "-" + employee[1] + " " + employee[2])

    def display_first_record(self):
        query = "SELECT * FROM employees ORDER BY ROWID ASC LIMIT 1"
        employee = cursor.execute(query).fetchone()
        print(employee)
        image = QLabel()
        image.setPixmap(QPixmap("images/" + employee[5]))
        name = QLabel(employee[1])
        surname = QLabel(employee[2])
        phone = QLabel(employee[3])
        email = QLabel(employee[4])
        address = QLabel(employee[6])
        self.left_layout.setVerticalSpacing(20)
        self.left_layout.addRow("", image)
        self.left_layout.addRow("Name: ", name)
        self.left_layout.addRow("Surname :", surname)
        self.left_layout.addRow("Phone :", phone)
        self.left_layout.addRow("Email :", email)
        self.left_layout.addRow("Address:", address)

    def single_click(self):

        for i in reversed(range(self.left_layout.count())):
            widget = self.left_layout.takeAt(i).widget()

            if widget is not None:
                widget.deleteLater()

        employee = self.employee_list.currentItem().text()
        print(employee)
        id = employee.split('-')[0]
        query = ("SELECT * FROM employees WHERE id =?")
        person = cursor.execute(query, (id,)).fetchone()
        print(person)
        image = QLabel()
        image.setPixmap(QPixmap("images/" + person[5]))
        name = QLabel(person[1])
        surname = QLabel(person[2])
        phone = QLabel(person[3])
        email = QLabel(person[4])
        address = QLabel(person[6])
        self.left_layout.setVerticalSpacing(20)
        self.left_layout.addRow("", image)
        self.left_layout.addRow("Name: ", name)
        self.left_layout.addRow("Surname :", surname)
        self.left_layout.addRow("Phone :", phone)
        self.left_layout.addRow("Email :", email)
        self.left_layout.addRow("Address:", address)

    def delete_employee(self):
        if self.employee_list.selectedItems():
            person = self.employee_list.currentItem().text()
            id = person.split("-")[0]
            mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this person?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM employees WHERE id=?"
                    cursor.execute(query, (id,))
                    connection.commit()
                    QMessageBox.information(self, "Info!!!", "Person has been deleted")
                    self.close()
                    self.main = Main()

                except:
                    QMessageBox.information(self, "Warning!!!", "Person has not been deleted")

        else:
            QMessageBox.information(self, "Warning!!!", "Please select a person to delete")

    def update_employee(self):
        # pass
        global person_id
        if self.employee_list.selectedItems():
            person = self.employee_list.currentItem().text()
            person_id = person.split("-")[0]
            self.update_window = UpdateEmployee()
            self.close()

        else:
            QMessageBox.information(self, "Warning!!!", "Please select a person to update")


class UpdateEmployee(QWidget):
    # pass
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Employee")
        self.setGeometry(450, 150, 350, 600)
        self.ui()
        self.show()

    def ui(self):
        # pass
        self.get_person()
        self.main_design()
        self.layouts()

    def closeEvent(self, event):
        # pass
        self.main = Main()

    def get_person(self):
        # pass
        global person_id
        query = "SELECT * FROM employees WHERE id = ?"
        employee = cursor.execute(query, (person_id,)).fetchone()
        print(employee)

        self.name = employee[1]
        self.surname = employee[2]
        self.phone = employee[3]
        self.email = employee[4]
        self.image = employee[5]
        self.address = employee[6]

    def main_design(self):
        # pass
        # ###############Top Layout widgets#######################
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        self.title = QLabel("Update Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold;')
        self.image_add = QLabel()
        self.image_add.setPixmap(QPixmap("images/{}".format(self.image)))
        # # ##################Bottom Layout Widgets#####################
        self.name_lbl = QLabel("Name :")
        self.name_entry = QLineEdit()
        self.name_entry.setText(self.name)
        self.surname_lbl = QLabel("Surname :")
        self.surname_entry = QLineEdit()
        self.surname_entry.setText(self.surname)
        self.phone_lbl = QLabel("Phone :")
        self.phone_entry = QLineEdit()
        self.phone_entry.setText(self.phone)
        self.email_lbl = QLabel("Email :")
        self.email_entry = QLineEdit()
        self.email_entry.setText(self.email)
        self.image_lbl = QLabel("Picture: ")
        self.image_button = QPushButton("Browse")
        self.image_button.setStyleSheet("background-color:orange;font-size:10pt")
        self.image_button.clicked.connect(self.upload_image)
        self.address_lbl = QLabel("Address: ")
        self.address_editor = QTextEdit()
        self.address_editor.setText(self.address)
        self.add_button = QPushButton("Update")
        self.add_button.setStyleSheet("background-color:orange;font-size:10pt")
        self.add_button.clicked.connect(self.update_employee)

    def layouts(self):
        # pass
        # #################creating main layouts##########
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        #
        # ##########adding child layouts to main layout##############
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        #
        # # #################adding wigdets to layouts##############
        # # #############top layout################
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget(self.image_add)
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)  # left,top,right,bottom
        # # ##########bottom layout#################
        self.bottom_layout.addRow(self.name_lbl, self.name_entry)
        self.bottom_layout.addRow(self.surname_lbl, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lbl, self.phone_entry)
        self.bottom_layout.addRow(self.email_lbl, self.email_entry)
        self.bottom_layout.addRow(self.image_lbl, self.image_button)
        self.bottom_layout.addRow(self.address_lbl, self.address_editor)
        self.bottom_layout.addRow("", self.add_button)
        #
        # # ##########setting main layout for window##################
        self.setLayout(self.main_layout)

    def upload_image(self):
        # pass
        global default_image
        size = (128, 128)
        self.file_name, ok =QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image Files (*.jpg *.png)')

        if ok:

            default_image = os.path.basename(self.file_name)
            image = Image.open(self.file_name)
            imgage = image.resize(size)
            image.save("images/{}".format(default_image))

    def update_employee(self):
        # pass
        global default_image
        global person_id
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        img = default_image
        address = self.address_editor.toPlainText()

        if (name and surname and phone !=""):
            try:
                query = "UPDATE employees set name =?, surname=?, phone=?,email=?,img=?,address=? WHERE id=?"
                cursor.execute(query, (name, surname, phone, email, img, address, person_id))
                connection.commit()
                QMessageBox.information(self, "Success", "Person has been updated")
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self, "Warning", "Person has not been updated")

        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")


class AddEmployer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employee")
        self.setGeometry(450, 150, 350, 600)
        self.ui()
        self.show()

    def ui(self):
        self.main_design()
        self.layouts()

    def closeEvent(self, event):
        self.main = Main()

    def main_design(self):

        # ##############Top Layout widgets#######################

        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        self.title = QLabel("Add Person")
        self.title.setStyleSheet("font-size: 24pt; font-family; Arial Bold;")
        self.img_add = QLabel()
        self.img_add.setPixmap(QPixmap("icons/person.png"))

        # ##################Bottom Layout Widgets#####################

        self.name_lbl = QLabel("Name :")
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Enter Employee Name")
        self.surname_lbl = QLabel("Surname :")
        self.surname_entry = QLineEdit()
        self.surname_entry.setPlaceholderText("Enter Employee Surname")
        self.phone_lbl = QLabel("Phone :")
        self.phone_entry = QLineEdit()
        self.phone_entry.setPlaceholderText("Enter Employee Phone Number")
        self.email_lbl = QLabel("Email :")
        self.email_entry = QLineEdit()
        self.email_entry.setPlaceholderText("Enter Employee Email")
        self.img_lbl = QLabel("Picture: ")
        self.img_button = QPushButton("Browse")
        self.img_button.setStyleSheet("background-color:orange;font-size:10pt")
        self.img_button.clicked.connect(self.upload_image)
        self.address_lbl = QLabel("Address: ")
        self.address_editor = QTextEdit()
        self.add_button = QPushButton("Add")
        self.add_button.setStyleSheet("background-color:orange;font-size:10pt")
        self.add_button.clicked.connect(self.add_employee)

    def layouts(self):

        # #########################creating main layout########################################################

        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()

        # #########################adding child layoutd to main layout#########################################

        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout((self.bottom_layout))

        # #########################adding widget to layout#####################################################
        # #########################top layout################

        self.top_layout.addStretch()
        self.top_layout.addWidget(self.title)
        self.top_layout.addWidget((self.img_add))
        self.top_layout.addStretch()
        self.top_layout.setContentsMargins(110, 20, 10, 30)

        # #########################bottom layout################

        self.bottom_layout.addRow(self.name_lbl, self.name_entry)
        self.bottom_layout.addRow(self.surname_lbl, self.surname_entry)
        self.bottom_layout.addRow(self.phone_lbl, self.phone_entry)
        self.bottom_layout.addRow(self.email_lbl, self.email_entry)
        self.bottom_layout.addRow(self.img_lbl, self.img_button)
        self.bottom_layout.addRow(self.address_lbl, self.address_editor)
        self.bottom_layout.addRow("", self.add_button)

        # #########################setting main layout for window##############################################

        self.setLayout(self.main_layout)

    def upload_image(self):
        global default_image
        size = (128, 128)
        self.file_name, ok = QFileDialog.getOpenFileName(self, "Upload Image", '', "Image Files(*.jpg *.png)")

        if ok:
            print(self.file_name)
            default_image = os.path.basename(self.file_name)
            print(default_image)
            image = Image.open(self.file_name)
            image = image.resize(size)
            image.save("images/{}".format(default_image))

    def add_employee(self):
        global default_image
        name = self.name_entry.text()
        surname = self.surname_entry.text()
        phone = self.phone_entry.text()
        email = self.email_entry.text()
        image = default_image
        address = self.address_editor.toPlainText()

        if (name and surname and phone != ""):
            try:
                query = "INSERT INTO employees(name, surname, phone, email, image, address) VALUES(?, ? , ? , ? , ? ,?)"
                cursor.execute(query, (name, surname, phone, email, image, address))
                connection.commit()
                QMessageBox.information(self, "Success", "Person has been added")
                self.close()
                self.main = Main()
            except:
                QMessageBox.information(self, "Warning", "Person has not been added")
        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")


def main():
    APP = QApplication(sys.argv)
    window = Main()
    sys.exit(APP.exec_())


if __name__ == '__main__':
    main()
