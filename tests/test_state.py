from fanorona.state import State
from fanorona.piece import Player

def test_state_exists():
    state = State()
    assert state is not None

def test_initial_board_state():
    state = State()
    assert state.board is not None, "Expected state to have a board"
    assert len(state.board.grid) == 5, "Expected board to have 5 rows"
    assert len(state.board.grid[0]) == 9, "Expected board to have 9 columns"
    assert state.current_player == Player.WHITE, "Expected white to go first (current_player=1)"

def test_get_possible_moves():
    state = State()
    moves = state.get_possible_moves()
    assert isinstance(moves, list), "Expected get_possible_moves to return a list"
    assert len(moves) > 0, "Expected get_possible_moves to return some moves for the initial state"

def test_make_move():
    state = State()
    moves = state.get_possible_moves()
    move = moves[0]
    new_state = state.make_move(move)
    assert new_state is not None, "Expected make_move to return a new state"
    assert new_state.current_player == Player.BLACK, "Expected current player to switch after a move"

def test_make_move_inplace():
    state = State()
    moves = state.get_possible_moves()
    move = moves[0]
    state.make_move(move, inplace=True)
    assert state is not None, "Expected make_move to return a new state"
    assert state.current_player == Player.BLACK, "Expected current player to switch after a move"