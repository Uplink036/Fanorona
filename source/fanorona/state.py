from fanorona.board import Board, Move
from fanorona.piece import Player

class State:
    """Represents the current state of a Fanorona game, including the board and player turn."""
    def __init__(self):
        self.board = Board()
        self.board.initiliaze_fanorona()
        self.current_player = Player.WHITE

    def get_possible_moves(self) -> list[Move]:
        """Return a list of all possible moves for the current player in the current state."""
        if self.current_player == Player.WHITE:
            return self.board.get_possible_moves(Player.WHITE)
        else:
            return self.board.get_possible_moves(Player.BLACK)
        
    def make_move(self, move: Move, inplace=True) -> 'State':
        """Return a new State resulting from making the given move."""
        if inplace:
            self.board.make_move(move)
            self.current_player = Player.BLACK if self.current_player == Player.WHITE else Player.WHITE
            return self
        else:
            new_state = State()
            new_state.board = self.board.copy()  # Assuming Board has a copy method
            new_state.board.make_move(move)
            new_state.current_player = Player.BLACK if self.current_player == Player.WHITE else Player.WHITE
        return new_state
    
    def __str__(self) -> str:
        return f"State(current_player={self.current_player}, board=\n{self.board})"