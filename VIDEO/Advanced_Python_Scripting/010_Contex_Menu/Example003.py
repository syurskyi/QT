import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *



class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        QTableWidget.__init__(self, parent)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)

        quitAction = QAction("Quit", self)
        quitAction.triggered.connect(qApp.quit)
        self.addAction(quitAction)


app = QApplication([])
tableWidget = TableWidget()
tableWidget.show()
sys.exit(app.exec_())