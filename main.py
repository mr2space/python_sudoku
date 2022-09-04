from operator import pos
import pygame
import requests


class StartWindow:
    def __init__(self, screen, grid_background):
        self.screen = screen
        self.width = 720
        self.height = 720
        self.window_color = grid_background
        self.font = pygame.font.SysFont('Agency FB', 50)

    def display(self):
        self.rect = pygame.Rect((0, 0), (self.width, self.height))
        self.text_surf = self.font.render("sudoku", True, filled_box_color)
        self.text_center = self.text_surf.get_rect(center=self.rect.center)
        pygame.draw.rect(screen, self.window_color, self.rect)
        self.screen.blit(
            self.text_surf, (self.text_center[0]-10, self.text_center[1]-20))

        self.button()
        self.clickEvent()
        return 0

    def button(self):
        self.btn = pygame.Rect(
            (self.text_center[0]-10, self.text_center[1]+100), (110, 50))
        pygame.draw.rect(screen, (234, 229, 9), self.btn, border_radius=15)
        font = pygame.font.SysFont('Agency FB', 25)
        text_surf = font.render("start", True, (0, 0, 0))
        text_center = text_surf.get_rect(center=self.btn.center)
        self.screen.blit(text_surf, (text_center[0], text_center[1]-2))

    def clickEvent(self):
        mouse_pos = pygame.mouse.get_pos()
        pass


class Board:
    #User interface varibles
    grid_background = (0, 200, 151)
    grid_color = (0, 0, 0)
    filled_text = (0, 0, 0)
    filled_box_color = (234, 229, 9)
    user_text = (255, 255, 255)
    user_box_color = (19, 99, 223)
    padding = 3
    #mistake variable
    mistake_pos = []
    mistake_count = 0
    
    #score Count
    score = 0
    def sudokuGrid(self):
        for i in range(0, 10):
            self.width = 2
            if i % 3 == 0:
                self.width = 3
            pygame.draw.line(screen, self.grid_color, (40 + 70*i, 40),
                             (40 + 70*i, 670), self.width)
            pygame.draw.line(screen, self.grid_color, (40, 40 + 70*i),
                             (670, 40 + 70*i), self.width)

    def displayGameNumber(self, user_box_color=user_box_color):
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
                        print("checked for error", i, j)
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
        print("in checking ")
        print(self.mistake_pos)
        if position in self.mistake_pos:
            try:
                self.mistake_pos.remove(position)
            except:
                print("hello world")
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
            value = self.insertion()
            self.displayGameNumber()
            pygame.display.update()
        return False
    def displayScore(self):
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
        pygame.draw.rect(screen, (234, 229, 9), self.btn, border_radius=15)
        font = pygame.font.SysFont('Agency FB', 25)
        text_surf = font.render("Restart", True, (0, 0, 0))
        text_center = text_surf.get_rect(center=self.btn.center)
        screen.blit(text_surf, (text_center[0], text_center[1]-2))



def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            return False
    return True


# getting sudoku game info from api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
grid = response.json()['board']
grid_original = []
grid_original = [[grid[x][y] for y in range(9)] for x in range(9)]


# Intialize the pygame
pygame.init()
clock = pygame.time.Clock()
# game window
global screen
screen = pygame.display.set_mode((920, 720))


# title and Logo
pygame.display.set_caption("Sudoku Awesome Game")
icon = pygame.image.load(r"resources\restaurant.png")
pygame.display.set_icon(icon)

# font and color
global font
font = pygame.font.SysFont('Agency FB', 30)

play = Board()

start = StartWindow(screen, play.grid_background)


global running
running = True
screen.fill(play.grid_background)
play.displayGameNumber()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        play.temp_displayIndex(event)
        play.displayScore()
        play.sudokuGrid()
        # start.display()
        pygame.display.update()
        clock.tick(60)

