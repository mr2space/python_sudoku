
import pygame
import requests

# getting sudoku game info from api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = []
grid_original.extend(grid) 
print(grid)


# Intialize the pygame
pygame.init()

# game window
screen = pygame.display.set_mode((720,720))


# title and Logo
pygame.display.set_caption("Sudoku Awesome Game")
icon = pygame.image.load(r"resources\restaurant.png")
pygame.display.set_icon(icon)

# font and color
font = pygame.font.SysFont('Agency FB',30)

def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def sudokuGrid():
    for i in range(0,10):
        width = 1
        if i % 3 == 0:
            width = 2
        pygame.draw.line(screen, (0, 0, 0), (40 + 70*i, 40), (40 + 70*i, 670),width)
        pygame.draw.line(screen, (0, 0, 0), (40,40 + 70*i), (670,40 + 70*i),width)
        width = 1


def displayGameNumber():
    for i in range(9):
        for j in range(9):
            number = grid[j][i]
            if 0 < number < 10:
                value = font.render(str(number),True,(255,0,0))
                screen.blit(value, (70*j+70, 70*i+60))


        
class UserInput:
    def temp_displayIndex(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button ==1:
                pos = pygame.mouse.get_pos()
                i, j = pos[0], pos[1]
                self.i,self.j = (i-40)//70, (j-40)//70
                print("its in input error")
                self.insertion()
                return i,j
    def insertion(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.quit()
                if event.type == pygame.KEYDOWN:
                    print(grid[self.i][self.j],"grid value")
                    if grid[self.i][self.j] != 0:
                        return None
                    if event.key > 48:
                        print("in if 2",event.key-48,event.key)
                        grid[self.i][self.j] = event.key - 48 
                        print("hello",grid)
                        return



insert = UserInput()
running = True
while running:
    running = quitGame()
    screen.fill((255,255,255))
    sudokuGrid()
    displayGameNumber()
    insert.temp_displayIndex()
    pygame.display.update()