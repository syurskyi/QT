#!/usr/bin/env python

__author__ = 'Trevor Payne'
__version__ = '1.0'

import os
import sys

import Qt
from Qt import QtWidgets, QtCore, QtGui
import tp_launcher_model

QT_VER = Qt.__binding__
PY_VER = sys.version[:3]


class TP_Launcher_GUI(QtWidgets.QWidget):
    '''The goal of this tool is to create a GUI that 
        allows the user to quickly create, select and 
        delete workspaces and add, remove and launch
        applications within those workspaces.
    '''
    def __init__(self, parent=None):
        super(TP_Launcher_GUI, self).__init__(parent)

        self._icons = QtWidgets.QFileIconProvider()
        self._my_path = os.path.dirname(os.path.realpath(__file__))
        images_path = os.path.join(self._my_path, 'images')
        full_path = os.path.join(images_path, 'TPayne_Launcher.png')
        self._tpl_icon = QtGui.QIcon(full_path)

        self._tp_launcher = tp_launcher_model.TP_Launcher_Model()

        self._setup()
        self._testing()

    #======= SETUP UI =================================

    def _setup(self):
        v_layout = QtWidgets.QVBoxLayout(self)

        v_layout.addLayout(self._setup_header())
        v_layout.addWidget(self._setup_apps())

        self._setup_connections()

        self.setWindowTitle('TPayne\'s Launcher ' + __version__)
        self.setWindowIcon(self._tpl_icon)
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

    def _setup_connections(self):
        ws = self._workspace_changed
        self._workspace_cb.currentIndexChanged.connect(ws)

        self._app_lw.itemClicked.connect(self._run_app) ## TEMP

    #======= DISPLAY =================================

    def _populate_workspaces(self):
        self._workspace_cb.clear()
        self._workspace_cb.addItems(self._tp_launcher.get_workspaces())
        self._populate_apps()

    def _populate_apps(self):
        self._app_lw.clear()
        ws = self.get_workspace()
        for app_name in self._tp_launcher.get_app_names(ws):
            item = QtWidgets.QListWidgetItem(self._app_lw)
            icon = self._tp_launcher.get_app_icon(ws, app_name)
            if icon:
                item.setIcon(QtGui.QIcon(icon))
            else:
                item.setIcon(self._icons.icon(self._icons.File))
            item.setText(app_name)

    #======= WORKSPACE + APP =================================

    def get_workspace(self):
        ''' Returns the currently selection workspace from combobox. '''
        return str(self._workspace_cb.currentText())

    def _workspace_changed(self):
        self._populate_apps()

    def _run_app(self, item):
        item.setSelected(False)
        self._tp_launcher.run_app(self.get_workspace(), str(item.text()))

    def _testing(self):
        ws1 = 'My_first_workspace'
        ws2 = 'My_second_workspace'
        ## CHANGE TO YOUR COMPUTER PATHS
        app1 = r'C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe'
        icon1 = r'C:\Program Files (x86)\Google\Chrome\Application\61.0.3163.100\VisualElements\smalllogo.png'
        app2 = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self._tp_launcher.add_workspace(ws1)
        self._tp_launcher.add_app(ws1, app1, icon1)
        self._tp_launcher.add_app(ws1, app2, None)
        self._tp_launcher.add_workspace(ws2)
        self._tp_launcher.add_app(ws2, app2, None)
        self._populate_workspaces()


if __name__ == '__main__':
    print (PY_VER)
    print (QT_VER)
    app = QtWidgets.QApplication(sys.argv)
    ex = TP_Launcher_GUI()
    ex.show()
    sys.exit(app.exec_())

