import random


class Board:
    def __init__(self, size=10, mines=5):
        self.size = size
        self.mines = mines
        self.grid = [["🟫" for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self._place_mines()

    def _place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.size - 1)
            c = random.randint(0, self.size - 1)
            self.mine_positions.add((r, c))
