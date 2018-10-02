from itertools import repeat


class Grid:

    def __init__(self, size):
        self.size = size
        self.values = list(repeat(list(repeat(None, size)), size))

    def mark_at(self, x, y):
        return self.values[x][y]
