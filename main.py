from window import Line, Point, Window


def main():
    win = Window(800, 600)
    point1 = Point(0, 100)
    point2 = Point(200, 100)
    line = Line(point1, point2)
    win.draw_line(line, "white")
    win.wait_for_close()


if __name__ == "__main__":
    main()
