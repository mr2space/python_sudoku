from .Constants import *
import os
import sys
import time
import copy
import pygame
import UI.sudokuGen as sudokuGen
import network.network as network
import threading
from math import floor


class Button:
    def __init__(self, text:str, x:int, y:int,width:int, height:int, color:tuple[int,int,int]) -> None:
        pygame.font.init()
        self.text = text
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    
    def draw(self, win:pygame.surface):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), border_radius=4)
        font = pygame.font.SysFont(FONT_NAME, 35)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2)-round(text.get_width()/2),self.y + round(self.height/2)-round(text.get_height()/2)))
    
    def click(self, pos:tuple[int,int]):
        x1 = pos[0]
        y1 = pos[1]
        if (self.x <= x1 <= self.x + self.width) and (self.y <= y1 <= self.y + self.height):
            return True
        else:
            return False



class Quit(Button):
    text = "Quit"
    color = COLOR_RED
    height = 50
    width = 150
    def __init__(self, pos: tuple[int, int]):
        self.x = pos[0]
        self.y = pos[1]



class Cell:
    def __init__(self, value:str, color:tuple[int, int, int], pos:tuple[int, int]) -> None:
        self.value = value
        self.RESETCOLOR = color
        self.SELECTCOLOR = (0,255,0)
        self.color = color
        self.is_selected = False
        self.button = Button(value, pos[0], pos[1], CELL_WIDTH, CELL_HEIGHT,self.color)
    
    def draw(self,win:pygame.Surface):
        self.win = win
        self.button.draw(win)
        
    def setValue(self, value:str):
        self.value = value
        self.button.text = str(value)
        
    def setColor(self, color:tuple[int, int, int]):
        # self.RESETCOLOR = self.color
        self.color = color
        self.button.color = color
    
    def click(self,pos:tuple[int, int]):
        flag = self.button.click(pos)
        if flag:
            self.setColor(COLOR_POPGREEN)
            self.draw(self.win)
            self.is_selected = True
        else:
            self.setColor(self.RESETCOLOR)
            self.draw(self.win)
            self.is_selected = False
    
    def key_input(self, event)->int:
        if self.is_selected == False:
            return self.value
        if event.key == pygame.K_1:
            return 1
        if event.key == pygame.K_2:
            return 2
        if event.key == pygame.K_3:
            return 3
        if event.key == pygame.K_4:
            return 4
        if event.key == pygame.K_5:
            return 5
        if event.key == pygame.K_6:
            return 6
        if event.key == pygame.K_7:
            return 7
        if event.key == pygame.K_8:
            return 8
        if event.key == pygame.K_9:
            return 9
        return 0




class Grid:
    def __init__(self, grid:list[list[int]], pos, win) -> None:
        self.original_grid = copy.deepcopy(grid)
        self.grid = grid
        self.cells:list[Cell] = [[None for i in range(9)] for j in range(9)]
        self.d = self.draw(pos, win)
        self.win:pygame.Surface = win
    
    def calcXPos(self, val, idx):
        padding = 5
        adjust = 0
        if idx % 3 == 0:
            padding = 8
        else:
            adjust = 8 * (idx // 3)
        return val+(CELL_WIDTH + padding)*idx + adjust
    
    def calcYPos(self, val, idx):
        padding = 5
        adjust = 0
        if idx % 3 == 0:
            padding = 8
        else:
            adjust = 8 * (idx // 3)
        return val+(CELL_HEIGHT + padding)*idx + adjust
    
    def draw(self,pos, win:pygame.Surface):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    self.cells[i][j] = Cell(" ", CELL_COLOR, (self.calcXPos(pos[0],i), self.calcYPos(pos[1], j)))
                else:
                    self.cells[i][j] = Cell(str(self.grid[i][j]), FILLCELL_COLOR, (self.calcXPos(pos[0], i), self.calcYPos(pos[1], j)))
                self.cells[i][j].draw(win)
                
    def decideColor(self, i:int, j:int)->tuple[int, int, int]:
        if sudokuGen.checkGameStatus(self.grid, i, j):
            return COLOR_BLUE
        return COLOR_RED
    
    def click(self,pos:tuple[int,int]):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].click(pos)
    
    def checkCellStatus(self):
        for i in range(9):
            for j in range(9):
                if (self.original_grid[i][j] != 0 ) or (self.grid[i][j] == 0):
                    continue
                cell_color = self.decideColor(i,j)
                self.cells[i][j].setColor(cell_color)
                self.cells[i][j].RESETCOLOR = cell_color
                self.cells[i][j].draw(self.win)
                
    def key_event(self, event):
        for i in range(9):
            for j in range(9):
                val = self.cells[i][j].key_input(event)
                if self.original_grid[i][j] != 0:
                    continue
                if val == " " or val == 0:
                    continue
                self.grid[i][j] = val or 0
                self.cells[i][j].setValue(val)
                self.cells[i][j].draw(self.win)
        self.checkCellStatus()
