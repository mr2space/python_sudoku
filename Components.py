import time
import copy
import pygame
import sudokuGen
import network
from math import floor

WIN_WIDTH:int = 800
WIN_HEIGHT:int = 700

CELL_WIDTH:int = 50
CELL_HEIGHT:int = 60

FONT_NAME:str = "Agency FB"

COLOR_NEWPURPLE:tuple[int, int, int]  = (108, 34, 166)
COLOR_BLUE:tuple[int, int, int] =(0, 121, 255)
COLOR_DARKBLUE:tuple[int, int, int] =  (41, 52, 98)
COLOR_RED:tuple[int, int, int] = (255, 0, 77)
COLOR_POPGREEN:tuple[int, int, int] = (73, 255, 0)

BACKGROUND_COLOR:tuple[int, int, int] = (30, 3, 66)
CELL_COLOR:tuple[int, int, int] = (255, 245, 224)
FILLCELL_COLOR:tuple[int, int, int] = (14, 70, 163)

IMG_PATH:str = r"Multiplayer_sudoku\—Pngtree—simple white background with blue_2338364.jpg"
BACK_IMG:pygame.Surface = pygame.image.load(IMG_PATH)
BACK_IMG:pygame.Surface = pygame.transform.scale(BACK_IMG, (WIN_WIDTH, WIN_HEIGHT))

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
        
    def setValue(self, value:str):
        self.value = value
        self.button.text = str(value)
        
    def setColor(self, color:tuple[int, int, int]):
        # self.RESETCOLOR = self.color
        self.color = color
        self.button.color = color
    
    def click(self,pos:tuple[int, int]):
        flag = self.button.click(pos)
        if flag:
            self.setColor(COLOR_POPGREEN)
            self.draw(self.win)
            self.is_selected = True
        else:
            self.setColor(self.RESETCOLOR)
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
        return 0



class Grid:
    def __init__(self, grid:list[list[int]], pos, win) -> None:
        self.original_grid = copy.deepcopy(grid)
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
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.cells[i][j] = Cell(" ", CELL_COLOR, (self.calcXPos(pos[0],i), self.calcYPos(pos[1], j)))
                else:
                    self.cells[i][j] = Cell(str(self.grid[i][j]), FILLCELL_COLOR, (self.calcXPos(pos[0], i), self.calcYPos(pos[1], j)))
                self.cells[i][j].draw(win)
                
    def decideColor(self, i:int, j:int)->tuple[int, int, int]:
        if sudokuGen.checkGameStatus(self.grid, i, j):
            return COLOR_BLUE
        return COLOR_RED
    
    def click(self,pos:tuple[int,int]):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].click(pos)
    
    def checkCellStatus(self):
        for i in range(9):
            for j in range(9):
                if (self.original_grid[i][j] != 0 ) or (self.grid[i][j] == 0):
                    continue
                cell_color = self.decideColor(i,j)
                self.cells[i][j].setColor(cell_color)
                self.cells[i][j].RESETCOLOR = cell_color
                self.cells[i][j].draw(self.win)
                
    def key_event(self, event):
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].key_input(event)
                if self.original_grid[i][j] != 0:
                    continue
                if val == " " or val == 0:
                    continue
                self.grid[i][j] = val or 0
                self.cells[i][j].setValue(val)
                self.cells[i][j].draw(self.win)
        self.checkCellStatus()


class Time:
    def __init__(self, pos:tuple[int, int], color:tuple[int, int, int]) -> None:
        self.time = floor(time.time())
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
    
    def setTime(self):
        self.time = floor(time.time() - self.time)
    
    def draw(self, win):
        # self.text = Button("Time: ", self.x, self.y, 100, 55, self.color)
        self.button = Button(str(self.time), self.x, self.y, 100, 55, self.color)
        self.setTime()
        self.button.draw(win)
        # self.text.draw(win)

class Label:
    def __init__(self,text:str,value:int, pos:tuple[int, int], color:tuple[int, int, int]) -> None:
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.text = text
        self.value = value
        
    def setValue(self, value):
        self.value = value
    
    def draw(self, win):
        self.text = Button("Time: ", self.x, self.y, 200, 55, self.color)
        self.button = Button(str(self.value + 9999), self.x+220, self.y, 200, 55, self.color)
        self.button.draw(win)
        self.text.draw(win)
    




     
class OfflineGameMode:
    def __init__(self, win:pygame.Surface) -> None:
        self.grid = sudokuGen.SudoGrid().getGrid()
        grid_width = CELL_WIDTH*9 + 20
        grid_height = CELL_HEIGHT*9 + 20
        self.BoardPos = (int(WIN_WIDTH/100)*50 - int(grid_width/2), int(WIN_HEIGHT/100)*50 - int(grid_height/2))
        self.win = win
        self.score = 00
        self.chance = 3
        self.boardColor = BACKGROUND_COLOR
        pos = (600, 100)
        self.time = Time(pos,self.boardColor)
        
    def checkWinStatus(self):
        countZero = 0
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    countZero += 1
        if countZero == 0:
            return True
        return False
    
    def WinPanel(self):
        self.win.fill(COLOR_DARKBLUE)
        Btn = Button("You won", 7 * 40, 5*20, 400, 40, COLOR_DARKBLUE)
        Btn.draw(self.win)
        pygame.display.update()
        time.sleep(5)
        del Btn
        return None
    
     
    def main(self):
        run = True
        self.win.fill(self.boardColor)
        clock = pygame.time.Clock();
        g = Grid(self.grid, self.BoardPos, self.win)
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    g.click(pos)
                if event.type == pygame.KEYDOWN:
                    g.key_event(event)
                if self.checkWinStatus():
                    self.WinPanel()
                    return None
            pygame.display.update()
        
        
class OnlineGameMode(OfflineGameMode):
    def __init__(self, win:pygame.Surface) -> None:
        ...
    
    def LosePanel(self):
        self.win.fill(COLOR_DARKBLUE)
        Btn = Button("You lost", 7 * 40, 5*20, 400, 40, COLOR_DARKBLUE)
        Btn.draw(self.win)
        pygame.display.update()
        time.sleep(5)
        del Btn
        return None
        
    def main(self):
        run = True
        self.win.fill(self.boardColor)
        clock = pygame.time.Clock();
        g = Grid(self.grid,(10,10), self.win)
        net = network.Network()
        opponentG = net.send(g) or False
        while run:
            clock.tick(60)
            opponentG = net.send(g) or False
            if opponentG:
                self.LosePanel()
                return None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    g.click(pos)
                if event.type == pygame.KEYDOWN:
                    g.key_event(event)
                if self.checkWinStatus():
                    self.WinPanel()
                    return None
            pygame.display.update()
          


class Menu:
    def __init__(self, win:pygame.Surface) -> None:
        self.pos:tuple[int, int] = (5,7)
        self.win = win 
        self.win.fill((255, 255, 255))
        self.win.blit(BACK_IMG, (0,0))
        self.online = Button("MultiPlayer", (WIN_WIDTH/100)*50 - 75, (WIN_HEIGHT/100)*45, 150, 55, COLOR_BLUE)
        self.offline = Button("Offline", (WIN_WIDTH/100)*50 - 75, (WIN_HEIGHT/100)*55, 150, 55, COLOR_NEWPURPLE)
        
    def draw(self):
        self.online.draw(self.win)
        self.offline.draw(self.win)
    
    
    def optionOnline(self):
        ...
    
    def optionOffline(self):
        self.offlineMode = OfflineGameMode(self.win)
        self.offlineMode.main()
        del self.offlineMode
        self.__init__(self.win)
        self.draw()
        
    def click(self, pos:tuple[int, int]):
        if self.online.click(pos):
            self.optionOnline()
        elif self.offline.click(pos):
            self.optionOffline()
        else:
            return None
        
    def main(self):
        run = True
        clock = pygame.time.Clock();
        self.draw()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.click(pos)
                if event.type == pygame.KEYDOWN:
                    ...
            pygame.display.update()
            