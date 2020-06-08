'''
coder-Shubham maddhashiya
(16NA10027)

following Python with PyQt code is for a advance calculater with several important Math Function

NOTE-1) RUN THIS CODE WITH PYTHON-3 OR ABOVE AND PYQT-4
     2) ON PYTHON VERSION BELOW 3, CODE WILL NOT WORK PROPERLY(SO FOR RUNNING COMMAND SHOULD BE-python3 MyCalculater.py)
     3) FOR USING ANY MATHEMATICAL FUNCTION ...SYNTAX...WILL BE LIKE THIS ...FOR SQUARE ROOT...sqrt(input)...factorial(input)

   now keep this things in mind you can solve your multi complex calculation in seconds...

         #HAPPY CODING
'''
import sys
from PyQt4 import QtGui, QtCore
import math
class Shubham(QtGui.QMainWindow):
    flag=1
    
    def __init__(self):
        super(Shubham, self).__init__()
        self.initUI()
        
    def initUI(self):

               
                       # FOLLOWING CODE FOR WINDOW, BUTTON AND TEXTPAD


        self.setGeometry(100,100,255,331)
        self.setWindowTitle("MyCalculater")
        self.setStyleSheet("background-color:black")
        font = QtGui.QFont()
        font.setPointSize(11)
        font1 = QtGui.QFont()
        font1.setPointSize(18)
        font2= QtGui.QFont()
        font2.setPointSize(15)


        self.le = QtGui.QLineEdit(self)
        self.le.move(0, 0)
        self.le.setStyleSheet("color: red;")
        self.le.setFont(font2)
        self.le.resize(251, 91)

        self.btn1 = QtGui.QPushButton("C", self)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("color: red;")
        self.btn1.resize(51, 41)
        self.btn1.move(0, 90)
        self.btn1.clicked.connect(lambda: self.Signal('C'))



        self.btn2 = QtGui.QPushButton("7", self)
        self.btn2.resize(51, 41)
        self.btn2.setFont(font)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet(" color: white;")
        self.btn2.move(50, 90)
        self.btn2.clicked.connect(lambda: self.Signal('7'))

        self.btn3 = QtGui.QPushButton("8", self)
        self.btn3.resize(51, 41)
        self.btn3.setStyleSheet(" color: white;")
        self.btn3.move(100, 90)
        self.btn3.setFont(font)
        self.btn3.clicked.connect(lambda: self.Signal('8'))

        self.btn4 = QtGui.QPushButton("9", self)
        self.btn4.resize(51, 41)
        self.btn4.move(150, 90)
        self.btn4.setStyleSheet(" color: white;")
        self.btn4.setFont(font)
        self.btn4.clicked.connect(lambda: self.Signal('9'))

        self.btn5 = QtGui.QPushButton("+", self)
        self.btn5.resize(51, 41)
        self.btn5.setStyleSheet(" color: white;")
        self.btn5.setFont(font)
        self.btn5.setFont(font1)
        self.btn5.move(200, 90)
        self.btn5.clicked.connect(lambda: self.Signal('+'))

        self.btn6 = QtGui.QPushButton("del", self)
        self.btn6.resize(51, 41)
        self.btn6.setFont(font)
        self.btn6.setStyleSheet(" color: white;")
        self.btn6.move(0, 130)
        self.btn6.setStyleSheet("background-color: black; color: red;")
        self.btn6.clicked.connect(lambda: self.Signal('del'))

        self.btn7 = QtGui.QPushButton("4", self)
        self.btn7.resize(51, 41)
        self.btn7.move(50, 130)
        self.btn7.setFont(font)
        self.btn7.setStyleSheet(" color: white;")
        self.btn7.clicked.connect(lambda: self.Signal('4'))

        self.btn8 = QtGui.QPushButton("5", self)
        self.btn8.resize(51, 41)
        self.btn8.setFont(font)
        self.btn8.move(100, 130)
        self.btn8.setStyleSheet(" color: white;")
        self.btn8.clicked.connect(lambda: self.Signal('5'))

        self.btn9 = QtGui.QPushButton("6", self)
        self.btn9.resize(51, 41)
        self.btn9.setStyleSheet(" color: white;")
        self.btn9.move(150, 130)
        self.btn9.setStyleSheet(" color: white;")
        self.btn9.setFont(font)
        self.btn9.clicked.connect(lambda: self.Signal('6'))

        self.btn10 = QtGui.QPushButton("-", self)
        self.btn10.resize(51, 41)
        self.btn10.setFont(font)
        self.btn10.move(200, 130)
        self.btn10.setFont(font1)
        self.btn10.setStyleSheet(" color: white;")
        self.btn10.clicked.connect(lambda: self.Signal('-'))

        self.btn11 = QtGui.QPushButton("sin", self)
        self.btn11.resize(51, 41)
        self.btn11.setFont(font)
        self.btn11.setStyleSheet(" color: white;")
        self.btn11.move(0, 170)
        self.btn11.clicked.connect(lambda: self.Signal('math.sin('))

        self.btn12 = QtGui.QPushButton("1", self)
        self.btn12.resize(51, 41)
        self.btn12.move(50, 170)
        self.btn12.setStyleSheet(" color: white;")
        self.btn12.setFont(font)
        self.btn12.clicked.connect(lambda: self.Signal('1'))

        self.btn13 = QtGui.QPushButton("2", self)
        self.btn13.resize(51, 41)
        self.btn13.move(100, 170)
        self.btn13.setFont(font)
        self.btn13.setStyleSheet(" color: white;")
        self.btn13.clicked.connect(lambda: self.Signal('2'))

        self.btn14 = QtGui.QPushButton("3", self)
        self.btn14.resize(51, 41)
        self.btn14.move(150, 170)
        self.btn14.setFont(font)
        self.btn14.setStyleSheet(" color: white;")
        self.btn14.clicked.connect(lambda: self.Signal('3'))

        self.btn15 = QtGui.QPushButton("*", self)
        self.btn15.resize(51, 41)
        self.btn15.setFont(font)
        self.btn15.setFont(font1)
        self.btn15.setStyleSheet(" color: white;")
        self.btn15.move(200, 170)
        self.btn15.clicked.connect(lambda: self.Signal('*'))

        self.btn16 = QtGui.QPushButton("cos", self)
        self.btn16.resize(51, 41)
        self.btn16.setFont(font)
        self.btn16.move(0, 210)
        self.btn16.setStyleSheet(" color: white;")
        self.btn16.clicked.connect(lambda: self.Signal('math.cos('))

        self.btn17 = QtGui.QPushButton("log", self)
        self.btn17.resize(51, 41)
        self.btn17.setFont(font)
        self.btn17.setStyleSheet(" color: white;")
        self.btn17.move(50, 210)
        self.btn17.clicked.connect(lambda: self.Signal('math.log10('))

        self.btn18 = QtGui.QPushButton("0", self)
        self.btn18.resize(51, 41)
        self.btn18.setFont(font)
        self.btn18.setStyleSheet(" color: white;")
        self.btn18.move(100, 210)
        self.btn18.clicked.connect(lambda: self.Signal('0'))

        self.btn19 = QtGui.QPushButton(".", self)
        self.btn19.resize(51, 41)
        self.btn19.setFont(font)
        self.btn19.setStyleSheet(" color: white;")
        self.btn19.move(150, 210)
        self.btn19.clicked.connect(lambda: self.Signal('.'))

        self.btn20 = QtGui.QPushButton("/", self)
        self.btn20.resize(51, 41)
        self.btn20.move(200, 210)
        self.btn20.setFont(font1)
        self.btn20.setStyleSheet(" color: white;")
        self.btn20.setFont(font)
        self.btn20.clicked.connect(lambda: self.Signal('/'))

        self.btn21 = QtGui.QPushButton("tan", self)
        self.btn21.resize(51, 41)
        self.btn21.setFont(font)
        self.btn21.setStyleSheet(" color: white;")
        self.btn21.move(0, 250)
        self.btn21.clicked.connect(lambda: self.Signal('math.tan('))

        self.btn22 = QtGui.QPushButton("ln", self)
        self.btn22.resize(51, 41)
        self.btn22.setStyleSheet(" color: white;")
        self.btn22.setFont(font)
        self.btn22.move(50, 250)
        self.btn22.clicked.connect(lambda: self.Signal('math.log('))

        self.btn23 = QtGui.QPushButton("!", self)
        self.btn23.resize(51, 41)
        self.btn23.setFont(font)
        self.btn23.move(100, 250)
        self.btn23.setStyleSheet(" color: white;")
        self.btn23.clicked.connect(lambda: self.Signal('math.factorial('))

        self.btn24 = QtGui.QPushButton("Ans", self)
        self.btn24.resize(51, 41)
        self.btn24.setFont(font)
        self.btn24.move(150, 250)
        self.btn24.setStyleSheet(" color: white;")
        self.btn24.clicked.connect(lambda: self.Signal('Ans'))

        self.btn25 = QtGui.QPushButton("e", self)
        self.btn25.resize(51, 41)
        self.btn25.setFont(font)
        self.btn25.setStyleSheet(" color: white;")
        self.btn25.move(0, 290)
        self.btn25.clicked.connect(lambda: self.Signal('math.e'))

        self.btn26 = QtGui.QPushButton("(", self)
        self.btn26.resize(51, 41)
        self.btn26.setStyleSheet(" color: white;")
        self.btn26.setFont(font)
        self.btn26.move(50, 290)
        self.btn26.clicked.connect(lambda: self.Signal('('))

        self.btn27 = QtGui.QPushButton(")", self)
        self.btn27.resize(51, 41)
        self.btn27.setFont(font)
        self.btn27.move(100, 290)
        self.btn27.setStyleSheet(" color: white;")
        self.btn27.clicked.connect(lambda: self.Signal(')'))

        self.btn28 = QtGui.QPushButton("sqrt", self)
        self.btn28.resize(51, 41)
        self.btn28.setFont(font)
        self.btn28.setStyleSheet(" color: white;")
        self.btn28.move(150, 290)
        self.btn28.clicked.connect(lambda: self.Signal('math.sqrt('))

        self.btn29 = QtGui.QPushButton("=", self)
        self.btn29.resize(51, 81)
        self.btn29.setStyleSheet(" color: white;")
        self.btn29.setFont(font)
        self.btn29.move(200, 250)
        self.btn29.setFont(font1)
        self.btn29.clicked.connect(lambda: self.Signal('='))

        self.show()
         

                                #FOLLOWING CODE FOR EVENT HANDLER FOR BUTTONS


    def Signal(self,n):
        font3 = QtGui.QFont()
        font3.setPointSize(15)

        if Shubham.flag==1:
            global list,ans,Answer
            ans=" "
            list=[]
            Answer=" "
        if n=='Ans':
            list.append(Answer)
            ans=ans+'Ans'
            self.le.setText(str(ans))
        else:
          if n!='=':
            if n!='del':
                if n!='C':
                   list.append(n)
                   if n[0]!='m':
                    ans=ans+n
                    self.le.setText(str(ans))
                   else:
                     if n=='math.log10(':
                        ans=ans+'log('
                        self.le.setText(str(ans))
                     elif n=='math.log(':
                             ans=ans+'ln('
                             self.le.setText(str(ans))
                     else:
                          n=n[5:]
                          ans=ans+n
                          self.le.setText(str(ans))

        if n=='C':
               list[:]=[]
               ans=""
               self.le.clear()
        if n=='del':
              del list[-1]
              self.le.clear()
              a=len(ans)
              ans=ans[0:a-1]
              self.le.setText(str(ans))

        if n=='=':
            
             self.le.clear()
             st="".join(list)
             try:
                result=eval(st)    #USING EVAL FOR SOLVING MATH EXPRESSION STRING
                ans=str(result)
                Answer=str(result)
                ans=""
                list[:]=[]
                self.le.setText(str(result))
             except (ValueError,SyntaxError,ZeroDivisionError):    #CATCHING INVALID FORMAT OR INVALID MATHEMATICS TERM
                  self.le.clear()
                  self.le.setFont(font3)
                  self.le.setText("Invalid Format")

        Shubham.flag=2

        
                                              #DEFINING MAIN FUNCTION
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Shubham()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
