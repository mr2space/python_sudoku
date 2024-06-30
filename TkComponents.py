import customtkinter as ck
from PIL import Image
import sys
import os


class TextScreen():
    def __init__(self, text, app:ck.CTk, rowid=0, colid=0, weight=1) -> None:
        self.text = text
        self.pos = (rowid, colid)
        self.app = app
        self.set_text()
        
        
    def set_text(self):
        self.textlabel = ck.CTkButton(master=self.app, height=30, width=50, text=self.text, font=("Arial", 55), bg_color="#11468F",fg_color="#11468F", hover_color="#11468F", corner_radius=25)
        self.textlabel.grid(row=self.pos[0],column=self.pos[1],sticky="nwes")

class Screen():
    img_path = r"imgs\bg_min.jpg"
    
    def __init__(self, app:ck.CTk, win_size:tuple[int, int]) -> None:
        self.app = app
        self.win_size = win_size
        self.app.resizable(0,0)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure((0,1,3), weight=1, uniform='a')
        self.__set_image()
        self.__display_content()
    
    
    def __offline_start(self,frame):
        button = ck.CTkButton(frame,text="Start Offline",bg_color="#EEEEEE", fg_color="#EEEEEE")
        button.pack(pady=20,expand=True, fill="both")
        
    def __online_start(self,frame):
        button = ck.CTkButton(frame,  text="Start Online",bg_color="#11468F", fg_color="#11468F")
        button.pack(expand=True, fill="both", )
    
    def __display_content(self):
        self.header = TextScreen("Sudoku", self.app)
        frame = ck.CTkFrame(self.app, bg_color="red",)
        frame.grid(row=1)
        self.__offline_start(frame)
        self.__online_start(frame)
    
    def __set_image(self):
        img_path = self.resource_path(self.img_path)
        img = Image.open(img_path)
        bg_img = ck.CTkImage(img, size=(self.win_size))
        bg_lb = ck.CTkLabel(self.app, text="", image=bg_img)
        bg_lb.place(x=0, y=0)
        label = ck.CTkLabel(self.app, text="")
        label.grid(row=0,column=0)
    
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
    def startLoop(self):
        self.app.mainloop()
    