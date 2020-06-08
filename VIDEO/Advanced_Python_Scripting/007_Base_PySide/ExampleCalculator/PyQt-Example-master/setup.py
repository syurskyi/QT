import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_exe_options = {"packages": [], "excludes": [], "include_files":["icon.png", "converter.py", "interface.py"]}

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(
        "converter.py", 
        base=base, 
        icon = "icon.png"
        )
]

setup(name='PyConverter',
      version = '0.5',
      author='Luiyi Dilone',
      author_email='dilone@outlook.com',
      url='https://digidev.do/',
      description = 'Temperature Converter using PyQt',
      options = {"build_exe": build_exe_options},
      executables = executables)
