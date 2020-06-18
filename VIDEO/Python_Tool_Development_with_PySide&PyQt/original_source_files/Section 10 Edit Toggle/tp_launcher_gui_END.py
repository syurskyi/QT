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

        self._edit_op = {
            True: self._edit_on,
            False: self._edit_off
        }

        self._setup()
        self._testing()
        self._edit_toggle()

    #======= SETUP UI =================================

    def _setup(self):
        v_layout = QtWidgets.QVBoxLayout(self)

        v_layout.addLayout(self._setup_header())
        v_layout.addLayout(self._setup_edit_options())
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

        self._edit_btn = QtWidgets.QPushButton('Edit')
        self._edit_btn.setMaximumSize(QtCore.QSize(40, 23))
        self._edit_btn.setCheckable(True)

        v_layout.addWidget(self._workspace_cb)
        h_layout.addWidget(workspace_gb)
        h_layout.addStretch()
        h_layout.addWidget(self._edit_btn)
        return h_layout

    def _setup_edit_options(self):
        add_del_l = QtWidgets.QHBoxLayout()

        self._add_btn = QtWidgets.QPushButton('Add')
        self._add_btn.setMaximumSize(QtCore.QSize(60,23))
        add_menu = QtWidgets.QMenu(self)
        add_menu.addAction('Workspace', self._print_ham)
        add_menu.addAction('App or File', self._print_ham)
        self._add_btn.setMenu(add_menu)

        self._del_btn = QtWidgets.QPushButton()
        self._del_btn.setText('Delete')
        self._del_btn.setAcceptDrops(True)
        self._del_btn.setIcon(self._icons.icon(self._icons.Trashcan))
        self._del_btn.setIconSize(QtCore.QSize(32,32))
        self._del_btn.setFlat(True)

        add_del_l.addWidget(self._add_btn)
        add_del_l.addWidget(self._del_btn)
        return add_del_l

    def _setup_apps(self):
        self._app_lw = QtWidgets.QListWidget()
        self._app_lw.setAlternatingRowColors(True)
        flag = QtWidgets.QAbstractItemView.InternalMove
        self._app_lw.setDragDropMode(flag)
        return self._app_lw

    def _setup_connections(self):
        ws = self._workspace_changed
        self._workspace_cb.currentIndexChanged.connect(ws)
        self._edit_btn.clicked.connect(self._edit_toggle)

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

    #======= EDIT MODE =================================

    def _edit_toggle(self):
        self._edit_op[self._edit_btn.isChecked()]()
        self._app_lw.setDragEnabled(self._edit_btn.isChecked())
        self._add_btn.setVisible(self._edit_btn.isChecked())
        self._del_btn.setVisible(self._edit_btn.isChecked())

    def _edit_on(self):
        self._app_lw.itemClicked.disconnect(self._run_app)
        self._edit_btn.setText('Done')

    def _edit_off(self):
        self._app_lw.itemClicked.connect(self._run_app)
        self._edit_btn.setText('Edit')

    #======= TEST CODE =================================

    def _testing(self):
        ws1 = 'My_first_workspace'
        ws2 = 'My_second_workspace'
        ## CHANGE TO YOUR COMPUTER PATHS
        app1 = r'C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe'
        icon1 = r'C:\Program Files (x86)\Google\Chrome\Application\61.0.3163.100\VisualElements\smalllogo.png'
        app2 = r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        self._tp_launcher.add_workspace(ws1)
        self._tp_launcher.add_app(ws1, app1, icon1)
        self._tp_launcher.add_app(ws1, app2, None)
        self._tp_launcher.add_workspace(ws2)
        self._tp_launcher.add_app(ws2, app2, None)
        self._populate_workspaces()

    def _print_ham(self):
        print('ham')


if __name__ == '__main__':
    print (PY_VER)
    print (QT_VER)
    app = QtWidgets.QApplication(sys.argv)
    ex = TP_Launcher_GUI()
    ex.show()
    sys.exit(app.exec_())

# Copyright (c) 2017 Trevor Payne
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.