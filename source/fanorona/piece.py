
# Create an enum that is black or white
from enum import Enum

class Player(Enum):
    WHITE = "white"
    BLACK = "black"

class Piece:
    def __init__(self, x: int, y: int, player: Player | str):
        self.x = x
        self.y = y
        if isinstance(player, str):
            try:
                player = Player(player)
            except ValueError:
                raise ValueError("player must be 'white' or 'black'")
        elif not isinstance(player, Player):
            raise ValueError("player must be an instance of the Player enum")
        self.player = player

    