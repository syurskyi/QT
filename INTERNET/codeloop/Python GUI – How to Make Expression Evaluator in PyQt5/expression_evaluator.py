from PyQt5.QtWidgets import QApplication, QTextBrowser, QLineEdit,QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Simple Application"
        self.top = 400
        self.left = 400
        self.width = 800
        self.height = 600

        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QIcon('icon.png'))
        self.Ui()

    def Ui(self):
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit("Type An Expression And Hit Enter")
        vbox = QVBoxLayout()
        vbox.addWidget(self.browser)
        vbox.addWidget(self.lineEdit)
        self.setLayout(vbox)
        self.lineEdit.returnPressed.connect(self.updateBrowser)

    def updateBrowser(self):
        try:
            text = str(self.lineEdit.text())
            self.browser.append("%s = <b>%s</b>" %(text, eval(text)))
        except:
            self.browser.append(
                "<font color = red > %s Is Invalid </font>" %text)


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()