from fanorona.piece import Player
from fanorona.board import Board

def test_board_exists():
    board = Board()
    assert board is not None

def test_empty_board():
    board = Board()
    for row in board.grid:
        for cell in row:
            assert cell is None, "Expected all cells to be empty on a new board"

def test_default_correct_dimensions():
    board = Board()

    rows = 5
    cols = 9
    assert len(board.grid) == rows, f"Expected {rows} rows, got {len(board.grid)}"
    for row in board.grid:
        assert len(row) == cols, f"Expected {cols} columns, got {len(row)}"

def test_special_dimensions():
    rows = 3
    cols = 3
    board = Board(rows=rows, cols=cols, grid=[[None, None, None], [None, None, None], [None, None, None]])

    assert len(board.grid) == rows, f"Expected {rows} rows, got {len(board.grid)}"
    for row in board.grid:
        assert len(row) == cols, f"Expected {cols} columns, got {len(row)}"

def test_special_dimensions_with_pieces():
    rows = 3
    cols = 3
    board = Board(rows=rows, cols=cols, grid=[[None, Player.WHITE, None], 
                                              [None, Player.WHITE, None], 
                                              [None, None, None]])
    assert board.grid[0][1].player == Player.WHITE, "Expected a white piece at (0, 1)"
    assert board.grid[1][1].player == Player.WHITE, "Expected a white piece at (1, 1)"

def test_get_piece():
    board = Board()
    piece = board.get_piece(0, 0)
    assert piece is None, "Expected get_piece to return None for an empty cell"

def test_get_all_pieces():
    board = Board()
    pieces = board.get_all_pieces()
    assert isinstance(pieces, list), "Expected get_all_pieces to return a list"
    assert len(pieces) == 0, "Expected get_all_pieces to return an empty list for a new board"

def test_create_board_with_wrong_dimensions():
    try:
        board = Board(rows=3, cols=3, grid=[[None, None], [None, None], [None, None]])
        assert False, "Expected ValueError for grid with wrong number of columns"
    except ValueError:
        pass

    try:
        board = Board(rows=3, cols=3, grid=[[None, None, None], [None, None], [None, None, None]])
        assert False, "Expected ValueError for grid with wrong number of columns in a row"
    except ValueError:
        pass