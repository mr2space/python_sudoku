import copy
import pygame
import sudokuGen

FONT_NAME:str = "Agency FB"
CELL_WIDTH:int = 50
CELL_HEIGHT:int = 60
COLOR_YELLOW:tuple[int, int, int] = (234, 229, 9)
COLOR_GREEN:tuple[int, int, int] = (141, 236, 180) #(0, 223, 162)
COLOR_PURPLE:tuple[int, int, int] = (101, 33, 255)
COLOR_BLUE:tuple[int, int, int] =(0, 121, 255)
COLOR_DARKBLUE:tuple[int, int, int] =  (41, 52, 98)
COLOR_RED:tuple[int, int, int] = (255, 0, 77)
COLOR_POPGREEN:tuple[int, int, int] = (73, 255, 0)

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
        print(self.grid)
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.cells[i][j] = Cell(" ", COLOR_GREEN, (self.calcXPos(pos[0],i), self.calcYPos(pos[1], j)))
                else:
                    self.cells[i][j] = Cell(str(self.grid[i][j]), COLOR_DARKBLUE, (self.calcXPos(pos[0], i), self.calcYPos(pos[1], j)))
                self.cells[i][j].draw(win)
                
    def decideColor(self, i:int, j:int)->tuple[int, int, int]:
        if sudokuGen.checkGameStatus(self.grid, i, j):
            print("yes for i, j", i,j, self.grid[i][j])
            return COLOR_BLUE
        print("No for i, j", i,j, self.grid[i][j])
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
        self.time = 0
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
    
    def setTime(self):
        self.time += 1
    
    def draw(self, win):
        self.text = Button("Time: ", self.x, self.y, 200, 55, self.color)
        self.button = Button(str(self.time), self.x+220, self.y, 200, 55, self.color)
        self.button.draw(win)
        self.text.draw(win)

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
        self.button = Button(str(self.value), self.x+220, self.y, 200, 55, self.color)
        self.button.draw(win)
        self.text.draw(win)
    

    


     
class OfflineGameMode:
    def __init__(self, win:pygame.Surface) -> None:
        self.grid = sudokuGen.SudoGrid().getGrid()
        self.BoardPos = (10, 10)
        self.win = win
        self.Grid = Grid(self.grid, self.BoardPos, self.win)
        self.score = 00
        self.chance = 3
        self.boardColor = COLOR_PURPLE
    
    def manageTime(self):
        pos = (400, 100)
        self.time = Time(pos,self.boardColor)
        self.time.draw(self.win)
    
    def incrementScore(self):
        self.score += 10
    
    def manageScore(self):
        self.score = 0
        pos = (400, 300)
        self.Score = Label("Score", self.score, pos, self.boardColor)
        self.Score.draw(self.win)
        
     
    def main(self):
        run = True
        self.win.fill(self.boardColor)
        clock = pygame.time.Clock();
        btn = Button("hello", 100, 100, 75, 50, (255,00,0))
        g = Grid(self.grid,(10,10), self.win)
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
            pygame.display.update()
        
        
            


class Menu:
    def __init__(self, win:pygame.Surface) -> None:
        self.pos:tuple[int, int] = (5,7)
        self.win = win 
        self.win.fill((255, 255, 255))
        self.online = Button("MultiPlayer", 5*40, 7*40, 150, 55, COLOR_BLUE)
        self.offline = Button("offline", 5*40, 7*60, 150, 55, COLOR_GREEN)
        
    def draw(self):
        self.online.draw(self.win)
        self.offline.draw(self.win)
    
    def optionOnline(self):
        ...
    
    def optionOffline(self):
        self.grid = sudokuGen.SudoGrid().getGrid()
        g = Grid(self.grid, (10, 10), self.win)
        g.main()
        del g
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
            