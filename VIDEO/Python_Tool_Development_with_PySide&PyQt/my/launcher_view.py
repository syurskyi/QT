#!/usr/bin/env python

__author__ = 'Serhii Yurskyi'
__version__ = '1.0'

import os
import sys
from collections import defaultdict

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import PYQT_VERSION_STR

import launcher_model

PyQt5_VER = PYQT_VERSION_STR
PY_VER = sys.version[:3]


class Delete_Btn(QtWidgets.QPushButton):
    ''' Custom button that Triggers parent's 'delete_item' function. '''
    def __init__(self, parent=None):
        super(Delete_Btn, self).__init__(parent)


class LauncherGUI(QtWidgets.QWidget):
    """
    The goal of this tool is to create a GUI that allows the user to quickly create, select and delete workspaces
    and add, remove and launch applications within those workspaces.
    """
    def __init__(self, parent=None):
        super(LauncherGUI, self).__init__(parent)

        self._icons = QtWidgets.QFileIconProvider()
        self._my_path = os.path.dirname(os.path.realpath(__file__))
        images_path = os.path.join(self._my_path, 'images')
        full_path = os.path.join(images_path, 'launcher.png')
        self._tpl_icon = QtGui.QIcon(full_path)

        self._launcher = launcher_model.LauncherModel()

        self._edit_op = {
            True: self._edit_on,
            False: self._edit_off
        }
        self._app_instruction = True
        self._file_dialogs = defaultdict(lambda: self._file_dialog)
        self._file_dialogs['PyQt5'] = self._file_dialog_pyqt5
        self._dragging = None
        self._delete_op = {
            'workspace': self._delete_workspace,
            'application': self._delete_app
        }

        self._setup()
        self._testing()
        self._edit_toggle()

    # ================ SETUP UI ========================================================================================

    def _setup(self):
        v_layout = QtWidgets.QVBoxLayout(self)

        v_layout.addLayout(self._setup_header())
        v_layout.addLayout(self._setup_edit_options())
        v_layout.addWidget(self._setup_apps())

        self._setup_connections()

        self.setWindowTitle('SYurskyi\'s Launcher' + __version__)
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
        add_menu.addAction('Workspace', self._add_workspace)
        add_menu.addAction('App or File', self._add_app)
        self._add_btn.setMenu(add_menu)

        self._del_btn = Delete_Btn(self)
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

    # ================ DISPLAY ========================================================================================

    def _populate_workspaces(self):
        ws = self._workspace_changed
        self._workspace_cb.currentIndexChanged.disconnect(ws)
        self._workspace_cb.clear()
        self._workspace_cb.addItems(self._launcher.get_workspaces())
        self._workspace_cb.currentIndexChanged.connect(ws)
        self._populate_apps()

    def _populate_apps(self):
        self._app_lw.clear()
        ws = self.get_workspace()
        for app_name in self._launcher.get_app_names(ws):
            item = QtWidgets.QListWidgetItem(self._app_lw)
            icon = self._launcher.get_app_icon(ws, app_name)
            if icon:
                item.setIcon(QtGui.QIcon(icon))
            else:
                item.setIcon(self._icons.icon(self._icons.File))
            item.setText(app_name)

    # ================ WORKSPACE + APP ================================================================================

    def get_workspace(self):
        ''' Returns the currently selection workspace from combobox. '''
        return str(self._workspace_cb.currentText())

    def _workspace_changed(self):
        self._populate_apps()

    def _run_app(self, item):
        item.setSelected(False)
        self._launcher.run_app(self.get_workspace(), str(item.text()))

    # ================ EDIT MODE ======================================================================================

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

    # ================ ADD ============================================================================================

    def _add_workspace(self):
        ws = 'New WORKSPACE'
        msg = 'What would you like to title the new WORKSPACE?'
        text = QtWidgets.QInputDialog.getText(self, ws, msg)[0]
        if text:
            self._launcher.add_workspace(str(text))
            self._populate_workspaces()
            index = self._workspace_cb.findText(text)
            self._workspace_cb.setCurrentIndex(index)

    def _add_app(self):
        if self._app_instruction:
            msg = '1) Select the application file\n'
            msg += '2) Select a app icon image (Optional)'
            QtWidgets.QMessageBox.information(self, 'Add App', msg)
            self._app_instruction = False
        sel = 'Select APP file'
        app = self._file_dialogs[PyQt5_VER](sel, self._my_path)
        if app:
            path = os.path.split(app)[0]
            msg = 'Select ICON file (optional)'
            icon = self._file_dialogs[PyQt5_VER](msg, path)
            self._launcher.add_app(self.get_workspace(), app, icon)
            self._populate_apps()

    def _file_dialog(self, msg, path):
        return QtWidgets.QFileDialog.getOpenFileName(self, msg, path)[0]

    def _file_dialog_pyqt5(self, msg, path):
        fd = QtWidgets.QFileDialog.getOpenFileName(self, msg, path)
        return str(fd)

    # ================ DELETE =========================================================================================

    def _delete_app(self, app_name):
        self._tp_launcher.delete_app(self.get_workspace(), app_name)
        self._populate_apps()

    def _delete_workspace(self, ws_name):
        self._tp_launcher.delete_workspace(ws_name)
        self._populate_workspaces()

    def delete_item(self):
        ''' Delete the item dragged onto Delete button '''
        typ = self._dragging[0]
        name = self._dragging[1]
        title = 'Delete {}?'.format(typ)
        msg = 'Are you sure you want to delete {} "{}"'.format(typ, name)
        no = QtWidgets.QMessageBox.No
        yes = QtWidgets.QMessageBox.Yes
        btn = QtWidgets.QMessageBox.warning(self, title, msg, yes, no)
        if btn == yes:
            self._delete_op[typ](name)

    # ================ TEST CODE ======================================================================================

    def _testing(self):
        ws1 = 'My_first_workspace'
        ws2 = 'My_second_workspace'
        ## CHANGE TO YOUR COMPUTER PATHS
        app1 = r'C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe'
        icon1 = r'C:\Users\syurskyi\PycharmProjects\QT\VIDEO\Python_Tool_Development_with_PySide&PyQt\my\icons\chrome.png'
        app2 = r'C:\Program Files (x86)\Notepad++\notepad++.exe'
        icon2 = r'C:\Users\syurskyi\PycharmProjects\QT\VIDEO\Python_Tool_Development_with_PySide&PyQt\my\icons\notepad++.ico'
        self._launcher.add_workspace(ws1)
        self._launcher.add_app(ws1, app1, icon1)
        self._launcher.add_app(ws1, app2, icon2)
        self._launcher.add_workspace(ws2)
        self._launcher.add_app(ws2, app2, icon2)
        self._populate_workspaces()

    def _print_ham(self):
        print('ham')

if __name__ == '__main__':
    print(PY_VER)
    print(PyQt5_VER)
    app = QtWidgets.QApplication(sys.argv)
    ex = LauncherGUI()
    ex.show()
    sys.exit(app.exec_())






