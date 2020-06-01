import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.show()
    
    sys.exit(app.exec_())