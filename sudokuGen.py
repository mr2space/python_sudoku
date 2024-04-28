from dokusan import generators
import numpy as np


class SudoGrid:
    def __init__(self) -> None:
        self.puzzle_string = np.array(list(str(generators.random_sudoku())))
        vector_function = np.vectorize(int)
        self.puzzle_string = vector_function(self.puzzle_string)
        self.np_grid = self.puzzle_string.reshape(9,9)
        self.grid = self.np_grid.tolist()
    
    def getGrid(self):
        return self.grid
    


def checkGameStatus(grid:list[list[int]], i:int, j:int)->bool:
    val = grid[i][j]
    for idx in range(9):
        if idx == j:
            continue
        if grid[i][idx] == val:
            return False
    for idx in range(9):
        if idx == i:
            continue
        if grid[idx][j] == val:
            return False
    x = i // 3
    y = j // 3
    for idx in range(3):
        for idy in range(3):
            if (x + idx) == i and (y + idy) == j:
                continue
            if grid[x+idx][y+idy] == val:
                return False
    return True

    
    