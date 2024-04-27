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