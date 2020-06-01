from PyQt5.QtWidgets import (QWidget, QCheckBox, QPushButton, QSlider)
from PyQt5.QtCore import Qt
import time
import threading


class Game(QWidget):

    def __init__(self, w, h, cells):
        self.slider = None
        # init vars
        self.running = True
        self.loop = True
        self.timer = 0.5
        self.w = w
        self.h = h
        self.boxes = [[None for j in range(self.w)] for i in range(self.h)]
        self.cells = cells
        # init ui
        super().__init__()
        self.init_ui()
        # start polling with new thread
        self.t = threading.Thread(target=self.get_next)
        self.t.start()

    def closeEvent(self, event):
        self.running = False
        event.accept()

    def get_next(self):
        while self.running:
            if self.loop:
                # load new cells and redraw
                cells_new = self.cells.get_next()
                self.redraw(cells_new)
            time.sleep(self.timer)

    def checkbox_clicked(self):
        sender = self.sender()
        # get x,y values of button and send to Cells
        tip = sender.toolTip()
        x, y = tip.split(':')
        self.cells.set_cell(int(x), int(y))

    def button_clicked(self):
        self.loop = not self.loop

    def slider_changed(self):
        self.timer = self.slider.value() / 10

    def init_bottom_panel(self, margin, bottom_lane_h):
        # create button to start/ stop
        button_ss = QPushButton("Start/ Stop", self)
        button_ss_w = margin*10
        button_ss.resize(button_ss_w, bottom_lane_h)
        button_ss.move(0, self.h * margin)
        button_ss.pressed.connect(self.button_clicked)
        # create refresh button
        button_rf = QPushButton("Refresh", self)
        button_rf_w = margin*3
        button_rf.resize(margin*3, bottom_lane_h)
        button_rf.move(margin * self.w - margin*3, self.h * margin)
        # create speed slider
        slider = QSlider(Qt.Horizontal, self)
        slider.move(button_ss_w, self.h * margin)
        slider.resize(self.w * margin - button_ss_w - button_rf_w, bottom_lane_h)
        # set parameter for slider
        slider.setMinimum(1)
        slider.setMaximum(30)
        slider.setValue(self.timer*10)
        slider.setTickPosition(QSlider.TicksAbove)
        slider.setTickInterval(1)
        slider.valueChanged.connect(self.slider_changed)
        self.slider = slider

    def init_ui(self):
        margin = 20
        # create checkboxes to simulate cells
        for x in range(self.w):
            for y in range(self.h):
                check_box = QCheckBox('', self)
                check_box.setToolTip(str(x) + ":" + str(y))
                check_box.move(x * margin, y * margin)
                check_box.resize(margin, margin)
                check_box.setStyleSheet("QCheckBox::indicator:unchecked {image: url(./images/unchecked.bmp);}"
                                        "QCheckBox::indicator:checked {image: url(./images/checked.bmp);}"
                                        "QCheckBox::indicator:checked:hover {image: url(./images/pressed.bmp);}"
                                        )
                check_box.pressed.connect(self.checkbox_clicked)
                # noinspection PyTypeChecker
                self.boxes[x][y] = check_box
        bottom_panel_h = margin*2
        self.init_bottom_panel(margin, bottom_panel_h)
        # set window
        self.setGeometry(0, 0, margin * self.w, margin * self.h + bottom_panel_h)
        self.setWindowTitle('Game of Life')
        self.show()

    def redraw(self, cells):
        # redraw buttons
        for x in range(self.w):
            for y in range(self.h):
                if cells[x][y]:
                    self.boxes[x][y].setChecked(True)
                else:
                    self.boxes[x][y].setChecked(False)
