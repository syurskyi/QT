import sys
import os
import random
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt, QTimer
from pygame import mixer
from mutagen.mp3 import MP3
import style

music_list = []
mixer.init()
muted = False
count = 0
song_length = 0
index = 0


class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Music Player')
        self.setGeometry(450, 150, 480, 700)
        self.ui()
        self.show()

    def ui(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # ###################################Progress Bar#######################################################
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet(style.progress_bar_style())

        # #######################Labels###################
        self.song_timer_label = QLabel("0:00")
        self.song_lenth_label = QLabel("/ 0:00")

        # ###################################Buttons#######################################################
        self.add_button = QToolButton()
        self.add_button.setIcon(QIcon("icons/add.png"))
        self.add_button.setIconSize(QSize(48, 48))
        self.add_button.setToolTip("Add a Song")
        self.add_button.clicked.connect(self.add_sound)

        self.shuffle_button = QToolButton()
        self.shuffle_button.setIcon(QIcon("icons/shuffle.png"))
        self.shuffle_button.setIconSize(QSize(48, 48))
        self.shuffle_button.setToolTip("Shuffle The list")
        self.shuffle_button.clicked.connect(self.shuffle_play_list)

        self.previous_button = QToolButton()
        self.previous_button.setIcon(QIcon("icons/previous.png"))
        self.previous_button.setIconSize(QSize(48, 48))
        self.previous_button.setToolTip("Play Previous")
        self.previous_button.clicked.connect(self.play_previous)

        self.play_button = QToolButton()
        self.play_button.setIcon(QIcon("icons/play.png"))
        self.play_button.setIconSize(QSize(64, 64))
        self.play_button.setToolTip("Play")
        self.play_button.clicked.connect(self.play_sounds)

        self.next_button = QToolButton()
        self.next_button.setIcon(QIcon("icons/next.png"))
        self.next_button.setIconSize(QSize(48, 48))
        self.next_button.setToolTip("Play Next")
        self.next_button.clicked.connect(self.play_next)

        self.mute_button = QToolButton()
        self.mute_button.setIcon(QIcon("icons/mute.png"))
        self.mute_button.setIconSize(QSize(24, 24))
        self.mute_button.setToolTip("Mute")
        self.mute_button.clicked.connect(self.mute_sound)

        # ####################Volume Slider#################
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setToolTip("Volume")
        self.volume_slider.setValue(70)
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        mixer.music.set_volume(0.7)
        self.volume_slider.valueChanged.connect(self.set_volume)

        # ##################Play List####################
        self.play_list = QListWidget()
        self.play_list.doubleClicked.connect(self.play_sounds)
        self.play_list.setStyleSheet(style.play_list_style())

        # ##################Timer########################
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_progress_bar)

    def layouts(self):
        # ###################################Creating Layouts#######################################################
        self.main_layout = QVBoxLayout()
        self.top_main_layout = QVBoxLayout()
        self.top_groupbox = QGroupBox('Music Player')
        self.top_groupbox.setStyleSheet(style.groupbox_style())
        self.top_layout = QHBoxLayout()
        self.middle_layout = QHBoxLayout()
        self.bottom_layout = QVBoxLayout()

        # ###################################Adding Widgets#######################################################
        # ###################################Top Layouts Widgets##################################################
        self.top_layout.addWidget(self.progress_bar)
        self.top_layout.addWidget(self.song_timer_label)
        self.top_layout.addWidget(self.song_lenth_label)

        # #################Middle layout Widget#################
        self.middle_layout.addStretch()
        self.middle_layout.addWidget(self.add_button)
        self.middle_layout.addWidget(self.shuffle_button)
        self.middle_layout.addWidget(self.play_button)
        self.middle_layout.addWidget(self.previous_button)
        self.middle_layout.addWidget(self.next_button)
        self.middle_layout.addWidget(self.volume_slider)
        self.middle_layout.addWidget(self.mute_button)
        self.middle_layout.addStretch()

        # ##################Bottom layout widget#############
        self.bottom_layout.addWidget(self.play_list)

        self.top_main_layout.addLayout(self.top_layout)
        self.top_main_layout.addLayout(self.middle_layout)
        self.top_groupbox.setLayout(self.top_main_layout)
        self.main_layout.addWidget(self.top_groupbox, 25)
        self.main_layout.addLayout(self.bottom_layout, 75)
        self.setLayout(self.main_layout)

    def add_sound(self):
        directory = QFileDialog.getOpenFileName(self, "Add Sound", "", "Sound Files (*.mp3 *.ogg *.wav)")
        print(directory)
        filename = os.path.basename(directory[0])
        print(filename)
        self.play_list.addItem(filename)
        music_list.append(directory[0])

    def shuffle_play_list(self):
        random.shuffle(music_list)
        print(music_list)
        self.play_list.clear()
        for song in music_list:
            filename = os.path.basename(song)
            self.play_list.addItem(filename)

    def play_sounds(self):
        global song_length
        global count
        global index
        count = 0
        index = self.play_list.currentRow()
        print(index)
        print(music_list[index])

        try:
            mixer.music.load(str(music_list[index]))
            mixer.music.play()
            self.timer.start()
            sound = MP3(str(music_list[index]))
            song_length = sound.info.length
            song_length = round(song_length)
            print(song_length)
            min, sec = divmod(song_length, 60)

            self.song_lenth_label.setText("/ "+str(min)+":"+str(sec))
            self.progress_bar.setValue(0)
            self.progress_bar.setMaximum(song_length)

        except:
            pass

    def play_previous(self):
        global song_length
        global count
        global index
        count = 0
        items = self.play_list.count()
        print(index, 'first value')
        index -= 1
        print(index, 'second value')

        if index == 0:
            index = items
        index -= 1

        try:
            mixer.music.load(str(music_list[index]))
            mixer.music.play()
            self.timer.start()
            sound = MP3(str(music_list[index]))
            song_length = sound.info.length
            song_length = round(song_length)
            print(song_length)
            min, sec = divmod(song_length, 60)

            self.song_lenth_label.setText("/ " + str(min) + ":" + str(sec))
            self.progressBar.setValue(0)
            self.progressBar.setMaximum(song_length)

        except:
            pass

    def play_next(self):
        global song_length
        global count
        global index
        count = 0
        items = self.play_list.count()
        index += 1

        if index == items:
            index = 0

        try:
            mixer.music.load(str(music_list[index]))
            mixer.music.play()
            self.timer.start()
            sound = MP3(str(music_list[index]))
            song_length = sound.info.length
            song_length = round(song_length)
            print(song_length)
            min, sec = divmod(song_length, 60)

            self.song_lenth_label.setText("/ " + str(min) + ":" + str(sec))
            self.progressBar.setValue(0)
            self.progressBar.setMaximum(song_length)

        except:
            pass

    def set_volume(self):
        self.volume = self.volume_slider.value()
        print(self.volume)
        mixer.music.set_volume(self.volume/100)

    def mute_sound(self):
        global muted

        if muted == False:
            mixer.music.set_volume(0.0)
            muted = True
            self.mute_button.setIcon(QIcon("icons/unmuted.png"))
            self.mute_button.setToolTip('UnMute')
            self.volume_slider.setValue(0)

        else:
            mixer.music.set_volume(0.7)
            muted = False
            self.mute_button.setToolTip('Mute')
            self.mute_button.setIcon(QIcon("icons/mute.png"))
            self.volume_slider.setValue(70)

    def update_progress_bar(self):
        global count
        global song_lenth
        count += 1
        self.progress_bar.setValue(count)
        self.song_timer_label.setText(time.strftime("%M:%S", time.gmtime(count)))
        if count == song_length:
            self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window = Player()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
