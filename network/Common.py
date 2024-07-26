import sys
import subprocess


# TODO: BETTER WAY TO WRITE AND OPTIMIZE
def runAndClose(file_path = "GameMain.py"):
    game_ui = file_path
    subprocess.Popen([sys.executable, game_ui])
    sys.exit()