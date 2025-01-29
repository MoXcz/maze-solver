import tkinter as tk
from maze import Maze
from window import Window

num_rows = 12
num_cols = 16
margin = 50
screen_x = 800
screen_y = 600
cell_size_x = (screen_x - 2 * margin) / num_cols
cell_size_y = (screen_y - 2 * margin) / num_rows


def main():
    def start():
        start_button.pack_forget()
        animation_entry.pack_forget()
        maze = Maze(
            margin,
            margin,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            speed=float(animation_speed.get()),
        )
        print("Maze Generated")
        solvable = maze.solve()
        if solvable:
            print("Maze solved")
        else:
            print("Maze could not be solved")
        restart_button = tk.Button(win.root, text="Restart", command=restart)
        restart_button.pack(side="left")

    global win
    win = Window(screen_x, screen_y)

    animation_speed = tk.StringVar()
    animation_speed.set("0.05")
    start_button = tk.Button(win.root, text="Start", command=start)
    start_button.pack(side="left")
    animation_entry = tk.Entry(win.root, width=5, textvariable=animation_speed)
    animation_entry.pack(side="left")

    win.wait_for_close()


if __name__ == "__main__":

    def restart():
        win.root.destroy()
        main()

    main()
