#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import resources.voice_resources

from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *

class Voice(QMediaPlayer):

    def __init__(self):
        super().__init__()

        self.id = ''

    def play_voice(self, voice_id):

        self.id = voice_id

        self.setMedia(
                QMediaContent(QUrl(
                'qrc:/vc/{0}.mp3'.format(
                self.id))))
        self.play()
