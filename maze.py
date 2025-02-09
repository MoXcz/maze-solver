from wall import Cell
from time import sleep
import random


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
        seed=None,
        speed=0.05,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.speed = speed
        self._create_cells()
        self._break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self.num_cols):
            self._cells.append([])
            for cell in range(self.num_rows):
                self._cells[col].append(Cell(self.win))
                self._draw_cell(col, cell)

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
        sleep(self.speed)

    def _break_entrance_and_exit(self):
        if self._cells == []:
            return
        x = self.num_cols - 1
        y = self.num_rows - 1

        self._cells[0][0].has_top_wall = False  # Entrance
        self._draw_cell(0, 0)

        self._cells[x][y].has_bottom_wall = False  # Exit
        self._draw_cell(x, y)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            coordinates = []
            if i > 0 and self._cells[i - 1][j].visited is False:
                coordinates.append([i - 1, j])  # left
            if i < self.num_cols - 1 and self._cells[i + 1][j].visited is False:
                coordinates.append([i + 1, j])  # right
            if j > 0 and self._cells[i][j - 1].visited is False:
                coordinates.append([i, j - 1])  # top
            if j < self.num_rows - 1 and self._cells[i][j + 1].visited is False:
                coordinates.append([i, j + 1])  # bottom

            if coordinates == []:
                self._draw_cell(i, j)
                return

            r_cell = random.randint(0, len(coordinates) - 1)

            adjacent_x = coordinates[r_cell][0]
            adjacent_y = coordinates[r_cell][1]
            chosen_cell = self._cells[adjacent_x][adjacent_y]
            if adjacent_x > i:  # right
                chosen_cell.has_left_wall = False
                current_cell.has_right_wall = False
            if adjacent_x < i:  # left
                chosen_cell.has_right_wall = False
                current_cell.has_left_wall = False
            if adjacent_y > j:  # bottom
                chosen_cell.has_top_wall = False
                current_cell.has_bottom_wall = False
            if adjacent_y < j:  # top
                chosen_cell.has_bottom_wall = False
                current_cell.has_top_wall = False
            self._break_walls_r(adjacent_x, adjacent_y)

    def _reset_cells_visited(self):
        for col in range(self.num_cols):
            for cell in range(self.num_rows):
                self._cells[col][cell].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if current_cell == self._cells[-1][-1]:  # the end
            return True

        if (
            i > 0
            and self._cells[i - 1][j].visited is False
            and current_cell.has_left_wall is False
        ):  # left
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            current_cell.draw_move(self._cells[i - 1][j], True)
        if (
            i < self.num_cols - 1
            and self._cells[i + 1][j].visited is False
            and current_cell.has_right_wall is False
        ):  # right
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            current_cell.draw_move(self._cells[i + 1][j], True)
        if (
            j > 0
            and self._cells[i][j - 1].visited is False
            and current_cell.has_top_wall is False
        ):  # top
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            current_cell.draw_move(self._cells[i][j - 1], True)
        if (
            j < self.num_rows - 1
            and self._cells[i][j + 1].visited is False
            and current_cell.has_bottom_wall is False
        ):  # bottom
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            current_cell.draw_move(self._cells[i][j + 1], True)
        return False
