from wall import Cell
from window import Window


def main():
    win = Window(800, 600)
    wall = Cell(win, left=False)
    wall.draw(100, 100, 200, 200)
    win.wait_for_close()


if __name__ == "__main__":
    main()
