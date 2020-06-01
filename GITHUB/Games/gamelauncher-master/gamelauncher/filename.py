import os
import re
#some keywords to filter out games
keywords = ["vcredist", "redist", "000", "install", "unistall", "unist",
"x360", "setup", "cleanup", "clean", "ui", "activation", "trial", "dxsetup", 
"vcredist_x64", "vcredist_x86", "emulator", "service", "external", "market", 
"dotnet", "inst", "bugreport", "adb", "crash", "report", "touch"]

#game directory 
game_directory = "D:\\Games"

#search in the game directory
for root, dirs, files in os.walk(game_directory):
    for f in files:
        if f.endswith('.exe'):
            s = str(os.path.basename(f))
            flag = True
            for k in keywords:
                if re.search(k, s, re.IGNORECASE):
                    flag = False
            
            if flag:
                print(f)
             