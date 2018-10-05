from itertools import repeat


class Grid:

    def __init__(self, size):
        self.size = size
        self.spread = range(0, self.size)
        self.values = list(repeat(list(repeat(' ', size)), size))

    def mark_at(self, at):
        (x, y) = at
        return self.values[x][y]

    def is_full(self):
        return all(map(lambda at: self.mark_at(at) != ' ', self.everywhere()))

    def is_winner(self, mark):
        return any(map(lambda line: all(map(lambda at: self.mark_at(at) == mark, line)), self.lines()))

    def winner(self):
        return 'Y' if self.is_winner('Y') else 'X' if self.is_winner('X') else ' '

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

    # A potential win is a 3-in-a-row line with 2
    # of the player's mark and an blank space
    def has_potential_win(self, line, mark):
        if list(sorted(map(self.mark_at, line))) == [' ', mark, mark]:
            return list(filter(lambda a: self.mark_at(a) == ' ', line))[0]

        return None

    def find_win(self, mark):
        for l in self.lines():
            win = self.has_potential_win(l, mark)
            if win is not None:
                return win

        return None

    # A potential fork position is blank and is part of
    # at least 2 lines each of which contains only a
    # single non-blank position which is held by given mark
    def has_potential_fork(self, at, mark):
        if self.mark_at(at) != ' ':
            return None

        lines = filter(lambda l: at in l, self.lines())
        lines = filter(lambda l: 1 if list(sorted(map(self.mark_at, l))) == [' ', ' ', mark] else 0, lines)
        return at if len(list(lines)) >= 2 else None

    def find_fork(self, mark):
        for at in self.everywhere():
            if self.has_potential_fork(at, mark):
                return at

        return None

    # Only works for 3x3 grids
    def pick_spot(self, mark):

        # If there's no where to go, forget about it
        if self.is_full():
            return None

        # If you can win, win
        my_win = self.find_win(mark)

        if my_win is not None:
            return my_win

        # If the opponent is going to win, stop them
        their_win = self.find_win(Grid.opponent(mark))

        if their_win is not None:
            return their_win

        # If you can make a fork, do so
        my_fork = self.find_fork(mark)

        if my_fork is not None:
            return my_fork

        # If the opponent is going to make a fork, stop them
        their_fork = self.find_fork(Grid.opponent(mark))

        if their_fork is not None:
            return their_fork

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
            if self.mark_at(at) == ' ':
                return at

        # Shouldn't reach this point, but give up if you do
        return None

    @staticmethod
    def opponent(mark):
        return 'X' if mark == 'O' else 'O' if mark == 'X' else ' '
