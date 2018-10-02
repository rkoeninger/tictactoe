from itertools import product
from tkinter import Button, Tk


class Window:

    def __init__(self, grid):
        self.grid = grid
        self.window = Tk()
        self.window.title("Tic-Tac-Toe")

        for (x, y) in product(range(grid.size), range(grid.size)):
            button = Button(
                self.window,
                text=" ",
                command=self.clicked(x, y))
            button.config(font=("Courier", 40))
            button.grid(column=x, row=y)

    def clicked(self, x, y):
        return lambda: print(str(self.grid.mark_at(x, y)))

    def show(self):
        self.window.mainloop()
