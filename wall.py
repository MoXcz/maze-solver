from window import Line, Point


class Cell:
    def __init__(
        self,
        win,
        x1,
        y1,
        x2,
        y2,
        left=True,
        right=True,
        top=True,
        bottom=True,
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom

    def draw(self):
        """
        p1(x1,y2)  p2(x2, y2)
        p3(x1,y1)  p4(x2, y1)
        """
        p1 = Point(self._x1, self._y2)
        p2 = Point(self._x2, self._y2)
        p3 = Point(self._x1, self._y1)
        p4 = Point(self._x2, self._y1)
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
