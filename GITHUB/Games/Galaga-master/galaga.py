from PyQt5.QtWidgets import QApplication
import gui
import sys


class Galaga():

    def __init__(self):
        print('STARTING APPLICATION')
        self.game = gui.GameWindow()
        self.game.startAgain.connect(self.startGame)

    def startGame(self):
        try:
            print('STARTING APPLICATION AGAIN')
            self.game.stopThreads()
            print('Stopped threads')
            self.game = gui.GameWindow()
            self.game.startAgain.connect(self.startGame)
        except Exception as e:
            print('Exception in StartGame/Galaga: ', str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = Galaga()
    sys.exit(app.exec_())

