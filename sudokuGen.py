from dokusan import generators
import numpy as np


class SudoGrid:
    def __init__(self) -> None:
        self.puzzle_string = np.array(list(str(generators.random_sudoku(100))))
        vector_function = np.vectorize(int)
        self.puzzle_string = vector_function(self.puzzle_string)
        self.np_grid = self.puzzle_string.reshape(9,9)
        self.grid = self.np_grid.tolist()
    
    def getGrid(self):
        return self.grid
    


def checkGameStatus(grid:list[list[int]], i:int, j:int)->bool:
    num = grid[i][j]
    grid[i][j] = 0
    row = i
    col = j
    board = grid
    if num == " " or num == 0 :
        return False
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                grid[row][col] = num
                return False
    grid[row][col] = num
    return True

    
    