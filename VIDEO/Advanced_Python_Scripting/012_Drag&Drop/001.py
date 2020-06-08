import sys
import os
from PySide.QtCore import *
from PySide.QtGui import *


class listWidgetClass(QListWidget):
    def __init__(self):
        super(listWidgetClass, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setDragDropMode(QAbstractItemView.DropOnly)

    def dropEvent(self, event):
        print 'DROP', type(event)
    #     mimedata = event.mimeData()
    #     if mimedata.hasText():
    #         print 'text'
    #         # print mimedata.hasText()
    #     elif mimedata.hasUrls():
    #         print 'urls'
    #         # print mimedata.urls()
    #
    def dragEnterEvent(self, event):
        event.accept()
        print 'ENTER', type(event)

    def dragMoveEvent(self, event):
        event.accept()
        # print 'MOVE'


if __name__ == '__main__':
    import sys

    app = None
    try:
        import nuke
    except ImportError:
        app = QApplication(sys.argv)
    main = listWidgetClass()
    main.show()

    if app is not None:
        app.exec_()