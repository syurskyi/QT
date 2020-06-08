import sys
from PyQt4.QtGui import *

def main():
    app = QApplication ( sys.argv )
    button = QPushButton ( "Hello World!", None )
    button.show()
    app.exec_()

if __name__ == '__main__':
    main()
