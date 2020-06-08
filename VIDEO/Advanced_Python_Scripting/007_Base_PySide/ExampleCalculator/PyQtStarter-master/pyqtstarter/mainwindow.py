from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QSettings, pyqtSlot

from pyqtstarter import __version__
from pyqtstarter.ui.MainWindow_py import Ui_MainWindow


class MainWindow(QMainWindow):
    """Main window"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.read_settings()

        self.ui.statusbar.showMessage("Version: %s" % __version__, 5000)

    def read_settings(self):
        """Reads application settings and applies them"""

        settings = QSettings()

        value = settings.value('myValue')
        if value:
            # do something with it
            pass

    def write_settings(self):
        """Saves known application settings to disk"""

        settings = QSettings()

        settings.setValue('myValue', 123456)

        # per PyQt docs to force write almost immediately...
        del settings

    @pyqtSlot(bool)
    def on_actionAbout_Qt_triggered(self, checked):
        msgbox = QMessageBox.aboutQt(self)

    @pyqtSlot()
    def on_centeredPushButton_clicked(self):
        msgbox = QMessageBox.aboutQt(self)
