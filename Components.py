from math import floor
import pygame

FONT_NAME:str = "Agency FB"
CELL_WIDTH:int = 45
CELL_HEIGHT:int = 60
COLOR_YELLOW:tuple[int, int, int] = (234, 229, 9)
COLOR_GREEN:tuple[int, int, int] = (0, 223, 162)
COLOR_PURPLE:tuple[int, int, int] = (101, 33, 255)
COLOR_BLUE:tuple[int, int, int] = (41, 52, 98)

class Button:
    def __init__(self, text:str, x:int, y:int,width:int, height:int, color:tuple[int,int,int]) -> None:
        pygame.font.init()
        self.text = text
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def draw(self, win:pygame.surface):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont(FONT_NAME, 35)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2)-round(text.get_width()/2),self.y + round(self.height/2)-round(text.get_height()/2)))
    
    def click(self, pos:tuple[int,int]):
        x1 = pos[0]
        y1 = pos[1]
        if (self.x <= x1 <= self.x + self.width) and (self.y <= y1 <= self.y + self.height):
            return True
        else:
            return False


class Cell:
    def __init__(self, value:str, color:tuple[int, int, int], pos:tuple[int, int]) -> None:
        self.value = value
        self.RESETCOLOR = color
        self.SELECTCOLOR = (0,255,0)
        self.color = color
        self.is_selected = False
        self.button = Button(value, pos[0], pos[1], CELL_WIDTH, CELL_HEIGHT,self.color)
    
    def draw(self,win:pygame.Surface):
        self.win = win
        self.button.draw(win)
        
    def setValue(self, value):
        self.value = value
        self.button.text = str(value)
    
    def updatedDraw(self, win:pygame.Surface, val):
        self.button.text = str(val)
        self.button.draw(self.win)
    
    def click(self,pos:tuple[int, int]):
        flag = self.button.click(pos)
        if flag:
            self.color = self.SELECTCOLOR
            self.button.color = self.color
            self.draw(self.win)
            self.is_selected = True
        else:
            self.color = self.RESETCOLOR
            self.button.color = self.color
            self.draw(self.win)
            self.is_selected = False
    
    def key_input(self, event)->int:
        if self.is_selected == False:
            return self.value
        if event.key == pygame.K_1:
            return 1
        if event.key == pygame.K_2:
            return 2
        if event.key == pygame.K_3:
            return 3
        if event.key == pygame.K_4:
            return 4
        if event.key == pygame.K_5:
            return 5
        if event.key == pygame.K_6:
            return 6
        if event.key == pygame.K_7:
            return 7
        if event.key == pygame.K_8:
            return 8
        if event.key == pygame.K_9:
            return 9
        



class Grid:
    def __init__(self, grid:list[list[int]], pos, win) -> None:
        self.grid = grid
        self.cells:list[Cell] = [[None for i in range(9)] for j in range(9)]
        self.d = self.draw(pos, win)
        self.win:pygame.Surface = win
    
    def calcXPos(self, val, idx):
        padding = 5
        adjust = 0
        if idx % 3 == 0:
            padding = 8
        else:
            adjust = 8 * (idx // 3)
        return val+(CELL_WIDTH + padding)*idx + adjust
    
    def calcYPos(self, val, idx):
        padding = 5
        adjust = 0
        if idx % 3 == 0:
            padding = 8
        else:
            adjust = 8 * (idx // 3)
        return val+(CELL_HEIGHT + padding)*idx + adjust
    
    def draw(self,pos, win:pygame.Surface):
        print(self.grid)
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.cells[i][j] = Cell(" ", COLOR_GREEN, (self.calcXPos(pos[0],i), self.calcYPos(pos[1], j)))
                else:
                    self.cells[i][j] = Cell(str(self.grid[i][j]), COLOR_YELLOW, (self.calcXPos(pos[0], i), self.calcYPos(pos[1], j)))
                self.cells[i][j].draw(win)
    
    def click(self,pos:tuple[int,int]):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].click(pos)
    def key_event(self, event):
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].key_input(event)
                self.cells[i][j].SetValue(val)
                self.cells[i][j].draw(self.win)
                if val == 0:
                    continue
                self.grid[i][j] = val
        
        
        
        
            
    