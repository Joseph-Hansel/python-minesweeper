from app.db import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class GameResult(Base):
    __tablename__ = "game_results"

    id = Column(Integer, primary_key=True, index=True)
    player_name = Column(String, nullable=False)
    board_size = Column(Integer, nullable=False)
    mines = Column(Integer, nullable=False)
    result = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
