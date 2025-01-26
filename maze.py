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
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self.num_cols):
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(self.win))
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        """
        (x1,y2)  (x2, y2)
        (x1,y1)  (x2, y1)
        """
        x1 = self.x1 + (i * self.cell_size_x)
        y2 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y1 = y2 + self.cell_size_y

        cell = self._cells[i][j]

        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        sleep(0)

    def _break_entrance_and_exit(self):
        if self._cells == []:
            return
        x = self.num_cols - 1
        y = self.num_rows - 1

        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[x][y].has_bottom_wall = False
        self._draw_cell(x, y)
