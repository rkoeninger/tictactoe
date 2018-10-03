from itertools import repeat


class Grid:

    def __init__(self, size):
        self.size = size
        self.spread = range(0, self.size)
        self.values = list(repeat(list(repeat(None, size)), size))

    def mark_at(self, at):
        (x, y) = at
        return self.values[x][y]

    def is_mark_at(self, at):
        return self.mark_at(at) is not None

    def is_full(self):
        return all(map(self.is_mark_at, self.everywhere()))

    def is_winner(self, mark):
        return any(map(lambda line: all(map(lambda at: self.mark_at(at) == mark, line)), self.lines()))

    def winner(self):
        if self.is_winner("X"):
            return "X"

        if self.is_winner("Y"):
            return "Y"

        return None

    def everywhere(self):
        for x in self.spread:
            for y in self.spread:
                yield (x, y)

    def lines(self):

        # Verticals
        yield from map(lambda x: map(lambda y: (x, y), self.spread), self.spread)

        # Horizontals
        yield from map(lambda y: map(lambda x: (x, y), self.spread), self.spread)

        # Diagonals
        yield map(lambda z: (z, z), self.spread)
        yield map(lambda z: (z, -z), self.spread)

    @staticmethod
    def opponent(mark):
        if mark == "X":
            return "O"

        if mark == "O":
            return "X"

        return None

    # A potential win is a 3-in-a-row line with 2
    # of the player's mark and an blank space
    def find_win(self, line, mark):
        mark_count = 0
        none_count = 0
        none_at = None

        for at in line:
            here = self.mark_at(at)

            if here == mark:
                mark_count = mark_count + 1

            if here is None:
                none_count = none_count + 1
                none_at = at

        if mark_count == 2 and none_count == 1:
            return none_at

        return None

    # Only works for 3x3 grids
    def pick_spot(self, mark):

        # If there's no where to go, forget about it
        if self.is_full():
            return None

        # If you can win, win
        for l in self.lines():
            win = self.find_win(l, mark)
            if win is not None:
                return win

        # If the opponent is going to win, stop them
        for l in self.lines():
            win = self.find_win(l, Grid.opponent(mark))
            if win is not None:
                return win

        # If you can make a fork, do so
        # TODO: implement potential fork detection

        # If the opponent is going to make a fork, stop them
        # TODO: implement potential fork detection

        # Pick a spot, with priority: center, corner, side
        priority = [
            (1, 1),
            (0, 0),
            (0, 2),
            (2, 0),
            (2, 2),
            (1, 0),
            (0, 1),
            (1, 2),
            (2, 1)
        ]

        for at in priority:
            if self.mark_at(at) is None:
                return at

        # Should reach this point, but give up if you do
        return None
