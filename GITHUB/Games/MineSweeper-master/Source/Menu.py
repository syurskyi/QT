from PyQt5.QtWidgets import QAction, qApp
import webbrowser
from Source import globals


class Menu:
    def __init__(self, window, signals):
        self.window = window
        self.signals = signals
        self.menu_bar = window.menuBar()
        self.status_bar = window.statusBar()

        file_menu = self.menu_bar.addMenu('File')
        file_menu.addAction(self.exit())

        options_menu = self.menu_bar.addMenu('Options')
        options_menu.addAction(self.dark())
        options_menu.addAction(self.music())
        options_menu.addAction(self.question_marks())
        options_menu.addAction(self.no_bomb_in_first_click())
        options_menu.addAction(self.turn_off_loose_animation())
        options_menu.addAction(self.help())

    def exit(self):
        exit_action = QAction('Exit', self.window)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit program without save')

        def exit_without_ask():
            globals.save_values()
            qApp.quit()

        exit_action.triggered.connect(exit_without_ask)
        return exit_action

    def music(self):
        music_action = QAction('Music', self.window)
        music_action.setCheckable(True)
        music_action.setChecked(globals.music)
        music_action.setShortcut('Ctrl+M')

        def checked():
            if not music_action.isChecked():
                globals.music = False
                music_action.setStatusTip('Turn on Music')
                self.signals.stop_music.emit()
            else:
                globals.music = True
                music_action.setStatusTip('Turn off Music')
                self.signals.play_music.emit()

        checked()
        music_action.triggered.connect(checked)
        return music_action

    def dark(self):
        dark_action = QAction('Set black view', self.window)
        dark_action.setShortcut('Ctrl+B')
        dark_action.setStatusTip("Change a style on dark")
        # to finish
        return dark_action

    def help(self):
        open_webb = QAction('Help', self.window)
        open_webb.setShortcut('Ctrl+H')
        open_webb.setStatusTip('Display a website with rules')

        def web():
            self.signals.pause.emit()
            webbrowser.open("https://en.wikipedia.org/wiki/Minesweeper_(video_game)")

        open_webb.triggered.connect(web)
        return open_webb

    def question_marks(self):
        question_marks = QAction('Question marks(?)', self.window)
        question_marks.setCheckable(True)
        question_marks.setChecked(globals.question_marks)
        question_marks.setShortcut('Ctrl+H')

        def checked():
            if not question_marks.isChecked():
                globals.question_marks = False
                self.signals.hide_question_marks.emit()
                question_marks.setStatusTip('Turn on questions marks')
            else:
                globals.question_marks = True
                question_marks.setStatusTip('Turn off questions marks')

        checked()
        question_marks.triggered.connect(checked)
        return question_marks

    def no_bomb_in_first_click(self):
        first_click = QAction('No bomb in first click', self.window)
        first_click.setCheckable(True)
        first_click.setChecked(globals.no_bomb_in_first_click)

        def checked():
            if first_click.isChecked():
                globals.no_bomb_in_first_click = True
                first_click.setStatusTip('Set that you always click empty field in first click')
            else:
                globals.no_bomb_in_first_click = False
                first_click.setStatusTip('Set that you can draw a bomb in first click')

        checked()
        first_click.triggered.connect(checked)
        return first_click

    def turn_off_loose_animation(self):
        turn_off = QAction('Game over animation', self.window)
        turn_off.setCheckable(True)
        turn_off.setChecked(globals.loose_animation)

        def checked():
            if not turn_off.isChecked():
                globals.loose_animation = False
                turn_off.setStatusTip('Set available game over animation')
            else:
                globals.loose_animation = True
                turn_off.setStatusTip('Set switch off game over animation')

        checked()
        turn_off.triggered.connect(checked)
        return turn_off
