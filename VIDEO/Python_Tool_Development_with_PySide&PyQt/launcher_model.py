from collections import OrderedDict, defaultdict
import os
import platform
import subprocess
import webbrowser


class LauncherModel():
    def __init__(self):
        self._workspaces = OrderedDict()
        self._open_doc = defaultdict(lambda: 'open')
        self._open_doc['Window'] = 'start'
        self._platform = platform.system()

    # ================= WORKSPACE ===============================================

    def add_workspaces(self, ws_name):
        self._workspaces[ws_name] = OrderedDict()

    def get_workspaces(self):
        return list(self._workspaces.keys())

    def delete_workspaces(self, ws_name):
        del self._workspaces[ws_name]

    # ================= APPS ====================================================

    def get_app_names(self, ws_name):
        return self._workspaces[ws_name].keys()

    def get_app_icon(self, ws_name, app_name):
        return self._workspaces[ws_name][app_name][1]

    def add_app(self, ws_name, app_path, icon_path):
        app_name = os.path.splitext(os.path.basename(app_path))[0]
        self._workspaces[ws_name][app_name] = [app_path, icon_path]

    def delete_app(self, ws_name, app_name):
        del self._workspaces[ws_name][app_name]

    def reorder_apps(self, ws_name, app_list):
        if self._workspaces[ws_name].keys() != app_list:
            temp = OrderedDict()
            for name in app_list:
                temp[name] = self._workspaces[ws_name][name]
            self._workspaces[ws_name] = temp

    def run_app(self, ws_name, app_name):
        _file = self._workspaces[ws_name][app_name][0]
        if os.path.exists(_file):
            try:
                subprocess.Popen(_file)
            except:
                os.system(self._open_doc[self._platform] + _file)
        else:
            raise ValueError('Exe file no longer exists')

    def run_youtube(self):
        webbrowser.open('http://www.youtube.com/TPayneExperience')
