import pygame
import requests

# getting sudoku game info from api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
grid = response.json()['board']
grid_original = []
grid_original = [[grid[x][y] for y in range(9)] for x in range(9)]

#User interface varibles
grid_background = (0, 200, 151)
grid_color = (0, 0, 0)
filled_text = (0, 0, 0)
filled_box_color = (234, 229, 9)
user_text = (255, 255, 255)
user_box_color = (19, 99, 223)
padding = 3

# Intialize the pygame
pygame.init()

# game window
screen = pygame.display.set_mode((720, 720))


# title and Logo
pygame.display.set_caption("Sudoku Awesome Game")
icon = pygame.image.load(r"resources\restaurant.png")
pygame.display.set_icon(icon)

# font and color
font = pygame.font.SysFont('Agency FB', 30)

def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            return False
    return True


def sudokuGrid():
    for i in range(0, 10):
        width = 2
        if i % 3 == 0:
            width = 3
        pygame.draw.line(screen, grid_color, (40 + 70*i, 40),
                         (40 + 70*i, 670), width)
        pygame.draw.line(screen, grid_color, (40, 40 + 70*i),
                         (670, 40 + 70*i), width)
        width = 1


def displayGameNumber():
    for i in range(9):
        for j in range(9):
            number = grid[j][i]
            if 0 < number < 10:
                value = font.render(str(number), True, user_text)
                if grid_original[j][i] != 0:
                    pygame.draw.rect(
                        screen, filled_box_color, (40+70*j+padding, 40+70*i+padding, 70-padding, 70-padding))
                    value = font.render(str(number), True, filled_text)
                    screen.blit(value, (70*j+70, 70*i+60))
                else:
                    pygame.draw.rect(screen, user_box_color, (40+70 *
                                                              j+padding, 40+70*i+padding, 70-padding, 70-padding))
                    screen.blit(value, (70*j+70, 70*i+60))


def temp_displayIndex(event):
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        insertion()
        displayGameNumber()
        pygame.display.update()
    return False


def insertion():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return pygame.QUIT
            pos = pygame.mouse.get_pos()
            i, j = pos[0], pos[1]
            i, j = (i-40)//70, (j-40)//70
            pygame.draw.rect(screen, user_box_color, (40+70 *
                             i+padding, 40+70*j+padding, 70-padding, 70-padding))
            if event.type == pygame.KEYDOWN:
                print(grid[i][j], "grid value")
                if grid_original[i][j] != 0:
                    return None
                if event.key == 8:
                    grid[i][j] = 0
                    return None
                if event.key >= 4 and event.key <= 57:
                    grid[i][j] = event.key - 48
                    print(grid)
                    return True

def checking(i,j):
    pass


global running 
running = True
screen.fill(grid_background)
displayGameNumber()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        print('its here')
        temp_displayIndex(event)
        sudokuGrid()
        pygame.display.update()
