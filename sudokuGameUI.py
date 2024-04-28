import pygame
import Components
import sudokuGen

COLOR_PURPLE:tuple[int, int, int] = (101, 33, 255)
WIN_WIDTH:int = 800
WIN_HEIGHT:int = 700

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku")

icon = pygame.image.load(r"Multiplayer_sudoku\grid.png")
pygame.display.set_icon(icon)


clientNumber = 0
Gen = sudokuGen.SudoGrid()
grid = Gen.getGrid()

Menu = Components.Menu(win)
try:
    Menu.main()
except:
    pass
