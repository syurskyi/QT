from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys, os, random
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

ui,_ = loadUiType("main.ui")

class MainApp(QMainWindow, ui):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Action_Button()
        self.UI()
        self.Answer = 0
        self.count = 0


    def UI(self):
        style = open("stylesheet.css","r")
        style = style.read()
        self.setStyleSheet(style)


    def Action_Button(self):
        self.pushButton.clicked.connect(self.start_game)
        self.pushButton_2.clicked.connect(self.check_answer)
        self.pushButton_3.clicked.connect(self.reset_game)
        self.pushButton_4.clicked.connect(self.quit_game)


    def start_game(self):
        low_range = self.lineEdit.text()
        high_range = self.lineEdit_2.text()
        if low_range=="" or high_range=="":
            speak.Speak("Data Error, enter low and high number")
            QMessageBox.warning(self,"Data Error","Please Fill the low and High Value")
        else:
            speak.Speak("Game Started, Guess Number Between "+str(low_range)+" and "+str(high_range))
            self.Answer = random.randint(int(low_range),int(high_range))


    def check_answer(self):
        guess_number = self.lineEdit_3.text()
        low_range = self.lineEdit.text()
        high_range = self.lineEdit_2.text()
        if guess_number == "":
            speak.Speak("Data Error, enter number")
            QMessageBox.warning(self, "Data Error", "Please Enter Number")
        else:
            if int(guess_number)>self.Answer:
                self.count += 1
                speak.Speak("Guess Less than this")
                self.label_4.setText("Guess Less than this")
                self.lineEdit_3.setText("")
            elif int(guess_number)<self.Answer:
                self.count += 1
                speak.Speak("Guess Higher than this")
                self.label_4.setText("Guess Higher than this")
            elif int(guess_number) == self.Answer:
                speak.Speak("Hurray, Finally You Guessed It")
                self.label_4.setText("Congratulations! Finally You Guessed it")
            else:
                speak.Speak("Error, Number is not between "+str(low_range)+" and "+str(high_range))
                self.lineEdit_3.setText("")

        self.label_5.setText("You Tried : "+str(self.count)+" Times")




    def reset_game(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.Answer = 0
        self.count = 0



    def quit_game(self):
        speak.Speak("Quitting game Good bye")
        exit()



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()