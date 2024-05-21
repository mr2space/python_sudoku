import threading
from Components.Buttons import *
from Components.Constants import *
from Components.Labels import *
from abc import ABC, abstractmethod


class GameMode(ABC):
    grid_width = CELL_WIDTH*9 + 20
    grid_height = CELL_HEIGHT*9 + 20
    BoardPos = (int(WIN_WIDTH/100)*35 - int(grid_width/2), int(WIN_HEIGHT/100)*45 - int(grid_height/2))
    score = 60
    chance = 3
    boardColor = BACKGROUND_COLOR
    pos = (600, 100)
    quit = Quit((600, 500))
    thread_event = threading.Event()
    def check_win_status(self):
        count_zero = 0
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    count_zero += 1
                    return False
                if not sudokuGen.checkGameStatus(self.grid, i, j):
                    return False
        if count_zero == 0:
            return True
        return False
    def win_panel(self):
        self.win.fill(COLOR_DARKBLUE)
        self.win.blit(WIN_BACKGROUND, (0,0))
        label = Label(self.win,(7 * 45, 5*50 ), COLOR_DARKBLUE, "You won")
        self.thread_event.set()
        pygame.display.update()
        time.sleep(5)
        del label
        return None
    
    def loss_panel(self):
        self.win.fill(COLOR_DARKBLUE)
        self.win.blit(WIN_BACKGROUND, (0,0))
        label = Label(self.win,(7 * 45, 5*50 ), COLOR_DARKBLUE, "You lost")
        self.thread_event.set()
        pygame.display.update()
        time.sleep(5)
        del label
        return None
    
    @abstractmethod
    def main(self):
        ...
    
class OfflineGameMode(GameMode):
    def __init__(self, win:pygame.Surface) -> None:
        self.grid = sudokuGen.SudoGrid().getGrid()
        print(win)
        self.win = win
    
    def main(self):
        clk = Time(self.win, (600,100), BACKGROUND_COLOR, "Time", self.thread_event)
        run = True
        self.win.fill(self.boardColor)
        self.win.blit(GAME_BACK_IMG, (0,0))
        clock = pygame.time.Clock();
        g = Grid(self.grid, self.BoardPos, self.win)
        timeThread = threading.Thread(target = clk.show_time, args=())
        timeThread.start()
        while run:
            clock.tick(60)
            self.quit.draw(self.win)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    g.click(pos)
                    if self.quit.click(pos):
                        self.thread_event.set()
                        return None
                if event.type == pygame.KEYDOWN:
                    g.key_event(event)
                if self.check_win_status():
                    self.win_panel()
                    return None
            pygame.display.update()
        
   
class OnlineGameMode(GameMode):
    def __init__(self, win:pygame.Surface, game_id, player_id) -> None:
        ...
        
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
                self.loss_panel()
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
                    self.win_panel()
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
    
    def option_online(self):
        ...
        
    def option_offline(self):
        self.offlineMode = OfflineGameMode(self.win)
        self.offlineMode.main()
        del self.offlineMode
        self.__init__(self.win)
        self.draw()
    
    def click(self, pos:tuple[int, int]):
        if self.online.click(pos):
            self.option_online()
        elif self.offline.click(pos):
            self.option_offline()
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
            
    
    