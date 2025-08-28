class GameUI:
    def __init__(self, game_logic):
        self.game_logic = game_logic

    def display_board(self):
        for row in self.game_logic.board.grid:
            print("|".join(row))
        print()

    def get_move(self):
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            return row, col
        except ValueError:
            print("Invalid input, try again.")
            return self.get_move()
