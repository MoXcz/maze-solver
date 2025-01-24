from tkinter import Tk, Canvas


class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canva = Canvas(self.root, bg="black", height=height, width=width)
        self.canva.pack(fill="both", expand=1)
        self.on_window = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.on_window = True
        while self.on_window is True:
            self.redraw()

    def close(self):
        self.on_window = False
