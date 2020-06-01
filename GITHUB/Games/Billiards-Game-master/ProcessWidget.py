from PyQt5.QtWidgets import *
from PyQt5  import QtCore
# from PyQt4.QtCore import *
import psutil

class MyTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.but = QPushButton(self)
        self.but.setText("终止")
        # self.setGeometry(200, 200, 1000, 500)
        self.but.setGeometry(700, 0, 50, 50)
        self.but.clicked.connect(self.ButtonClickedSignal)

        pids = psutil.pids()
        self.ProcessDict = list()
        self.ProcessList = list()
        self.count = 0

        title = ['pid', 'Name', 'Create Time', ' Memory Info()','Process State']
        self.setColumnCount(len(title))
        self.setRowCount(10)
        for pid in pids:
            p = psutil.Process(pid)

            # p.terminate()
            self.ProcessDict.append([pid, p.name(), p.create_time()])
            self.setHorizontalHeaderLabels(title)

            self.ProcessList.append(p)
            #
            self.insertRow(self.count)
            self.setItem(self.count, 0, QTableWidgetItem(str(pid)))
            self.setItem(self.count, 1, QTableWidgetItem(str(p.name())))
            self.setItem(self.count, 2, QTableWidgetItem(str(p.create_time())))
            self.setItem(self.count, 3, QTableWidgetItem(str(p.memory_percent())))  # 进程使用的内存())))
            self.setItem(self.count, 4, QTableWidgetItem(str(p.status())))  # 进程使用的内存())))
            print("finished")
            self.count += 1

            # temp = str(p.name())

        # self.table.setRowCount(len(self.ProcessList))

        #


    def ButtonClickedSignal(self):

        i = self.currentRow()
        self.curRow =i
        for j in range(5):
            item = self.takeItem(i,j)
            item = None

        self.ProcessList[i].terminate()
        self.ProcessList.pop(i)
        self.ProcessDict.pop(i)

        print(self.curRow)
        QApplication.processEvents()
        self.update()
        # self.emit(i)
class ProcessWidget(QMainWindow):
    def __init__(self):
        super().__init__()



        self.table = MyTableWidget()

        # self.but = QPushButton(self)
        # self.but.setText("终止")
        self.setGeometry(200, 200, 1000, 500)
        # self.but.setGeometry(700, 0, 50, 50)

        # self.but.clicked.connect(self.ButtonClickedSignal)
        self.setCentralWidget(self.table)





        self.show()
        # self.connect(self.table, QtCore.PYQT_SIGNAL("clicked()"), self.RecieveData)
        # self.update()
        # self.repaint();

    def RecieveData(self,i):
        print(i)