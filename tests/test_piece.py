from fanorona.piece import Piece, Player

def test_piece_exists():
    piece = Piece(x=1, y=2, player='white')
    assert piece is not None

def test_piece_coords():
    piece = Piece(x=1, y=2, player='white')
    assert piece.x == 1
    assert piece.y == 2

def test_piece_color():
    piece = Piece(x=1, y=2, player='white')
    assert piece.player == Player.WHITE

def test_piece_without_color():
    try:
        piece = Piece(x=1, y=2)
        assert False, "Piece requires a player argument"
    except TypeError:
        pass
    