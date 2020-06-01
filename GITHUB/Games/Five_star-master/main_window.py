from PyQt5 import QtWidgets,QtCore, QtGui, Qt
import sys
import numpy as np
from map import Map, colors
from astar import AStar
from record_ui import record_Dialog
from changemapsize_dialog import Ui_ChangeMapSize


class Mywindow(QtWidgets.QMainWindow):

    GameEndSignal = QtCore.pyqtSignal(int)
    def __init__(self, map_size, main_app, gen_num=2, parent=None):
        super(Mywindow, self).__init__(parent)

        self.map_size = map_size
        self.selected_loc = None
        self.destine_loc = None
        self.just_start = True
        # the number of colored cells you generate each iteration
        self.gen_num = gen_num
        # deposit current grade
        self.grade = 0
        self.main_app = main_app
        [rows, cols] = map_size
        # self.resize(100+cols*50,100+cols*50)
        self.setMaximumSize(QtCore.QSize(100+cols*50,150+rows*50))
        self.setMinimumSize(QtCore.QSize(100+cols*50,150+rows*50))

        # initialize the label used to display the grade number
        self.grade_label = QtWidgets.QLabel()
        self.grade_label.setText('你的当前分数为: '+str(self.grade))
        self.grade_label.setObjectName('GradeLabel')
        self.grade_label.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(20)
        self.grade_label.setFont(font)
        self.grade_label.setMinimumSize(50*cols,50)
        self.grade_label.setMaximumSize(50*cols,50)

        # initialize the grid layout to deposit Mylabels
        self.gridlayoutWidget = QtWidgets.QWidget(self)
        self.gridlayoutWidget.setGeometry(QtCore.QRect(50,50,cols*50,rows*50))
        self.gridlayoutWidget.setObjectName("gridLayoutWidget")
        # self.setCentralWidget(self.gridlayoutWidget)
        self.gridLayout = QtWidgets.QGridLayout(self.gridlayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # setup the menubar widget
        self.setup_menubar()

        # combine the actions in menubar with different slot
        self.actionQuit.triggered['bool'].connect(self.exit_notice_slot)
        self.actionRecord.triggered['bool'].connect(self.record_notice)
        self.actionNew_game.triggered['bool'].connect(self.reset)
        self.actionEasy.triggered['bool'].connect(self.changetoeasy)
        self.actionCommon.triggered['bool'].connect(self.changetocommon)
        self.actionDifficult.triggered['bool'].connect(self.changetodifficult)
        self.actionChangemap.triggered['bool'].connect(self.mapsize_handler)

        # connect GameEndsignal to gameendhandler
        self.GameEndSignal.connect(self.game_end_handler)
        # the grade label takes an entire row to display
        self.gridLayout.addWidget(self.grade_label,0,0,1,cols)

        # initialize the map to all-cleared status
        # and add each map cell(Mylabel) into the gridcelllayout
        self.map = Map(self.map_size, main_app=main_app, parent=self)
        for row in range(rows):
            for col in range(cols):
                # connect the signals with slot functions
                self.map.data[row, col].selected_signal.connect(self.label_selected)
                self.map.data[row, col].pressed_but_nonselect_signal.connect(self.pressed_but_not_select)
                self.gridLayout.addWidget(self.map.data[row, col], row+1, col, 1, 1)

        # at last generate certain number of colored-cell
        self.map.rand_gen(self.gen_num)

    def changetoeasy(self):
        """
        change the game difficulty mode
        :return: None
        """
        self.gen_num = 2
        self.reset()

    def changetocommon(self):
        """
        change the game difficulty mode
        :return: None
        """
        self.gen_num = 3
        self.reset()

    def changetodifficult(self):
        """
        change the game difficulty mode
        :return: None
        """
        self.gen_num = 4
        self.reset()

    def mapsize_handler(self):
        class Mapsize_window(QtWidgets.QDialog, Ui_ChangeMapSize):
            def __init__(self, mainwin:Mywindow):
                super(Mapsize_window, self).__init__()
                self.mainwin = mainwin
                self.map_size_candidate = None
                self.setupUi(self)
                self.radioButton_12x12.toggled.connect(self.set_mapchangeinfo)
                self.radioButton_16x9.toggled.connect(self.set_mapchangeinfo)
                self.radioButton_15x15.toggled.connect(self.set_mapchangeinfo)
                self.radioButton_custom.toggled.connect(self.set_mapchangeinfo)
                self.buttonBox.accepted.connect(self.confirm_slot)
                self.buttonBox.rejected.connect(self.reject)
            def confirm_slot(self):
                if not self.lineEdit_2.isEnabled():
                    if self.map_size_candidate is None:
                        self.msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Information,'Something wrong'
                                                                                      ,'You haven\'t choose the size yet', QtWidgets.QMessageBox.Ok,)
                        self.setWindowModality(QtCore.Qt.ApplicationModal)
                        self.msg.show()
                    else:
                        self.mainwin.close()
                        self.mainwin = Mywindow(self.map_size_candidate, self.mainwin.main_app)
                        self.mainwin.show()
                        self.close()
                else:
                    width =  self.lineEdit.text()
                    hight = self.lineEdit_2.text()
                    if width =='' or hight == '':
                        self.msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning,'Something wrong'
                                                                                      ,'宽度或者高度未设定', QtWidgets.QMessageBox.Ok,)
                        self.setWindowModality(QtCore.Qt.ApplicationModal)
                        self.msg.show()
                    else:
                        self.mainwin.close()
                        self.mainwin = Mywindow([int(hight),  int(width)],main_app=self.mainwin.main_app)
                        self.mainwin.show()
                        self.close()
            def set_mapchangeinfo(self):
                button = self.sender()
                if button.isChecked():
                    buttonname = button.objectName()
                    if buttonname != 'radioButton_custom':
                        self.lineEdit.setEnabled(False)
                        self.lineEdit_2.setEnabled(False)
                        print(list(map(int, buttonname.split('_')[1].split('x'))))
                        self.map_size_candidate = list(map(int, buttonname.split('_')[1].split('x')))
                    else:
                        self.lineEdit.setEnabled(True)
                        self.lineEdit_2.setEnabled(True)

                    print('current selected map size is {}'.format(button.objectName()))
        self.mapchange_win = Mapsize_window(self)
        self.mapchange_win.setWindowModality(QtCore.Qt.ApplicationModal)
        self.mapchange_win.show()

    def setup_menubar(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuGame = QtWidgets.QMenu(self.menubar)
        self.menuGame.setObjectName("menuGame")
        self.menuChange_the_difficulty = QtWidgets.QMenu(self.menuGame)
        self.menuChange_the_difficulty.setObjectName("menuChange_the_difficulty")
        self.menuSystem = QtWidgets.QMenu(self.menubar)
        self.menuSystem.setObjectName("menuSystem")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew_game = QtWidgets.QAction(self)
        self.actionChangemap = QtWidgets.QAction(self)
        self.actionNew_game.setObjectName("actionNew_game")
        self.actionChangemap.setObjectName("actionChangemap")
        self.actionQuit = QtWidgets.QAction(self)
        self.actionQuit.setObjectName("actionQuit")
        self.actionRecord = QtWidgets.QAction(self)
        self.actionRecord.setObjectName("actionRecord")
        self.actionEasy = QtWidgets.QAction(self)
        self.actionEasy.setObjectName("actionEasy")
        self.actionCommon = QtWidgets.QAction(self)
        self.actionCommon.setObjectName("actionCommon")
        self.actionDifficult = QtWidgets.QAction(self)
        self.actionDifficult.setObjectName("actionDifficult")
        self.menuChange_the_difficulty.addAction(self.actionEasy)
        self.menuChange_the_difficulty.addAction(self.actionCommon)
        self.menuChange_the_difficulty.addAction(self.actionDifficult)
        self.menuGame.addAction(self.actionNew_game)
        self.menuGame.addAction(self.actionChangemap)
        self.menuGame.addAction(self.menuChange_the_difficulty.menuAction())
        self.menuSystem.addAction(self.actionRecord)
        self.menuSystem.addAction(self.actionQuit)
        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuSystem.menuAction())

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuGame.setTitle(_translate("MainWindow", "游戏"))
        self.menuChange_the_difficulty.setTitle(_translate("MainWindow", "选择游戏难度"))
        self.menuSystem.setTitle(_translate("MainWindow", "系统"))
        self.actionNew_game.setText(_translate("MainWindow", "新游戏"))
        self.actionChangemap.setText(_translate("MainWindow", "更改地图大小"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionRecord.setText(_translate("MainWindow", "查看最佳纪录"))
        self.actionEasy.setText(_translate("MainWindow", "简单"))
        self.actionCommon.setText(_translate("MainWindow", "一般"))
        self.actionDifficult.setText(_translate("MainWindow", "困难"))

    def reset(self):
        self.selected_loc = None
        self.destine_loc = None
        self.just_start = True
        self.grade = 0
        self.grade_label.setText('你的当前分数是: ' + str(self.grade))
        self.map.clear_all()
        self.map.rand_gen(self.gen_num)


    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        print('mainwindow pressed')

    def pressed_but_not_select(self,x,y):
        """
        Slot function to receive the pressed_but_nonselect signal
        if a Mylabel cinstance is clicked and also it's blank then
        get into this function
        This function implement these things:
        1.Before clicking this cell, if you have already clicked(selected) a
        colored cell, then this function detect whether there is a valid
        path from the selected loc (self.selected_loc) to this loc(x,y).
        If success then move the colored cell to this loc and then set the
        previous selected_loc to blank(valid), else only set the previous
        selected_loc to valid(only view this action as canceling the seleted cell)
        2. If there is no cell seleted before do nothing
        :param x:  Mylabel x coordinate
        :param y:  Mylabel y coordinate
        :return:
        """
        print('received pressed_but_not_select signal')
        if self.selected_loc is not None:
            astar = AStar()
            converted_map = self.map.get_valid_map()*10
            converted_map = converted_map.astype(np.float)
            is_success = astar.main(converted_map, start_loc=self.selected_loc, end_loc=np.array([x,y]))
            if is_success:
                astar.path_backtrace()
                path = astar.best_path_array
                path = path[:, ::-1]
                self.just_start = False
                self.map.flash_starttoend(path)
                self.grade += self.map.judge_five([x, y])
                # self.cancel_selected()
                self.selected_loc = None
                self.grade += self.map.rand_gen(self.gen_num)
                if self.map.get_valid_num() == 0:
                    self.grade_label.setText('你的分数是: ' + str(self.grade)+' 游戏结束')
                    self.GameEndSignal.emit(self.grade)
                else:
                    self.grade_label.setText('你的当前分数是: ' + str(self.grade))
            else:
                self.cancel_selected()
                # self.map.rand_gen(4)
    
    def label_selected(self, x, y):
        """
        Slot method to receive the slected_signal and mark the selected cell
        :param x:  Mylabel x coordinate
        :param y:  Mylabel y coordinate
        :return:
        """
        print('received selected_signal')
        print('previous selected loc is', self.selected_loc)
        if self.selected_loc is not None:
            # if it's not the first time you select a cell then
            # cancel the selection
            self.cancel_selected()
        print('set current selected loc to', x, y)
        self.selected_loc = np.array([x, y])
        self.mark_selected()

    def cancel_selected(self):
        # print('entering the cancel_selected method')
        current_color = colors[self.map.get_loc_color(self.selected_loc)]

        self.map.set_loc_color(self.selected_loc, current_color)
        self.map.data[self.selected_loc[0], self.selected_loc[1]].label_pressed = False
        self.selected_loc = None

    def mark_selected(self):
        # print(self.map.data[self.selected_loc[0],self.selected_loc[1]].color)
        current_color = colors[self.map.get_loc_color(self.selected_loc)]
        print('current color is ', current_color)
        modified_color = current_color.copy()
        # brighter the current selected cell: add 75 to each channel(RGB)
        for i in range(3):
            modified_color[i] +=75
            modified_color[i] = min(modified_color[i], 255)
        # print(modified_color)
        qcolor = QtGui.QColor(*(modified_color))
        self.map.set_loc_color(self.selected_loc, qcolor)

    def exit_notice_slot(self):
        self.close()

    def record_notice(self):
        record = []
        with open('record.txt', 'r') as f:
            for i in range(3):
                line = f.readline()
                record.append(int(line))
            f.close()
        class  Record_window(QtWidgets.QDialog, record_Dialog):

            def __init__(self, parent=None):
                super(Record_window, self).__init__()
                self.setupUi(self)

        self.record_win = Record_window()
        self.record_win.FirstgradeLabel.setText(str(record[0]))
        self.record_win.SecondgradeLabel.setText(str(record[1]))
        self.record_win.ThirdgradeLabel.setText(str(record[2]))
        self.record_win.ConfirmButton.clicked.connect(self.record_win.close)
        self.record_win.show()

    def set_label_format(self, label:QtWidgets.QLabel, text, size, color=(0,0,0)):
        label.setText(text)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setMinimumSize(size[0], size[1])
        label.setMaximumSize(size[0], size[1])
        label.setFrameShape(QtWidgets.QFrame.Box)
        label.setStyleSheet("border-width: 1px;border-style: solid;border-color: rgb({}, {}, {});".format(color[0], color[1], color[2]))

    def game_end_handler(self, current_grade: int):
        record = []
        file = open('record.txt','r')
        for i in range(3):
            line = file.readline()
            if current_grade > int(line):
                record.append(current_grade)
                if i <2:
                    record.append(int(line))
                    for k in range(i+1,3):
                        line = file.readline()
                        record.append(int(line))
                break
            record.append(int(line))
        file.close()

        file = open('record.txt','w')
        file.write(str(record[0]) + '\n')
        file.write(str(record[1]) + '\n')
        file.write(str(record[2]) )

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText("游戏结束")
        msg.setInformativeText("您的当前分数为：{}".format(current_grade))
        msg.setWindowTitle("游戏结束")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if not self.just_start:
            reply = QtWidgets.QMessageBox.question(self,
                                                   '本程序',
                                                   "是否要退出程序？\n未完成的游戏成绩将不会记录",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mywin = Mywindow((12,12),app)
    mywin.show()
    sys.exit(app.exec_())
