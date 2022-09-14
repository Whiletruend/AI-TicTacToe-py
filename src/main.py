# Imports
from src.game.frame import Frame
from src.sql.database import Database

# Init database
game_database: Database = Database()
game_database.connect()

# Game_Frame
game_frame: Frame = Frame("Tic'T-AI'Toe", "400x400")
game_frame.show()