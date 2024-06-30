import os
import sys
import pygame
import GameMode
import sudokuGen

COLOR_PURPLE:tuple[int, int, int] = (101, 33, 255)
WIN_WIDTH:int = 800
WIN_HEIGHT:int = 700

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

icon = pygame.image.load(resource_path(r"imgs\grid.png"))
pygame.display.set_icon(icon)


clientNumber = 0
Gen = sudokuGen.SudoGrid()
grid = Gen.getGrid()

Menu = GameMode.Menu(win)
try:
    Menu.main()
except:
    pass

