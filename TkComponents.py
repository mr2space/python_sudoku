import customtkinter as ck
from constants import Color
from PIL import Image
import sys
import os


class TextScreen():
    def __init__(self, text, app:ck.CTk, rowid=0, colid=0, weight=1) -> None:
        self.text = text
        self.pos = (rowid, colid)
        self.app = app
        self.Color = Color()
        self.set_text()
        
        
    def set_text(self):
        self.textlabel = ck.CTkButton(master=self.app, height=50, width=150, text=self.text, font=("Arial", 90), bg_color=self.Color.screen_bg,fg_color=self.Color.screen_bg, hover_color=self.Color.screen_bg, corner_radius=25)
        self.textlabel.grid(row=self.pos[0],column=self.pos[1])

class Screen():
    img_path = r"imgs\bg_min_.png"
    img_path2 = r"imgs\bg_min_final.png"
    
    def __init__(self, app:ck.CTk, win_size:tuple[int, int]) -> None:
        self.app = app
        self.win_size = win_size
        self.Color = Color()
        self.app.resizable(0,0)
        self.app.config(background=self.Color.screen_bg)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure((0,1,3), weight=1, uniform='a')
        self.__set_image(self.app,self.img_path)
        self.__display_content()

    
    
    def __offline_start(self,frame):
        button = ck.CTkButton(frame,width=170,height=40,text="Start Offline",bg_color=self.Color.screen_bg,fg_color=self.Color.white_bg, hover=self.Color.white_bg, text_color=self.Color.primary,font=("Arial",16))
        button.grid(row=0,column=1)
        
    def __online_start(self,frame):
        button = ck.CTkButton(frame,width=170,height=40,  text="Start Online",
                              bg_color=self.Color.screen_bg,fg_color=self.Color.primary, hover=self.Color.primary, text_color=self.Color.white_bg,font=("Arial",16))
        button.grid(row=1,column=1)
    
    def __display_content(self):
        #self.header = TextScreen("Sudoku", self.app)
        frame = ck.CTkFrame(self.app, bg_color=self.Color.screen_bg, fg_color=self.Color.screen_bg)
        self.__set_image(frame,self.img_path2)
        frame.columnconfigure((0,1,2),weight=1,uniform='a')
        frame.rowconfigure((0,1),weight=1)
        frame.grid(row=1, sticky="nwes")
        self.__offline_start(frame)
        self.__online_start(frame)
    
    def __set_image(self,app,path):
        img_path = self.resource_path(path)
        img = Image.open(img_path)
        bg_img = ck.CTkImage(img, size=(self.win_size))
        bg_lb = ck.CTkLabel(app, text="", image=bg_img,anchor="center")
        bg_lb.place(x=0, y=0)
        label = ck.CTkLabel(app, text="")
        label.grid(row=0,column=0)
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def startLoop(self):
        self.app.mainloop()
    