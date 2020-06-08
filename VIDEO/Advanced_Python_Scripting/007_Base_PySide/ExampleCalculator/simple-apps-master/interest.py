import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        principalLabel  = QLabel("Principal:")
        rateLabel       = QLabel("Rate:")
        yearsLabel      = QLabel("Years:")
        amountLabel     = QLabel("Amount:")
        self.valueLabel = QLabel("$ 0.00")

        self.principalSpinBox=QDoubleSpinBox()
        self.principalSpinBox.setRange(0.00, 10000.00)
        self.principalSpinBox.setSingleStep(1)
        self.principalSpinBox.setPrefix("$ ")

        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setRange(0.00, 999.99)
        self.rateSpinBox.setSingleStep(0.01)
        self.rateSpinBox.setValue(3.25)
        self.rateSpinBox.setSuffix(" %")
        
        self.yearsComboBox = QComboBox()
        self.yearsComboBox.addItem("1 year")
        for i in range(1, 100):
            self.yearsComboBox.addItem("%d years" % (i+1))
        
        grid = QGridLayout()
        grid.addWidget (principalLabel, 0, 0)
        grid.addWidget (rateLabel, 1, 0)
        grid.addWidget (yearsLabel, 2, 0)
        grid.addWidget (amountLabel, 3, 0)
        
        grid.addWidget (self.principalSpinBox, 0, 1)
        grid.addWidget (self.rateSpinBox, 1, 1)
        grid.addWidget (self.yearsComboBox, 2, 1)
        grid.addWidget (self.valueLabel, 3, 1)
        self.setLayout(grid)

        self.connect (self.principalSpinBox,
            SIGNAL("valueChanged(double)"), self.updateValue)
        self.connect (self.rateSpinBox,
            SIGNAL("valueChanged(double)"), self.updateValue)
        self.connect (self.yearsComboBox,
            SIGNAL("currentIndexChanged(int)"), self.updateValue)

        self.setWindowTitle("Interest")
        
    def updateValue(self):
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value()
        years = self.yearsComboBox.currentIndex()+1
        value = principal * ( ( 1 + (rate/100.0) ) **years )
        self.valueLabel.setText("$ %.2f" % value)


def main():
    app = QApplication ( sys.argv )
    interest = Form()
    interest.show()
    app.exec_()

if __name__ == '__main__':
    main()
