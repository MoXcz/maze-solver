from window import Line, Point


class Cell:
    def __init__(self, win=None, left=True, right=True, top=True, bottom=True):
        self._win = win
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None

    def draw(self, x1, y1, x2, y2):
        """
        p1(x1,y2)  p2(x2, y2)
        p3(x1,y1)  p4(x2, y1)
        """
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        p1 = Point(x1, y2)
        p2 = Point(x2, y2)
        p3 = Point(x1, y1)
        p4 = Point(x2, y1)
        if self.has_left_wall:
            l = Line(p1, p3)
            self._win.draw_line(l)
        if self.has_right_wall:
            l = Line(p2, p4)
            self._win.draw_line(l)
        if self.has_top_wall:
            l = Line(p1, p2)
            self._win.draw_line(l)
        if self.has_bottom_wall:
            l = Line(p3, p4)
            self._win.draw_line(l)

    def draw_move(self, to_cell, undo=False):
        """
        (x1, y1) -> (x2,y2)
        """
        if not self._x2 or not self._x1 or not self._y1 or not self._y2:
            raise ValueError("Missing coordiantes for self")
        if not to_cell._x2 or not to_cell._x1 or not to_cell._y1 or not to_cell._y2:
            raise ValueError("Missing coordiantes for to_cell")

        x2 = (to_cell._x2 - to_cell._x1) / 2 + to_cell._x1
        y2 = (to_cell._y2 - to_cell._y1) / 2 + to_cell._y1
        x1 = (self._x2 - self._x1) / 2 + self._x1
        y1 = (self._y2 - self._y1) / 2 + self._y1
        fill_color = "red"
        if undo:
            fill_color = "grey"

        l = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(l, fill_color)
