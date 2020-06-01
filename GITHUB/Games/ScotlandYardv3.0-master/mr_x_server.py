import rules
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket,pickle
import threading
import gui

class Window(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.lis = rules.start()
        self.setupUi(self)

        self.workerthread = WorkerThread()
        self.workerthread.sig1.connect(self.play_move)
        self.workerthread.sig2.connect(self.find_move)
        self.pushButton.clicked.connect(self.but_pushed)
        self.pushButton_4.clicked.connect(self.but4_pushed)

    def but4_pushed(self):
        self.label.setEnabled(True)
        self.pixmapItem1 = self.scene.addPixmap(self.pix1)
        self.pixmapItem2 = self.scene.addPixmap(self.pix2)
        self.pixmapItem3 = self.scene.addPixmap(self.pix3)
        self.pixmapItem4 = self.scene.addPixmap(self.pix4)
        self.pixmapItem5 = self.scene.addPixmap(self.pix5)
        self.pixmapItem6 = self.scene.addPixmap(self.pix6)
        self.play_move()

        self.pushButton.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(False)
        self.comboBox.setEnabled(True)

        e1.set()

    def but_pushed(self):
        self.label.setText("Move is played")

    def play_move(self):
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
        e2.set()

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
    sig1 = QtCore.pyqtSignal()
    sig2 = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        for y in range(22):
            for x in range(6):
                if x == 0:
                    self.sig2.emit(x)
                e2.wait()
                self.sig1.emit()
                e2.clear()

def screate():
    host = "127.0.0.1"
    port = 8080
    serverSocket = socket.socket()
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind((host,port))
    serverSocket.listen(5)
    (screate.client,(ip,port)) = serverSocket.accept()

def gcreate():
    app = QtWidgets.QApplication(sys.argv)
    gcreate.ui = Window()

    gcreate.ui.pushButton.setEnabled(False)
    gcreate.ui.pushButton_3.setEnabled(False)
    gcreate.ui.comboBox.setEnabled(False)
    gcreate.ui.label.setText("Start the Game")
    gcreate.ui.label.setEnabled(False)
    
    gcreate.ui.show()  # The show() method displays the widget on the screen.
    sys.exit(app.exec_())  # Finally, we enter the mainloop of the application.

def ncreate():
    lis1 = pickle.dumps(gcreate.ui.lis)
    screate.client.send(lis1)
    for y in range(22):
        for x in range(6):
            if x > 0:
                data = screate.client.recv(4096)
                gcreate.ui.lis = pickle.loads(data)
                lis2 = pickle.dumps(gcreate.ui.lis)
                screate.client.send(lis2)
                e2.set()
            else:
                e2.wait()
                lis1 = pickle.dumps(gcreate.ui.lis)
                screate.client.send(lis1)
            e2.clear()

e1 = threading.Event()
e2 = threading.Event()

t1 = threading.Thread(target = screate)
t2 = threading.Thread(target = gcreate)
t3 = threading.Thread(target = ncreate)

t1.start()
t1.join()
t2.start()

e1.wait()
t3.start()
gcreate.ui.workerthread.start()