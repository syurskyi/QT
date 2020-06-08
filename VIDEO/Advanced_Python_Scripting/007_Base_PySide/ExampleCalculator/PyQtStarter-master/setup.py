# settings to use py2exe to create executable for win, adapt python version if needed

from distutils.core import setup
import py2exe

includes = ["sip",
            "PyQt5",
            "PyQt5.QtCore",
            "PyQt5.QtGui",
            ]

datafiles = [
    ("platforms",
        ["C:\\Python34\\Lib\\site-packages\\PyQt5\\plugins\\platforms\\qwindows.dll"]),
    ("", ["C:\\windows\\syswow64\\MSVCP100.dll", "C:\\windows\\syswow64\\MSVCR100.dll"])]

setup(
    console=['run.py'],
    packages=['pyqtstarter'],
    data_files=datafiles,
    options={
        "py2exe": {
            "includes": includes,
        }
    }
)
