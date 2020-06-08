import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()
        
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        
        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)
        self.setWindowTitle("Signals and Slots")


def main():
    app = QApplication ( sys.argv )
    dial = Form()
    dial.show()
    app.exec_()

if __name__ == '__main__':
    main()
