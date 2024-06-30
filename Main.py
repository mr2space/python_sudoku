import customtkinter as ck
from PIL import Image
from constants import Color
import TkComponents as App
import sys
import os

# constants

WIN_WIDTH:int = 800
WIN_HEIGHT:int = 700
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


app = ck.CTk();
app.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
app.title("Sudoku Game")



Home = App.Screen(app, (WIN_WIDTH, WIN_HEIGHT))
Home.startLoop()
