
import pygame
import requests

# getting sudoku game info from api
response = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
grid = response.json()['board']
grid_original = []
grid_original.extend(grid) 

# Intialize the pygame

pygame.init()
# hello
# game window
# some new things
screen = pygame.display.set_mode((720,720))


# title and Logo
pygame.display.set_caption("Sudoku Awesome Game")
icon = pygame.image.load(r"Include\resources\restaurant.png")
pygame.display.set_icon(icon)


def 


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



running = True
while running:
    running = quitGame()
    screen.fill((255,255,255))
    sudokuGrid()
    pygame.display.update()