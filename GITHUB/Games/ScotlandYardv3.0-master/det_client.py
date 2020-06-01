import rules
import socket, pickle
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading
import gui

det_no = 1

class Window(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.lis = rules.start()
        self.setupUi(self)

        self.workerthread = WorkerThread(det_no)
        self.workerthread.sig1.connect(self.play_move)
        self.workerthread.sig2.connect(self.find_move)
        self.workerthread.sig3.connect(self.final_move)
        self.workerthread.sig4.connect(self.start_move)
        self.pushButton.clicked.connect(self.but_pushed)

    def start_move(self):
        self.pixmapItem2 = self.scene.addPixmap(self.pix2)
        self.pixmapItem3 = self.scene.addPixmap(self.pix3)
        self.pixmapItem4 = self.scene.addPixmap(self.pix4)
        self.pixmapItem5 = self.scene.addPixmap(self.pix5)
        self.pixmapItem6 = self.scene.addPixmap(self.pix6)

        self.pixmapItem2.setOffset(int(self.lis[1][1]),int(self.lis[1][2])-50)
        self.pixmapItem3.setOffset(int(self.lis[2][1]),int(self.lis[2][2])-50)
        self.pixmapItem4.setOffset(int(self.lis[3][1]),int(self.lis[3][2])-50)
        self.pixmapItem5.setOffset(int(self.lis[4][1]),int(self.lis[4][2])-50)
        self.pixmapItem6.setOffset(int(self.lis[5][1]),int(self.lis[5][2])-50)

    def but_pushed(self):
        self.label.setText("Move is played")

    def play_move(self, x, y):
        if x == 0 and y == 3:
            self.pixmapItem1 = self.scene.addPixmap(self.pix1)
        if y == 3 or y == 8 or y == 13 or y == 18:
            self.pixmapItem1.setOffset(int(self.lis[0][1]),int(self.lis[0][2])-50)

        self.pixmapItem2.setOffset(int(self.lis[1][1]),int(self.lis[1][2])-50)
        self.pixmapItem3.setOffset(int(self.lis[2][1]),int(self.lis[2][2])-50)
        self.pixmapItem4.setOffset(int(self.lis[3][1]),int(self.lis[3][2])-50)
        self.pixmapItem5.setOffset(int(self.lis[4][1]),int(self.lis[4][2])-50)
        self.pixmapItem6.setOffset(int(self.lis[5][1]),int(self.lis[5][2])-50)
        self.comboBox.clear()

    def find_move(self, x):
        labeltext = "Move of Player no." + str(x)
        self.label.setText(labeltext)
        self.det_moves(rules.poss_mov_det(self.lis[x][0],x),x)
        e1.set()

    def final_move():
        self.pixmapItem1.setOffset(int(self.lis[0][1]),int(self.lis[0][2])-50)

    def det_moves(self, pos_trans, num):
        for x in range(len(pos_trans)):
            s = pos_trans[x][0] + " " + pos_trans[x][1]
            self.comboBox.addItem(s)
            QApplication.processEvents()
        while self.label.text() != "Move is played":
            QApplication.processEvents()
        ns = self.comboBox.currentText()
        nl = ns.split (" ")
        t = rules.cord_node[int(nl[0])]
        self.lis[num] = t

class WorkerThread(QThread):
    sig1 = QtCore.pyqtSignal(int, int)
    sig2 = QtCore.pyqtSignal(int)
    sig3 = QtCore.pyqtSignal()
    sig4 = QtCore.pyqtSignal()

    def __init__(self, dn, parent=None):
        super(WorkerThread, self).__init__(parent)
        self.det = dn

    def run(self):
        self.sig4.emit()
        for y in range(22):
            for x in range(6):
                if x == self.det:
                    self.sig2.emit(x)
                e1.wait()
                self.sig1.emit(x, y)
                e1.clear()
        self.sig3.emit()

def screate():
    localhost = "127.0.0.1"
    port = 8080
    screate.mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    screate.mysocket.connect((localhost, port))

    e3.wait()
    data = screate.mysocket.recv(4096)
    gcreate.ui.lis = pickle.loads(data)
    e1.set()

def gcreate():
    app = QtWidgets.QApplication(sys.argv)
    gcreate.ui = Window()

    e3.set()
    e1.wait()
    e1.clear()
    gcreate.ui.pushButton_4.setEnabled(False)
    e2.set()

    gcreate.ui.show()
    sys.exit(app.exec_())

def ncreate():
    for y in range(22):
        for x in range(6):
            if x ==  det_no:
                e1.wait()
                lis1 = pickle.dumps(gcreate.ui.lis)
                screate.mysocket.send(lis1)
                data = screate.mysocket.recv(4096)
            else:
                data = screate.mysocket.recv(4096)
                gcreate.ui.lis = pickle.loads(data)
                e1.set()
            e1.clear()

e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()

t1 = threading.Thread(target = screate)
t2 = threading.Thread(target = gcreate)
t3 = threading.Thread(target = ncreate)

t1.start()
t2.start()

e2.wait()
t3.start()
gcreate.ui.workerthread.start()