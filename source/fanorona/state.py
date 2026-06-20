from fanorona.board import Board, Move
from fanorona.piece import Player, Piece


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
            # Clone the board grid and re-bind pieces to avoid identity checks in make_move()
            new_grid = [[None for _ in range(self.board.cols)] for _ in range(self.board.rows)]
            for y, row in enumerate(self.board.grid):
                for x, cell in enumerate(row):
                    if cell is not None:
                        # Re-create Piece with correct coordinates to maintain identity
                        new_grid[y][x] = Piece(x, y, cell.player)

            new_state = State()
            new_state.board.rows = self.board.rows
            new_state.board.cols = self.board.cols
            new_state.board.grid = new_grid
            new_state.current_player = Player.BLACK if self.current_player == Player.WHITE else Player.WHITE
            # Now the move references a piece from the cloned board, so make_move will work
            new_state.board.make_move(move)
        return new_state

    def __str__(self) -> str:
        return f"State(current_player={self.current_player}, board=\n{self.board})"
