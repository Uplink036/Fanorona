from copy import deepcopy
from dataclasses import dataclass

from fanorona.piece import Piece, Player

@dataclass
class Move:
    piece: Piece
    new_x: int
    new_y: int

class Board():
    def __init__(self, rows=5, cols=9, grid=None) -> None:
        self.rows = rows
        self.cols = cols
        if grid is not None:
            self.initiliaze(grid)
        else:
            self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def initiliaze(self, grid: list[list[Piece | None]]) -> None:
        self.grid = grid
        self._validate_grid(self.grid)
        self._place_pieces(self.grid)

    def initiliaze_fanorona(self) -> None:
        assert self.rows == 5 and self.cols == 9, "Fanorona board must be 5 rows and 9 columns"
        grid = [[Player.WHITE]*self.cols, 
            [Player.WHITE]*self.cols, 
            [Player.WHITE, Player.BLACK, Player.WHITE, Player.BLACK, None, Player.BLACK, Player.WHITE, Player.BLACK, Player.WHITE],
            [Player.BLACK]*self.cols, 
            [Player.BLACK]*self.cols]
        self.initiliaze(grid)

    def _validate_grid(self, grid: list[list[Player | None]]) -> None:
        if len(grid) != self.rows:
            raise ValueError(f"grid must have {self.rows} rows")
        for row in grid:
            if len(row) != self.cols:
                raise ValueError(f"grid must have {self.cols} columns")
            for cell in row:
                if cell is not None and not isinstance(cell, (Player, Piece)):
                    raise ValueError("grid cells must be instances of Player or Piece or None")
                
    def _place_pieces(self, grid: list[list[Piece | None]]) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] is not None:
                    grid[i][j] = Piece(j, i, grid[i][j])


    def get_piece(self, x: int, y: int) -> Piece | None:
        if 0 <= y < self.rows and 0 <= x < self.cols:
            return self.grid[y][x]
        else:
            raise IndexError("Coordinates out of bounds")
        
    def get_all_pieces(self) -> list[Piece]:
        pieces = []
        for row in self.grid:
            for cell in row:
                if cell is not None:
                    pieces.append(cell)
        return pieces
    
    def get_all_pieces_by_player(self, player: Player) -> list[Piece]:
        return [piece for piece in self.get_all_pieces() if piece.player == player]
    
    def _piece_has_empty_neighbor(self, piece: Piece) -> bool:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighbor_x = piece.x + dx
                neighbor_y = piece.y + dy
                if 0 <= neighbor_y < self.rows and 0 <= neighbor_x < self.cols:
                    if self.grid[neighbor_y][neighbor_x] is None:
                        return True
        return False
    
    def _get_all_pieces_with_atleast_one_empty_neighbor(self, player: Player) -> list[Piece]:
        pieces = []
        for piece in self.get_all_pieces_by_player(player):
            if self._piece_has_empty_neighbor(piece):
                pieces.append(piece)
        return pieces
    
    def get_possible_moves(self, player: Player) -> list[Move]:
        moves = []
        for piece in self._get_all_pieces_with_atleast_one_empty_neighbor(player):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    new_x = piece.x + dx
                    new_y = piece.y + dy
                    if 0 <= new_y < self.rows and 0 <= new_x < self.cols:
                        if self.grid[new_y][new_x] is None:
                            moves.append(Move(piece, new_x, new_y))
        return moves
    
    def make_move(self, move: Move) -> None:
        if self.grid[move.new_y][move.new_x] is not None:
            raise ValueError("Target cell is not empty")
        if self.grid[move.piece.y][move.piece.x] != move.piece:
            raise ValueError("Piece is not at its current location")
        if abs(move.new_x - move.piece.x) > 1 or abs(move.new_y - move.piece.y) > 1:
            raise ValueError("Move must be to an adjacent cell")
        if (move.new_x == move.piece.x and move.new_y == move.piece.y):
            raise ValueError("Move must change the piece's position")
        
        self.grid[move.piece.y][move.piece.x] = None
        move.piece.x = move.new_x
        move.piece.y = move.new_y
        self.grid[move.new_y][move.new_x] = move.piece


    def copy(self) -> 'Board':
        new_grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] is not None:
                    new_grid[i][j] = self.grid[i][j].player
        return Board(rows=self.rows, cols=self.cols, grid=new_grid)

    def __str__(self) -> str:
        return f"Board(rows={self.rows}, cols={self.cols}, grid=...)"