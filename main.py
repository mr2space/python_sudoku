
import pygame
import requests

# getting sudoku game info from api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = []
grid_original = [[grid[x][y] for y in range(9)] for x in range(9)] 
print(grid_original)

#global varibles
grid_background = (14, 24, 95)
grid_color = (255,255,255)
filled_text = (0,0,255)
user_text = (0,255,0)



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
        pygame.draw.line(screen, (225, 255, 238),
                         (40 + 70*i, 40), (40 + 70*i, 670), width)
        pygame.draw.line(screen, (225, 255, 238),
                         (40, 40 + 70*i), (670, 40 + 70*i), width)
        width = 1


def displayGameNumber():
    for i in range(9):
        for j in range(9):
            number = grid[j][i]
            if 0 < number < 10:
                value = font.render(str(number),True,(255,0,0))
                if grid_original[j][i] != 0:
                    value = font.render(str(number), True, (0, 0, 0))
                screen.blit(value, (70*j+70, 70*i+60))
   
def temp_displayIndex():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP and event.button ==1:
            pos = pygame.mouse.get_pos()
            i, j = pos[0], pos[1]
            i,j = (i-40)//70, (j-40)//70
            print("its in input error")
            return insertion(i,j)

def insertion(i,j):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
            if event.type == pygame.KEYDOWN:
                print(grid[i][j],"grid value")
                if grid_original[i][j] != 0:
                    return None
                if event.key == 8:grid[i][j] = 0
                if event.key >= 48:
                    print("in if 2",event.key-48,event.key)
                    grid[i][j] = event.key - 48 
                    print("hello",grid)
                    return True



running = True
while running:
    running = quitGame()
    screen.fill((22, 33, 62))
    sudokuGrid()
    displayGameNumber()
    temp_displayIndex()
    pygame.display.update()