from dataclasses import dataclass
import sys
import os

@dataclass
class Color:
    screen_bg:str = "#041562" #dark blue
    primary:str = "#11468F" #light blue
    secondary: str = "#DA1212" #red
    white_bg:str  = "#EEEEEE" #white


@dataclass   
class WindowSpec:
    COLOR_PURPLE:tuple[int, int, int] = (101, 33, 255)
    WIN_WIDTH:int = 800
    WIN_HEIGHT:int = 700
    
    difficulty:int = 100
    failed_attempt:int = 3
    
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
