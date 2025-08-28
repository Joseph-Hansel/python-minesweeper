
class GameLogic:
    def_init_(self, board):
        self.board = board

        def reveal(self, x, y):
            if (x, y) in 
            self.board.mine_positions:
            return False 
            self.board.grid[x][y] = "."
            return True

            def check_win(self):
                return all(
                    (x, y) in self.board.mine_positions or self.board.mine_positions or self.board.grid[x][y] != " "
                    for x in range(self.board.size) for y in range(self.board.size)
                )