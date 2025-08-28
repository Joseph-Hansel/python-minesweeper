from app.game_logic.board import Board
from app.game_logic.logic import GameLogic
from app.interaction.game_ui import GameUI
from app.storage.repository import save_result

def run_game():
    board = Board(size=10, mines=10)
    logic = GameLogic(board)
    cli = GameUI(logic)

    print("Welcome to Minesweeper!")
    cli.display_board()

    while True:
        row, col = cli.get_move()

        if not logic.reveal(row, col):
            print("💥 You hit a mine! Game over.")
            save_result("Player1", board.size, board.mines, "lose")
            break

        cli.display_board()

        if logic.check_win():
            print("🎉 You win!")
            save_result("Player1", board.size, board.mines, "win")
            break

if __name__ == "__main__":
    run_game()