
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setWindowTitle("Bomberman")
        self.MainWindow.resize(814, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 781, 521)) # TUUUU 0 0
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(910, 0, 81, 31))
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.pushButton_Start.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_End = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_End.setGeometry(QtCore.QRect(910, 35, 81, 31))
        self.pushButton_End.setObjectName("pushButton_End")
        self.pushButton_End.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(910, 70, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 550, 781, 21))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setObjectName("lineEdit")
        self.MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "Bomberman"))
        self.pushButton_Start.setText(_translate("MainWindow", "Start"))
        self.pushButton_End.setText(_translate("MainWindow", "Reset"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))

    def update_Ui(self,height,width,side=45):
        self.shape=height,width
        self.side=side
        button_width=self.side*2.5
        button_height=self.side
        lineEdit_height=21
        self.MainWindow.resize(self.shape[1]*self.side+button_width,self.shape[0]*self.side+lineEdit_height)
        self.centralwidget.resize(self.shape[1]*self.side+button_width,self.shape[0]*self.side+lineEdit_height)
        self.graphicsView.resize(self.shape[1]*self.side+button_width,self.shape[0]*self.side)
        self.pushButton_Start.setGeometry(QtCore.QRect(self.shape[1]*self.side, 0, button_width, button_height))
        self.pushButton_End.setGeometry(QtCore.QRect(self.shape[1]*self.side, button_height, button_width, button_height))
        self.pushButton_3.setGeometry(QtCore.QRect(self.shape[1]*self.side, button_height*2, button_width, button_height))
        self.lineEdit.setGeometry(QtCore.QRect(0, self.shape[0]*self.side, self.shape[1]*self.side, lineEdit_height))

        # QGraphicsScene
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(QtCore.QRectF(+self.side-self.side/4, 0, self.shape[1]*self.side,self.shape[0]*self.side-self.side))
        self.graphicsView.setScene(self.scene)

        self.read_images()

    def read_images(self):
        self.img_default_rect=QtGui.QPixmap('images/default_rect.png')
        self.img_blue_rect = QtGui.QPixmap('images/blue_rect.png')
        self.img_orange_rect = QtGui.QPixmap('images/orange_rect.png')
        self.img_explosion_rect = QtGui.QPixmap('images/explonsion_rect.png')
        self.img_ticking_bomb_rect = QtGui.QPixmap('images/bomb_rect.png')
        self.img_player_red= QtGui.QPixmap('images/bomberman_red_front.png')
        self.img_player_green= QtGui.QPixmap('images/bomberman_green_front.png')
