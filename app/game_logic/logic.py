class GameLogic:
    def __init__(self, board):
        self.board = board

    def reveal(self, row, col):
        if (row, col) in self.board.mine_positions:
            return False  
        self.board.grid[row][col] = "⬜"
        return True

    def check_win(self):
        return all(
            (r, c) in self.board.mine_positions or self.board.grid[r][c] != "🟫"
            for r in range(self.board.size) for c in range(self.board.size)
        )