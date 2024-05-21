from .Constants import *
from .Buttons import *

class Label:
    def __init__(self, win, pos:tuple[int, int], color:tuple[int, int, int], name: str, event = None):
        self.win = win
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.name = name
        self.event = event
    
    def draw(self, value:str):
        self.text = Button(self.name, self.x, self.y, 100, 55, self.color)
        self.text.draw(self.win)
        self.button = Button(value, self.x, self.y+55, 100, 55, self.color)
        self.button.draw(self.win)


class Time(Label):
    time = [0,0]
    def setTime(self):
        self.time[1] += 1
        self.time[0] += (self.time[1]//60)
        self.time[1] = (self.time[1]%60)
        time.sleep(1)
    
    def show_time(self):
        self.draw('A')
        print("time")
        while self.event and (not self.event.is_set()):
            self.draw(f'{self.time[0]}:{self.time[1]}')
            self.setTime()
            
            
        

    
    

