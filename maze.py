from wall import Cell
from time import sleep


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        """
        (x1,y2)  (x2, y2)
        (x1,y1)  (x2, y1)
        """
        x1 = self.x1 + (i * self.cell_size_x)
        y2 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y1 = y2 + self.cell_size_y

        cell = Cell(self.win)

        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        sleep(0.1)
