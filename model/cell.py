from enum import Enum
import numpy as np

from pygame import Surface
from view.colors import Color

from view.spot import Spot


class CellType(Enum):
    WATER = 0
    EARTH = 1
    OIL_SOURCE = 2

class Cell:
    def __init__(self, type: CellType, cell_size: int, row: int, col: int) -> None:
        self.oil_level = 0
        self.type = type
        self.row = row
        self.col = col
        self.visual = Spot(row, col, cell_size)
        self.neighbours = np.empty(8, dtype=np.dtype(object)) # NW, N, NE ,E, SE, S ,SW ,W  - can be None
        self.update_color(self._get_color_by_type())

    def _get_color_by_type(self) -> Color:
        if self.type == CellType.WATER:
            return Color.blue
        return Color.tea_green


    def draw(self, window: Surface):
        self.visual.draw(window)

    def update_color(self, new_color: Color):
        self.visual.color = new_color 

    def update_neighbours(self, grid: np.ndarray):
        """Updates neighbours list with all spot's neighbours."""
        height, width = grid.shape

        bot_border = self.row == height - 1
        top_border = self.row == 0
        right_border = self.col == width - 1
        left_border = self.col == 0

        self.neighbours.fill(None)
        if not (top_border or left_border):  # NW
            self.neighbours[0] = grid[self.row - 1, self.col - 1]
        if not (top_border):                 # N
            self.neighbours[1] = grid[self.row - 1, self.col]
        if not (top_border or right_border): # NE
            self.neighbours[2] = grid[self.row - 1, self.col + 1]
        if not (right_border):               # E
            self.neighbours[3] = grid[self.row, self.col + 1]
        if not (bot_border or right_border): # SE
            self.neighbours[4] = grid[self.row + 1, self.col + 1]
        if not (bot_border):                 # S
            self.neighbours[5] = grid[self.row + 1, self.col]
        if not (bot_border or left_border):  # SW
            self.neighbours[6] = grid[self.row + 1, self.col - 1]
        if not (left_border):                # W
            self.neighbours[7] = grid[self.row, self.col - 1]
