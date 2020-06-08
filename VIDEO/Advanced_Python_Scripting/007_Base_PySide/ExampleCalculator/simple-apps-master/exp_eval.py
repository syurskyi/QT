import sys
#from __future__ import division
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__ (self, parent=None):
        super (Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        self.button = QPushButton(" = ")
        self.button.setFixedSize(40,25)

        layout_eval = QHBoxLayout()
        layout_eval.addWidget(self.lineedit)
        layout_eval.addWidget(self.button)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addLayout(layout_eval)
        self.setLayout(layout)
        
        self.lineedit.setFocus()
        #self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        #not necessary since the button connect links return to clicked()
        self.connect(self.button, SIGNAL("clicked()"), self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = unicode(self.lineedit.text())
            self.lineedit.clear()
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except SyntaxError:
            pass
        except NameError:
            self.browser.append(
                "<font color=red>%s is invalid!<br></font>\n" % text)

def main():
    app = QApplication (sys.argv)
    calculator = Form()
    calculator.show()
    app.exec_()

if __name__ == '__main__':
    main()
