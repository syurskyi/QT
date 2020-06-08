from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Calculator(QDialog):
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit()
        #		self.lineedit.selectAll()
        grid = QGridLayout()
        grid.addWidget(self.browser, 0, 0, 4, 2)
        grid.addWidget(self.lineedit, 4, 0, 1, 1)
        names = ['Cls', 'Bck', '', "**", '7', '8', '9', '/',
                 '4', '5', '6', '*', '1', '2', '3', '-',
                 '0', '.', '=', '+']
        k = 0
        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
               (1, 0), (1, 1), (1, 2), (1, 3),
               (2, 0), (2, 1), (2, 2), (2, 3),
               (3, 0), (3, 1), (3, 2), (3, 3),
               (4, 0), (4, 1), (4, 2), (4, 3)]

        self.button = {}
        for i in names:
            self.button[k] = QPushButton(i)
            if j == 2:
                grid.addWidget(QLabel(''), 0, 2)
            else:
                grid.addWidget(self.button[k], pos[j][0], pos[j][1] + 2)
            j = j + 1
            k = k + 1
        self.setLayout(grid)
        self.lineedit.setFocus()
        self.connect(self.button[0], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[1], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[2], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[3], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[4], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[5], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[6], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[7], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[8], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[9], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[10], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[11], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[12], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[13], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[14], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[15], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[16], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[17], SIGNAL("clicked()"), self.buttonclicked)
        #	self.connect(button[18], SIGNAL("clicked()"), self.buttonclicked)
        self.connect(self.button[19], SIGNAL("clicked()"), self.buttonclicked)
        #	self.connect(button[20], SIGNAL("clicked()"), self.buttonclicked)
        self.exp = ' '
        self.connect(self.button[18], SIGNAL("clicked()"), self.updateUi)

    #	self.connect(self.lineedit,SIGNAL("button[18].clicked()"),self.updateUi)
    def buttonclicked(self):
        x = self.sender()
        if (x.text() == "Bck"):
            self.exp = self.exp[:len(self.exp) - 1]
            self.lineedit.setText(self.exp)
        else:
            self.exp = self.exp + x.text()
            self.lineedit.setText(self.exp)

    def updateUi(self):
        try:
            text = unicode(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
            self.exp = ' '
        except:
            self.browser.append("<font color=red>%s iss invalid! </font>" % text)
            self.exp = ' '


def main():
    app = QApplication(sys.argv)
    calculatr = Calculator()
    calculatr.show()
    app.exec_()


if __name__ == '__main__':
    main()