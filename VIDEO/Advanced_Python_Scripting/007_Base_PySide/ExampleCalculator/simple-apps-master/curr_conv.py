import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        date = self.getdata()
        countries = sorted(self.rates.keys())
        
        #defaults
        from_ = 'European Euro'
        to = 'Romanian New Leu'
        
        #self. hence reference before assignment
        dateLabel = QLabel(date)
        #those above are referred to only inside __init__() so there
        #is no need to keep references to them in the class instance
        self.toLabel = QLabel()

        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(countries)
        self.fromComboBox.setCurrentIndex(countries.index(from_))

        self.toComboBox = QComboBox()
        self.toComboBox.addItems(countries)
        self.toComboBox.setCurrentIndex(countries.index(to))

        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.0, 10000.0)
        self.fromSpinBox.setSingleStep(0.1)
        self.fromSpinBox.setValue(1.0)
        self.fromSpinBox.setDecimals(1)

        icon = QIcon("switch.png")
        self.switch = QPushButton()
        self.switch.setIcon(icon)
        self.switch.setAutoDefault(False)
        
        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.switch, 0, 1)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        self.updateUi()
        self.connect(self.switch, SIGNAL("clicked()"), self.switchCurr)
        self.connect(self.fromComboBox,
            SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox,
            SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox,
            SIGNAL("valueChanged(double)"), self.updateUi)
        self.setWindowTitle("Currency")


    def updateUi(self):
        to = unicode(self.toComboBox.currentText())
        from_ = unicode(self.fromComboBox.currentText())
        conv_rate = self.fromSpinBox.value()
        amount = (self.rates[from_] / self.rates[to]) * conv_rate
        self.toLabel.setText("%0.2f" % amount)

    def switchCurr(self):
        aux_index = self.toComboBox.currentIndex()
        self.toComboBox.setCurrentIndex ( self.fromComboBox.currentIndex() )
        self.fromComboBox.setCurrentIndex ( aux_index )
        self.updateUi()

        
    def getdata(self): # Idea taken from the Python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            for line in fh:
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1] #str date = last date
                    date = date[:-2] #sterg \n din final
                else:
                    try:
                        value = float(fields[-1]) #float value = last value
                        self.rates[unicode(fields[0])] = value
                        #fill up dict key=country, value = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception, e:
            return "Failed to download:\n%s" % e



def main():
    app = QApplication (sys.argv)
    converter = Form()
    converter.show()
    app.exec_()

if __name__ == '__main__':
    main()
