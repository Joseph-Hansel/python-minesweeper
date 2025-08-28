from app.db import SessionLocal
from app.models.game_results import GameResult

def save_result(player_name, board_size, mines, result):
    session = SessionLocal()
    game_result = GameResult(player_name=player_name, board_size=board_size, mines=mines, result=result)
    session.add(game_result)
    session.commit()
    session.close()
