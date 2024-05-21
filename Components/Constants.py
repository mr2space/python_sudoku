import os
import sys
import pygame

WIN_WIDTH:int = 800
WIN_HEIGHT:int = 700

CELL_WIDTH:int = 50
CELL_HEIGHT:int = 60

FONT_NAME:str = "Agency FB"

COLOR_NEWPURPLE:tuple[int, int, int]  = (108, 34, 166)
COLOR_BLUE:tuple[int, int, int] =(0, 121, 255)
COLOR_DARKBLUE:tuple[int, int, int] =  (41, 52, 98)
COLOR_RED:tuple[int, int, int] = (255, 0, 77)
COLOR_POPGREEN:tuple[int, int, int] = (73, 255, 0)

BACKGROUND_COLOR:tuple[int, int, int] = (30, 3, 66)
CELL_COLOR:tuple[int, int, int] = (255, 245, 224)
FILLCELL_COLOR:tuple[int, int, int] = (14, 70, 163)



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

IMG_PATH:str = r"imgs\—Pngtree—simple white background with blue_2338364.jpg"
BACK_IMG:pygame.Surface = pygame.image.load(resource_path(IMG_PATH))
BACK_IMG:pygame.Surface = pygame.transform.scale(BACK_IMG, (WIN_WIDTH, WIN_HEIGHT))
IMG_PATH:str = r"imgs\—Pngtree—simple white background with.jpg"
GAME_BACK_IMG:pygame.Surface = pygame.image.load(resource_path(IMG_PATH))
GAME_BACK_IMG = pygame.transform.scale(GAME_BACK_IMG, (WIN_WIDTH, WIN_HEIGHT))
IMG_PATH = r'imgs\leaves-8413064_1280.jpg'
WIN_BACKGROUND = pygame.image.load(resource_path(IMG_PATH))
WIN_BACKGROUND = pygame.transform.scale(WIN_BACKGROUND, (WIN_WIDTH, WIN_HEIGHT))
