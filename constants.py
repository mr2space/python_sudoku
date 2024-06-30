import dataclasses

@dataclasses.dataclass
class Color:
    screen_bg:str = "#041562" #dark blue
    primary:str = "#11468F" #light blue
    secondary: str = "#DA1212" #red
    white_bg:str  = "#EEEEEE" #white