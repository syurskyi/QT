__author__ = 'Serhii Yurskyi'
__version__ = '1.0'

import os
import sys
import PyQt5

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import PYQT_VERSION_STR

import launcher_model

PyQt5_VER = PYQT_VERSION_STR
PY_VER = sys.version[:3]

# print("Python version :", PY_VER)
# print("PyQt version:", PyQt5_VER )


class LauncherGUI(QtWidgets.QWidget):
    """
    The goal of this tool is to create a GUI that allows the user to quickly create, select and delete workspaces
    and add, remove and launch applications within those workspaces.
    """
    def __init__(self, parent=None):
        super(LauncherGUI, self).__init__(parent)

        self._icons = QtWidgets.QFileIconProvider()
        self._my_path = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(self._my_path, 'images')
        full_path = os.path.join(image_path, 'launcher.png')
        self._tpl_icon = QtGui.QIcon(full_path)


        self._setup()

    # ================ SETUP UI ========================================================================================

    def _setup(self):
        v_layout = QtWidgets.QVBoxLayout(self)

        v_layout.addLayout(self._setup_header())
        v_layout.addWidget(self._setup_apps())

        self.setWindowTitle('SYurskyi\'s Launcher' + __version__)
        self. setWindowIcon(self._tpl_icon)
        flag = QtCore.Qt.WindowCloseButtonHint
        self.setWindowFlags(QtCore.Qt.Window | flag)
        self.resize(190, 200)

    def _setup_header(self):
        h_layout = QtWidgets.QHBoxLayout()
        workspace_gb = QtWidgets.QGroupBox('Workspaces')
        v_layout = QtWidgets.QVBoxLayout(workspace_gb)

        self._workspace_cb = QtWidgets.QComboBox()

        v_layout.addWidget(self._workspace_cb)
        h_layout.addWidget(workspace_gb)
        h_layout.addStretch()
        return h_layout

    def _setup_apps(self):
        self._app_lw = QtWidgets.QListWidget()
        self._app_lw.setAlternatingRowColors(True)
        flag = QtWidgets.QAbstractItemView.InternalMove
        self._app_lw.setDragDropMode(flag)
        return self._app_lw


if __name__ == '__main__':
    print(PY_VER)
    print(PyQt5_VER)
    app = QtWidgets.QApplication(sys.argv)
    ex = LauncherGUI()
    ex.show()
    sys.exit(app.exec_())






