from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QDialog,QTabWidget, QComboBox, QCheckBox ,QGroupBox ,QVBoxLayout, QWidget, QLabel, QLineEdit, QDialogButtonBox
import sys
from PyQt5.QtGui import QIcon



class Tab(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 TabWidget Example")
        self.setWindowIcon(QIcon("icon.png"))
        #self.setStyleSheet('background-color:grey')
        vbox = QVBoxLayout()
        tabWidget = QTabWidget()
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        tabWidget.setFont(QtGui.QFont("Sanserif", 12))
        tabWidget.addTab(TabContact(), "Contact Details")
        tabWidget.addTab(TabPeronsalDetails(), "Personal Details")
        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonbox)
        self.setLayout(vbox)


class TabContact(QWidget):
    def __init__(self):
        super().__init__()
        nameLabel = QLabel("Name: ")
        nameEdit = QLineEdit()
        phone = QLabel("Phone:")
        phoneedit = QLineEdit()
        addr = QLabel("Address:")
        addredit = QLineEdit()
        email = QLabel("Email:")
        emailedit = QLineEdit()
        vbox = QVBoxLayout()
        vbox.addWidget(nameLabel)
        vbox.addWidget(nameEdit)
        vbox.addWidget(phone)
        vbox.addWidget(phoneedit)
        vbox.addWidget(addr)
        vbox.addWidget(addredit)
        vbox.addWidget(email)
        vbox.addWidget(emailedit)
        self.setLayout(vbox)


class TabPeronsalDetails(QWidget):
    def __init__(self):
        super().__init__()
        groupBox = QGroupBox("Select Your Gender")
        list = ["Male", "Female"]
        combo = QComboBox()
        combo.addItems(list)
        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        groupBox.setLayout(vbox)
        groupBox2 = QGroupBox("Select Your Favorite Programming Language")
        python =QCheckBox("Python")
        cpp = QCheckBox("C++")
        java = QCheckBox("Java")
        csharp = QCheckBox("C#")
        vboxp = QVBoxLayout()
        vboxp.addWidget(python)
        vboxp.addWidget(cpp)
        vboxp.addWidget(java)
        vboxp.addWidget(csharp)
        groupBox2.setLayout(vboxp)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupBox2)
        self.setLayout(mainLayout)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabdialog = Tab()
    tabdialog.show()
    app.exec()