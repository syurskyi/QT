from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWebSockets, QtNetwork
from PyQt5.uic import loadUiType
from PyQt5.QtMultimedia import *
import threading
import os
import sys
import time

scriptDir = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptDir)
FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__), "main.ui"))


class Json:
    def __init__(self):
        self.json = None

    def set_json(self, json):
        self.json = json

    def get(self, key):
        if self.json is None:
            return None
        if key in self.json:
            return self.json[key]
        return None

class Main(QMainWindow, FROM_MAIN):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.logo_bit = QPixmap("image/logo.jpg")
        pixmap = self.logo_bit.scaled(448, 630)
        self.image_view.setPixmap(pixmap)
        self.musiclist = QMediaPlaylist()
        url = QUrl.fromLocalFile("music/starter.mp3")
        self.musiclist.addMedia(QMediaContent(url))
        self.musiclist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.musiclist)
        self.player.play()
        self.client = QtWebSockets.QWebSocket("",QtWebSockets.QWebSocketProtocol.Version13,None)
        self.client.error.connect(self.on_error)
        self.client.open(QUrl("ws://127.0.0.1:80"))
        self.client.connected.connect(self.on_connected)
        self.client.disconnected.connect(self.on_disconnected)
        self.client.textMessageReceived.connect(self.on_messages)
        self.button_left.clicked.connect(self.on_some_button_clicked)
        self.button_right.clicked.connect(self.on_some_button_clicked)
        self.default()

    def default(self):
        self.message.hide()
        self.button_right.hide()
        self.button_left.hide()
        self.progressBar.setValue(50)
    def on_connected(self):
        self.progressBar.setValue(100)
        self.hide_progress()
        self.client.sendTextMessage(str({"get": "Hello server"}))

    def on_messages(self, msg):
        try:
            packet = eval(msg)
        except: return
        print(packet)
        json = Json()
        json.set_json(packet)
        t = json.get("type")
        if t is not None and t == "success":
            print("Game is end no question!")
        else:
            q = json.get("Q")
            BL = json.get("BL")
            BR = json.get("BR")
            BL_MSG = BL[0]
            BL_ALLOW = BL[1]
            BR_MSG = BR[0]
            BR_ALLOW = BR[1]
            
            if BL[1] == True:
                self.button_left.show()
            self.message.show()
            self.message.setText(q)
            if BL_ALLOW:
                self.button_left.show()
                self.button_left.setText(BL_MSG)
            else:
                self.button_left.hide()
            if BR_ALLOW:
                self.button_right.show()
                self.button_right.setText(BR_MSG)
            else:
                self.button_right.hide()

    def on_disconnected(self):
        print("disconnected!!!")
        self.default()

    def on_error(self, e):
        self.default()

    def hide_progress(self):
        self.progressBar.hide()
        
    def on_some_button_clicked(self):
        self.client.sendTextMessage(str({"space": "clicked"}))
    
def main():
    app=QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
