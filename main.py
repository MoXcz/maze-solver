from wall import Cell
from window import Window


def main():
    win = Window(800, 600)
    wall = Cell(win, 100, 100, 200, 200, right=False)
    wall.draw()
    wall2 = Cell(win, 300, 100, 400, 200, left=False)
    wall2.draw()
    wall.draw_move(wall2, True)
    win.wait_for_close()


if __name__ == "__main__":
    main()
