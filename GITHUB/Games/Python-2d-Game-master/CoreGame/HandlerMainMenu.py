import sys
from importlib import reload

from PyQt5 import QtWidgets, QtCore

from CoreGame.Menus.HandlerCoins import CoinsGui
from CoreGame.Menus.MainMenu import Ui_Dialog
from CoreGame import Settings
from CoreGame.Menus.HandlerStore import StoreGui
from CoreGame.Menus.Controller.HandlerMenuNivel import NivelGui
from CoreGame.Menus.service.ServNav import ServNav
from CoreGame.Menus.service.ServPowerUp import ServPowerUp


class MyFirstGuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setupUi(dialog)
        self.menunivel = 0
        self.dialog = dialog
        self.uiframe = NivelGui(QtWidgets.QFrame(self.widget),self.menunivel,self.nivelescolhido)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))

        Settings.NAVUNLOCKED.clear()
        Settings.LEVELUNLOCKED.clear()

        ref_arquivo = open("variaveis.txt", "r")

        #ref_arquivo.write(Settings.NAVUNLOCKED.__str__())

        lines = ref_arquivo.readlines()

        ref_arquivo.close()

        navs = str(lines[0]).replace("\n",'')
        Settings.COINS = int(lines[1])
        levels = str(lines[2]).replace("\n",'')
        pw1 = str(lines[3]).replace("\n",'').split(":")


        for n in navs:
            Settings.NAVUNLOCKED.append(int(n))

        for l in levels:
            Settings.LEVELUNLOCKED.append(int(l))


        for j in range(3):
            for k in pw1[j]:
                Settings.POWERUPUNLOCKED[j].append(int(k))




        self.menu = 0
        self.x = False
        self.game = 0
        self.navs = ServNav()
        self.pwups = ServPowerUp()

        self.style = """

                QPushButton{
                    background-image:url('store.png');
                    background-repeat:no-repeat;
                    margin: 1px;
                    border-style: outset;
                    text-align:bottom;
                     padding-bottom:7px;
                    background-position: center;
                    background-color:white;
                    color:white;
                }
                QPushButton:hover{
                    background-color:#f2f2f2;
                    color:#2b5259;
                    
                }
                

                """
        self.stylels = """

                QLabel{
                    background-image:url('lastscore.png');
                    background-repeat:no-repeat;
                    background-position: center;
                    background-color:white;
                color:white;
                }
                QLabel:hover{
                    background-color:#f2f2f2;
                    color:black;
                }

                """
        self.stylebs = """

                QLabel{
                    background-image:url('bigscore.png');
                    background-repeat:no-repeat;
                    background-position: center;
                    background-color:white;
                color:white;
                }
                QLabel:hover{
                    background-color:#f2f2f2;
                    color:black;

                }

                """
        self.styleexit = """

                QPushButton{
                    background-image:url('exit.png');
                    background-repeat:no-repeat;
                    margin: 1px;
                    border-style: outset;
                    text-align:bottom;
                    background-position: center;
                    background-color:white;
                color:white;
                }
                QPushButton:hover{
                    background-color:#f2f2f2;
                    color:#2b5259;

                }

                """

        self.stylefreecoins = """

            QPushButton{
                background-image:url('movie.png');
                background-repeat:no-repeat;
                margin: 1px;
                border-style: outset;
                text-align:bottom;
                padding-bottom:7px;
                background-position: center;
                background-color:white;
                color:white;
            }
            QPushButton:hover{
                background-color:#f2f2f2;
                color:#2b5259;

            }


            """

        #self.widget.setStyleSheet(self.style);
        # 0d111c
        self.frame.setVisible(True)
        self.label_3.setText(str(Settings.COINS))
        self.i = 0

        self.nav_baixo.setStyleSheet("QPushButton{background-image:url(" + Settings.navlistMINI[Settings.NAVESCOLHIDA] + ");color:#2b5259;background-color:transparent;padding-top:110px;background-position: center; background-repeat:no-repeat;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

        self.barra.setStyleSheet("QWidget{background-color:white;}")

        if self.menu == 0:
            self.bt_nav.setText("Niveis")
            self.bt_powerup.setText("Modo Livre")

            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('modelevel.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('modearcade.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

        elif self.menu == 1:
            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('navicon.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('powerupicon.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")


        self.bt_play.setStyleSheet("QPushButton{background-image:url('play.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
        self.bt_back.setStyleSheet("QPushButton{background-image:url('anterior.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
        self.label_3.setStyleSheet("QLabel{background-image:url('coins.png');background-repeat:no-repeat;margin: 1px; border-style: outset;text-align:bottom;padding-top:40px;background-position: center;background-color:white;color:#2b5259;}")


        #self.bt_right_2.setStyleSheet(self.styleright)
        #self.bt_left_2.setStyleSheet(self.styleleft)
        self.widget.setStyleSheet("background-color:#f2f2f2")
        self.ls_icon.setStyleSheet(self.stylels)
        self.bs_icon.setStyleSheet(self.stylebs)
        self.ls_freecoins.setStyleSheet(self.stylefreecoins)
        #self.label_9.setStyleSheet("")
        self.bt_store.setStyleSheet(self.style)
        self.label.setStyleSheet("background-image:url('logo.png');background-repeat:no-repeat;background-position: left;background-color:white;color:#2b5259;")
        self.lb_exit.setStyleSheet(self.styleexit)
        #self.label_4.setStyleSheet("QLabel{background-image:url('storebig.png');color:#2b5259;background-color:transparent;background-position: left;background-repeat:no-repeat;margin: 1px;border-style: outset;}")

        self.bt_play.clicked.connect(self.play)

        #self.bt_unlock.clicked.connect(self.unlock)
        self.bt_store.clicked.connect(self.store)
        self.bt_powerup.clicked.connect(self.handlebtpw)
        self.bt_nav.clicked.connect(self.handlebtnav)
        self.bt_back.clicked.connect(self.handlerbtanterior)
        self.ls_freecoins.clicked.connect(self.handlerbtcoins)
        self.lb_exit.clicked.connect(self.handlerexit)

    def handlerexit(self):

        ref_arquivo = open("variaveis.txt", "w")

        ref_arquivo.write(str(Settings.NAVUNLOCKED.__str__().replace("[","").replace("]","").replace(",","").replace(" ","")))
        ref_arquivo.write("\n")
        ref_arquivo.write(str(Settings.COINS))
        ref_arquivo.write("\n")
        ref_arquivo.write(Settings.LEVELUNLOCKED.__str__().replace("[","").replace("]","").replace(",","").replace(" ",""))
        ref_arquivo.write("\n")
        ref_arquivo.write(Settings.POWERUPUNLOCKED.__str__().replace("[","").replace("]","").replace(",",":").replace(" ",""))




        ref_arquivo.close()

        exit(0)


    def handlerbtcoins(self):
        self.uiframe = CoinsGui(QtWidgets.QFrame(self.widget),self.label_3)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
        self.label_3.setText(str(Settings.COINS))
        self.frame.show()
        self.bt_powerup.setVisible(False)
        self.bt_nav.setVisible(False)
        self.bt_play.setVisible(False)
        self.nav_baixo.setVisible(False)
        self.nivelescolhido.setVisible(False)


    def handlebtnav(self):
        if self.menu == 1:
            Settings.NAVSELECTED = 0
            self.uiframe = StoreGui(QtWidgets.QFrame(self.widget), 0,self.navs,self.pwups,self.nav_baixo,self.label_3)
            self.frame = self.uiframe.getframe()
            self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
            self.label_3.setText(str(Settings.COINS))
            self.frame.show()
        elif self.menu == 0:
            self.menunivel = 0
            self.uiframe = NivelGui(QtWidgets.QFrame(self.widget), 0,self.nivelescolhido)
            self.frame = self.uiframe.getframe()
            self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
            self.label_3.setText(str(Settings.COINS))
            self.frame.show()

    def handlebtpw(self):
        if self.menu == 1:
            for i in Settings.NAVUNLOCKED:
                if i == Settings.NAVSELECTED:
                    self.uiframe = StoreGui(QtWidgets.QFrame(self.widget), 1,self.navs,self.pwups,self.nav_baixo,self.label_3)
                    self.frame = self.uiframe.getframe()
                    self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
                    self.label_3.setText(str(Settings.COINS))
                    self.frame.show()


        elif self.menu == 0:
            self.menunivel = 1
            self.uiframe = NivelGui(QtWidgets.QFrame(self.widget), 1,self.nivelescolhido)
            self.frame = self.uiframe.getframe()
            self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
            self.label_3.setText(str(Settings.COINS))
            self.frame.show()


    def store(self):
        self.uiframe = StoreGui(QtWidgets.QFrame(self.widget),0,self.navs,self.pwups,self.nav_baixo,self.label_3)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
        self.label_3.setText(str(Settings.COINS))
        self.frame.show()
        self.style = """QPushButton{background-image:url('store.png');background-repeat:no-repeat;margin: 1px;border-style: outset;text-align:bottom;background-position: center;background-color:#f2f2f2;color:#2b5259;
            }
            
            """
        self.bt_store.setStyleSheet(self.style)
        self.menu = 1
        self.mudarmenu()
        self.bt_powerup.setVisible(True)
        self.bt_nav.setVisible(True)
        self.bt_play.setVisible(True)
        self.nav_baixo.setVisible(True)
        self.nivelescolhido.setVisible(True)

    def play(self):
        print(Settings.NAVIMG)
        check = False
        for u in Settings.NAVUNLOCKED:
            if u == Settings.NAVSELECTED:
                check = True
        if check:
            Settings.currentlevel = Settings.BOSSESCOLHIDO
            Settings.NAVIMG = Settings.navlist[Settings.NAVESCOLHIDA]
            Settings.velocidade = (self.navs.getnavs()[Settings.NAVESCOLHIDA].getvelocidade()/10)
            Settings.disparo = (self.navs.getnavs()[Settings.NAVESCOLHIDA].getdisparo() / 10)
            Settings.vidas = (self.navs.getnavs()[Settings.NAVESCOLHIDA].getvida() / 100)


            print(str(Settings.NAVIMG))


            self.dialog.setEnabled(False)
            if not self.x:
                from CoreGame import game
                self.x = True
                self.game = game

            elif self.x:
                reload(self.game)


            if Settings.currentlevel == 4:
                Settings.currentlevel = 6
                reload(game)

            print("e ntri")
            self.dialog.setEnabled(True)



    def mudarmenu(self):
        if self.menu == 0:
            self.bt_nav.setText("Niveis")
            self.bt_powerup.setText("Modo Livre")

            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('modelevel.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('modearcade.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")

        elif self.menu == 1:
            self.bt_nav.setText("Navs")
            self.bt_powerup.setText("PowerUps")
            self.bt_nav.setStyleSheet(
                "QPushButton{background-image:url('navicon.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")
            self.bt_powerup.setStyleSheet(
                "QPushButton{background-image:url('powerupicon.png');color:#2b5259;padding-top:80px;background-repeat:no-repeat;background-color:transparent;background-position: center;margin: 1px;border-style: outset;}QPushButton:hover{background-color:white;color:#2b5259;};")


    def reloadstyle(self):
        self.style = """QPushButton{background-image:url('store.png'); background-repeat:no-repeat;margin: 1px;
                border-style: outset;
                text-align:bottom;
                background-position: center;
                background-color:white;
                color:white;
            }
            QPushButton:hover{
                background-color:#f2f2f2;
                color:#2b5259;

            }


            """
        self.bt_store.setStyleSheet(self.style)

    def handlerbtanterior(self):
        self.reloadstyle()
        self.uiframe = NivelGui(QtWidgets.QFrame(self.widget),self.menunivel,self.nivelescolhido)
        self.frame = self.uiframe.getframe()
        self.frame.setGeometry(QtCore.QRect(0, 70, 1131, 651))
        self.label_3.setText(str(Settings.COINS))
        self.frame.show()
        self.menu = 0
        self.mudarmenu()
        self.bt_powerup.setVisible(True)
        self.bt_nav.setVisible(True)
        self.bt_play.setVisible(True)
        self.nav_baixo.setVisible(True)
        self.nivelescolhido.setVisible(True)

    def getlbnav(self):
        return self.nav_baixo

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = MyFirstGuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())