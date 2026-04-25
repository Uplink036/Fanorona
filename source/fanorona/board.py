from .piece import Piece, Player

class Board():
    def __init__(self, rows=5, cols=9, grid=None):
        self.rows = rows
        self.cols = cols
        if grid is not None:
            self.initiliaze(grid)
        else:
            self.grid = [[None for _ in range(cols)] for _ in range(rows)]

    def initiliaze(self, grid: list[list[Piece | None]]):
        self.grid = grid
        self._validate_grid(self.grid)
        self._place_pieces(self.grid)

    def initiliaze_fanorona(self):
        grid = [[Player.WHITE]*self.cols, 
            [Player.WHITE]*self.cols, 
            [Player.WHITE, Player.BLACK, Player.WHITE, Player.BLACK, None, Player.BLACK, Player.WHITE, Player.BLACK, Player.WHITE],
            [Player.BLACK]*self.cols, 
            [Player.BLACK]*self.cols]
        self.initiliaze(grid)

    def _validate_grid(self, grid: list[list[Piece | None]]):
        if len(grid) != self.rows:
            raise ValueError(f"grid must have {self.rows} rows")
        for row in grid:
            if len(row) != self.cols:
                raise ValueError(f"grid must have {self.cols} columns")
            for cell in row:
                if cell is not None and not isinstance(cell, (Player, Piece)):
                    raise ValueError("grid cells must be instances of Player or Piece or None")
                
    def _place_pieces(self, grid: list[list[Piece | None]]):
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