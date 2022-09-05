from operator import pos
import pygame
import requests


class StartWindow:
    def __init__(self, screen):
        self.screen = screen
        self.window_color = (101, 33, 255)
        self.widow_size = (920, 720)
        self.background_color = (101, 33, 255)
        self.font = pygame.font.SysFont('Agency FB', 50)
        screen.fill(self.background_color)
        logo = pygame.image.load("logo.png")
        loadingFont = pygame.font.SysFont('Agency FB', 20)
        screen.blit(logo, (400, 200))
        self.display()
        pygame.display.update()

    def display(self):
        self.startStatus = True
        pygame.display.update()
        while self.startStatus:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                self.button((415, 400), "EASY", self.clickEvent)
                self.button((415, 475),"MEDIUM",self.clickEvent)
                self.button((415, 550), "HARD", self.clickEvent)
                
            pygame.display.update()
        return 0

    def button(self, position, text, event, btn_color=(234, 229, 9)):
        call = event
        self.btn = pygame.Rect(
            position, (110, 40))
        pygame.draw.rect(screen, btn_color, self.btn, border_radius=10)
        font = pygame.font.SysFont('Agency FB', 23)
        text_surf = font.render(text, True,  "#000000")
        text_center = text_surf.get_rect(center=self.btn.center)
        screen.blit(text_surf, (text_center[0], text_center[1]-2))
        self.clickEvent(self.btn,text)

    def clickEvent(self,btn,text):
        print("in click")
        mouse_pos = pygame.mouse.get_pos()
        if btn.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                loading = WindowLayer()
                return self.buttonAction(text)
    def buttonAction(self,text):
        text = text.lower()
        response = requests.get(
            f"https://sugoku.herokuapp.com/board?difficulty={text}")
        self.startStatus = False
        

class Board:
    def __init__(self):
        self.grid_background = (0, 200, 151)
        self.grid_color = (0, 0, 0)
        self.filled_text = (0, 0, 0)
        self.filled_box_color = (234, 229, 9)
        self.user_text = (255, 255, 255)
        self.user_box_color = (19, 99, 223)
        self.padding = 3
        self.mistake_pos = []
        self.mistake_count = 0
        self.score = 0

    def sudokuGrid(self):
        for i in range(0, 10):
            self.width = 2
            if i % 3 == 0:
                self.width = 3
            pygame.draw.line(screen, self.grid_color, (40 + 70*i, 40),
                             (40 + 70*i, 670), self.width)
            pygame.draw.line(screen, self.grid_color, (40, 40 + 70*i),
                             (670, 40 + 70*i), self.width)
            
    def displayGameNumber(self):
        user_box_color = self.user_box_color
        for i in range(9):
            for j in range(9):
                number = grid[j][i]
                if 0 < number < 10:
                    value = font.render(str(number), True, self.user_text)
                    if grid_original[j][i] != 0:
                        pygame.draw.rect(
                            screen, self.filled_box_color, (40+70*j+self.padding, 40+70*i+self.padding, 70-self.padding, 70-self.padding))
                        value = font.render(
                            str(number), True, self.filled_text)
                        screen.blit(value, (70*j+70, 70*i+60))
                    else:
                        pygame.draw.rect(screen, user_box_color, (40+70 *
                                                                  j+self.padding, 40+70*i+self.padding, 70-self.padding, 70-self.padding))
                        screen.blit(value, (70*j+70, 70*i+60))
                    if (j, i) in self.mistake_pos:
                        pygame.draw.rect(
                            screen, (255, 0, 0), (40+70*j+self.padding, 40+70*i+self.padding, 70-self.padding, 70-self.padding))
                        value = font.render(
                            str(number), True, self.filled_text)
                        screen.blit(value, (70*j+70, 70*i+60))
                        
    def insertion(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return pygame.QUIT
                pos = pygame.mouse.get_pos()
                i, j = pos[0], pos[1]
                if i >= 680:
                    return True
                i, j = (i-40)//70, (j-40)//70
                pygame.draw.rect(screen, self.user_box_color, (40+70 *
                                                               i+self.padding, 40+70*j+self.padding, 70-self.padding, 70-self.padding))
                if event.type == pygame.KEYDOWN:
                    if grid_original[i][j] != 0:
                        return True
                    if event.key == 8:
                        grid[i][j] = 0
                        return True
                    if event.key >= 4 and event.key <= 57:
                        num = event.key - 48
                        grid[i][j] = event.key - 48
                        return [self.checking((i, j), num), (i, j)]

    def checking(self, position, num):
        if position in self.mistake_pos:
            try:
                self.mistake_pos.remove(position)
            except:
                pass
        #check row
        for i in range(len(grid[0])):
            if (grid[position[0]][i] == num) and i != position[1]:
                self.mistake_pos.append(position)
                self.mistake_count += 1
                return False
        #check col
        for i in range(len(grid[0])):
            if (grid[i][position[1]] == num) and i != position[0]:
                self.mistake_pos.append(position)
                self.mistake_count += 1
                return False

        #check sub-grid
        x = position[0] // 3
        y = position[0] // 3
        for i in range(0, 3):
            for j in range(0, 3):
                if (grid[x+i][y+i] == num) and (x+i) != position[0] and (y+i) != position[1]:
                    self.mistake_pos.append(position)
                    self.mistake_count += 1
                    return False
        self.score += 10
        return True

    def temp_displayIndex(self, event):
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            i = pygame.mouse.get_pos()[0]
            if i >= 680:
                return True
            value = self.insertion()
            self.displayGameNumber()
            pygame.display.update()
        return False
    def displayScore(self,grid):
        self.grid = grid
        text = font.render("SCORE",True,(255,255,255))
        rect = pygame.Rect((780, 250), (200, 200))
        pygame.draw.rect(screen, self.grid_background, rect)
        value = font.render(f"{self.score}", True, (255, 255, 255))
        screen.blit(text,(755,200))
        screen.blit(value,(780,250))
        self.displayMistake()
        self.button()
        
    def displayMistake(self):
        text = font.render("MISTAKE",True,(255,255,255))
        rect = pygame.Rect((780, 350), (200, 200))
        pygame.draw.rect(screen,self.grid_background,rect)
        value = font.render(f"{self.mistake_count}", True, (255, 255, 255))
        screen.blit(text,(755,300))
        screen.blit(value,(780,350))
        
    def button(self):
        self.btn = pygame.Rect(
            (735, 500), (110, 50))
        pygame.draw.rect(screen, (234, 229, 9), self.btn, border_radius=10)
        font = pygame.font.SysFont('Agency FB', 25)
        text_surf = font.render("Restart", True, (0, 0, 0))
        text_center = text_surf.get_rect(center=self.btn.center)
        screen.blit(text_surf, (text_center[0], text_center[1]-2))
        self.buttonClick()
    def buttonClick(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.btn.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return self.buttonAction()
        return [grid,False]
    def buttonAction(self):
        self.__init__()
        NewGame = WindowLayer()
        NewGame.loadNewGame()
        return True


class WindowLayer:
    def __init__(self):
        self.widow_size = (920,720)
        self.background_color = (101,33,255)
        screen.fill(self.background_color)
        logo = pygame.image.load("logo.png")
        loadingFont = pygame.font.SysFont('Agency FB',20)
        loading = loadingFont.render("Loading ...",True,(255,255,255))
        screen.blit(logo, (400, 200))
        screen.blit(loading,(445,350))
        pygame.display.update()
    
    def loadNewGame(self):
        global grid
        global grid_original
        grid = requests.get(
            "https://sugoku.herokuapp.com/board?difficulty=hard")
        grid = grid.json()['board']
        grid_original = [[grid[x][y] for y in range(9)] for x in range(9)]
        screen.fill(play.grid_background)
        play.displayGameNumber()


        


def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            return False
    return True


# getting sudoku game info from api4
global response
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
global grid
grid = response.json()['board']
grid_original = []
grid_original = [[grid[x][y] for y in range(9)] for x in range(9)]


# Intialize the pygame
pygame.init()
clock = pygame.time.Clock()
# game window
global screen
screen = pygame.display.set_mode((920, 720))
global running
running = True

# title and Logo
pygame.display.set_caption("Sudoku Awesome Game")
icon = pygame.image.load(r"resources\restaurant.png")
pygame.display.set_icon(icon)

# font and color
global font
font = pygame.font.SysFont('Agency FB', 30)
start = StartWindow(screen)
play = Board()



screen.fill(play.grid_background)
play.displayGameNumber()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        play.temp_displayIndex(event)
        play.displayScore(grid)
        play.sudokuGrid()
        pygame.display.update()
        clock.tick(60)
