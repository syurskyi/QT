from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer

from menu_modul import Ui_MainMenu
from data_modul import JsonConnector, SoundThread


class UiSkinSkills(object):
    core = None

    def setupUi(self, MainWindow, what):
        MainWindow.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.centralwidget.setObjectName("centralwidget")

        self.make_background()
        self.make_header()
        self.make_return_btn()
        self.make_coin_label()

        self.make_scroll()

        if what == "skins":
            self.load_skins()
        else:
            self.load_skills()

        self.etimer = QTimer()

        MainWindow.setCentralWidget(self.centralwidget)

        if what == "skins":
            self.retranslateUi(MainWindow)
        else:
            self.skillsRetranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Welcome in shop"))
        self.returnBtn.setText(_translate("MainWindow", "Return"))

    def make_background(self):
        self.sbackground = QtWidgets.QLabel(self.centralwidget)
        self.sbackground.setScaledContents(True)
        self.sbackground.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.sbackground.setAutoFillBackground(True)
        self.sbackground.setText("")
        self.sbackground.setPixmap(QtGui.QPixmap("images/stars_background.gif"))
        self.sbackground.setObjectName("background")

    def make_header(self):
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 791, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

    def make_return_btn(self):
        self.returnBtn = QtWidgets.QPushButton(self.centralwidget)
        self.returnBtn.setGeometry(QtCore.QRect(550, 740, 121, 41))
        self.returnBtn.setObjectName("returnBtn")
        self.customize_btn(self.returnBtn)
        self.returnBtn.clicked.connect(self.return_btn_click)

    def return_btn_click(self):
        x = SoundThread("shotClick.wav")
        x.start()

        if self.etimer.isActive():
            self.etimer.stop()

        self.core.reload_main_menu()

    def customize_btn(self, btn_inst):
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        btn_inst.setFont(font)
        btn_inst.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        btn_inst.setMouseTracking(False)
        btn_inst.setFocusPolicy(QtCore.Qt.StrongFocus)
        btn_inst.setToolTip("")
        btn_inst.setAutoFillBackground(True)
        btn_inst.setCheckable(False)
        btn_inst.setAutoDefault(False)
        btn_inst.setDefault(False)
        btn_inst.setFlat(True)
        palette = Ui_MainMenu.get_btn_palette()
        btn_inst.setPalette(palette)

    def load_skins(self):
        self.image_list = []    # tworzy liste z instancjami elementów karty skina aby można było je resizować
        self.btn_list = []
        self.label_list = []

        self.load_card_elements()       # ładuje gotowe właściwości do elementów scrolla
        self.set_scrollbar_pos_to_start()       # ustala scroll na początek aby po ponownym załadowaniu jego pozycja była prawidłowa

        self.skin_list = JsonConnector.get_skin_list()
        for ind, elem in enumerate(self.skin_list):
            self.make_skin_card(elem, ind)

    def make_skin_card(self, skin_info, index_in_skin_list):
        sclabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sclabel.setGeometry(QtCore.QRect(200, 0, 100, 100))
        sclabel.setText(skin_info["name"])
        sclabel.setFont(self.clfont)
        sclabel.setPalette(self.clpalette)
        self.label_list.append(sclabel)

        scimage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        scimage.setText("")
        scimage.setScaledContents(True)
        scimage.setGeometry(QtCore.QRect(200, 200, 100, 100))
        scimage.setPixmap(QtGui.QPixmap("images/skins/" + skin_info["path"] + ".png"))   # images/skins/benek.png
        self.image_list.append(scimage)

        scbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        scbutton.setGeometry(QtCore.QRect(200, 400, 100, 100))
        if skin_info["available"]:
            if JsonConnector.get_from_config("skin") == skin_info["path"]:
                scbutton.setText("Selected")
            else:
                scbutton.setText("Select")
                scbutton.clicked.connect(lambda: self.select_skin(skin_info["path"]))
        else:
            scbutton.setText("Buy by " + str(skin_info["price"]) + " coins")
            scbutton.clicked.connect(lambda: self.buy_skin(index_in_skin_list, scbutton))

        self.customize_btn(scbutton)
        self.btn_list.append(scbutton)

    def load_card_elements(self):
        self.clfont = QtGui.QFont()
        self.clfont.setPointSize(36)

        self.clpalette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.clpalette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.clpalette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.clpalette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

    def select_skin(self, path):
        x = SoundThread("shotClick.wav")
        x.start()

        JsonConnector.save_key_to_config("skin", path)
        self.centralwidget.close()
        self.load_skins()
        self.core.window.resize_tlo()
        self.centralwidget.show()

    def buy_skin(self, skin_dict_index, btn_instance):
        coins = JsonConnector.get_from_config("coins")
        if coins >= self.skin_list[skin_dict_index]["price"]:
            self.skin_list[skin_dict_index]["available"] = True
            JsonConnector.save_skin_list(self.skin_list)

            coins -= self.skin_list[skin_dict_index]["price"]
            JsonConnector.save_key_to_config("coins", coins)
            self.make_coin_label()

            x = SoundThread("shotFanfar.wav")
            x.start()

            self.centralwidget.close()
            self.load_skins()
            self.core.window.resize_tlo()
            self.centralwidget.show()
        else:
            self.can_not_buy_anim(btn_instance)

    def can_not_buy_anim(self, btn_instance):
        x = SoundThread("shotError.wav")
        x.start()
        if btn_instance.text() != "Can't buy":
            old_txt = btn_instance.text()
            btn_instance.setText("Can't buy")
            self.etimer.timeout.connect(lambda: self.restore_btn_text(old_txt, btn_instance, self.etimer))
            self.etimer.start(1500)

    def restore_btn_text(self, txt, btn, timer):
        timer.stop()
        btn.setText(txt)

    def make_scroll(self):
        self.scroll = QtWidgets.QScrollArea(self.centralwidget)

        x = QtWidgets.QScrollBar()
        x.setStyleSheet("QScrollBar:horizontal {border: 2px solid gray;background: black;height: 15px;margin: 0px 40px 0 20px;}"
                        "QScrollBar::handle:horizontal {background: gainsboro;min-width: 20px;}"
                        "QScrollBar::add-line:horizontal {background: gray;width: 16px;subcontrol-position: left;subcontrol-origin: margin;border: 2px solid black;}"
                        "QScrollBar::sub-line:horizontal {background: gray;width: 16px;subcontrol-position: top right;subcontrol-origin: margin;border: 2px solid black;position: absolute;right: 20px;}"
                        "QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {width: 3px;height: 3px;background: white;}"
                        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {background: none;}")
        self.scroll.setHorizontalScrollBar(x)

        self.scroll.setGeometry(QtCore.QRect(0, 200, 1600, 800))
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setFrameShape(QtWidgets.QFrame.NoFrame)

        scroll_palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(13, 13, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        scroll_palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        scroll_palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        scroll_palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.scroll.setPalette(scroll_palette)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scroll.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2929, 738))

    def make_coin_label(self):
        self.coin_label = QtWidgets.QLabel(self.centralwidget)
        self.coin_label.setGeometry(QtCore.QRect(0, 0, 791, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.coin_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.coin_label.setFont(font)
        self.coin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.coin_label.setText("Coins: " + str(JsonConnector.get_from_config("coins")))

    def set_scrollbar_pos_to_start(self):
        sb = self.scroll.horizontalScrollBar()
        sb.setValue(sb.minimum())

    # skills

    def skillsRetranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Welcome in skills menu"))
        self.returnBtn.setText(_translate("MainWindow", "Return"))

    def load_skills(self):
        self.image_list = []  # tworzy liste z instancjami elementów karty skilla aby można było je resizować
        self.btn_list = []
        self.label_list = []

        self.load_card_elements()       # ładuje gotowe właściwości do elementów scrolla
        self.set_scrollbar_pos_to_start()       # ustala scroll na początek aby po ponownym załadowaniu jego pozycja była prawidłowa

        self.skill_list = JsonConnector.get_skills_dict()
        for ind, elem in enumerate(self.skill_list):
            self.make_skill_card(elem, ind)

    def make_skill_card(self, skill_info, index_in_skill_list):
        sclabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sclabel.setGeometry(QtCore.QRect(200, 0, 100, 100))
        sclabel.setText(skill_info["name"])
        sclabel.setFont(self.clfont)
        sclabel.setPalette(self.clpalette)
        self.label_list.append(sclabel)

        scimage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        scimage.setText("")
        scimage.setScaledContents(True)
        scimage.setGeometry(QtCore.QRect(200, 200, 100, 100))
        scimage.setPixmap(QtGui.QPixmap("images/skills/" + skill_info["imgPath"] + ".png"))  # images/benek.png
        self.image_list.append(scimage)

        scbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        scbutton.setGeometry(QtCore.QRect(200, 400, 100, 100))
        if skill_info["available"]:
            if skill_info["selected"]:
                scbutton.setText("Unselect")
                scbutton.clicked.connect(lambda: self.unselect_skill(index_in_skill_list))
            else:
                scbutton.setText("Select")
                scbutton.clicked.connect(lambda: self.select_skill(index_in_skill_list))
        else:
            scbutton.setText("Buy by " + str(skill_info["price"]) + " coins")
            scbutton.clicked.connect(lambda: self.buy_skill(index_in_skill_list, scbutton))

        self.customize_btn(scbutton)
        self.btn_list.append(scbutton)

    def select_skill(self, index_):
        x = SoundThread("shotClick.wav")
        x.start()

        self.skill_list[index_]["selected"] = True
        JsonConnector.save_skills_dict(self.skill_list)

        self.load_skill_to_config(self.skill_list[index_]["name"])

        self.centralwidget.close()
        self.load_skills()
        self.core.window.resize_tlo()
        self.centralwidget.show()

    def unselect_skill(self, index_):
        x = SoundThread("shotClick.wav")
        x.start()

        self.skill_list[index_]["selected"] = False
        JsonConnector.save_skills_dict(self.skill_list)

        self.load_skill_to_config(self.skill_list[index_]["name"], select=False)

        self.centralwidget.close()
        self.load_skills()
        self.core.window.resize_tlo()
        self.centralwidget.show()

    @staticmethod
    def load_skill_to_config(skill_name, select=True):
        if select:
            if skill_name == "BiggerAmmo":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["ammoSize"] = [40, 12]
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "FasterAmmo":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["ammoSpeed"] = 16
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "SmallerShip":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["shipSize"] = 20
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "MoreFireRate":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["fireSpeed"] = 600
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "LaserPenetrate":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["penetrate"] = True
                JsonConnector.save_key_to_config("shipConfig", conf)
        else:
            if skill_name == "BiggerAmmo":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["ammoSize"] = [80, 20]
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "FasterAmmo":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["ammoSpeed"] = 23
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "SmallerShip":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["shipSize"] = 15
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "MoreFireRate":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["fireSpeed"] = 900
                JsonConnector.save_key_to_config("shipConfig", conf)
            elif skill_name == "LaserPenetrate":
                conf = JsonConnector.get_from_config("shipConfig")
                conf["penetrate"] = False
                JsonConnector.save_key_to_config("shipConfig", conf)

    def buy_skill(self, skill_dict_index, btn_instance):
        coins = JsonConnector.get_from_config("coins")
        if coins >= self.skill_list[skill_dict_index]["price"]:
            self.skill_list[skill_dict_index]["available"] = True
            JsonConnector.save_skills_dict(self.skill_list)

            coins -= self.skill_list[skill_dict_index]["price"]
            JsonConnector.save_key_to_config("coins", coins)
            self.make_coin_label()

            x = SoundThread("shotFanfar.wav")
            x.start()

            self.centralwidget.close()
            self.load_skills()
            self.core.window.resize_tlo()
            self.centralwidget.show()
        else:
            self.can_not_buy_anim(btn_instance)
