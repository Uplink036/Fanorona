from fanorona.board import Board, Move
from fanorona.piece import Player
from fanorona.state import State


def render_board(board: Board) -> str:
    lines: list[str] = []
    col_numbers = ' '.join(str(i) for i in range(board.cols))
    lines.append('    ' + col_numbers)
    lines.append('    ' + '-' * (2 * board.cols - 1))

    for y in range(board.rows):
        row_chars: list[str] = []
        for x in range(board.cols):
            piece = board.get_piece(x, y)
            if piece is None:
                row_chars.append('.')
            else:
                row_chars.append('W' if piece.player == Player.WHITE else 'B')
        lines.append(f"{y} | " + ' '.join(row_chars))

    return '\n'.join(lines)

def get_initial_message() -> str:
    return "Welcome to Fanorona (terminal version)!\n" \
           "Type 'q' + Enter to quit. Press Enter to refresh.\n" \
           "Type 'moves' + Enter to see possible moves for the current player.\n"


def try_make_move(state: State, from_x: int, from_y: int, to_x: int, to_y: int) -> bool:
    """Attempt to make a move. Returns True if successful, False otherwise."""
    piece = state.board.get_piece(from_x, from_y)
    if piece is None:
        print(f"No piece at ({from_x}, {from_y})")
        return False
    
    move = Move(piece=piece, new_x=to_x, new_y=to_y)
    possible_moves = state.get_possible_moves()
    
    if move in possible_moves:
        state.make_move(move)
        return True
    else:
        print(f"Invalid move: ({from_x}, {from_y}) -> ({to_x}, {to_y})")
        return False


def get_moves_for_piece(state: State, from_x: int, from_y: int) -> list[Move]:
    """Get all possible moves for a piece at the given position."""
    piece = state.board.get_piece(from_x, from_y)
    if piece is None:
        return []
    
    all_moves = state.get_possible_moves()
    return [m for m in all_moves if m.piece.x == from_x and m.piece.y == from_y]


def play_loop() -> None:
    state: State = State()
    print("Fanorona (terminal)")
    print("Type 'q' + Enter to quit. Type 'help' for commands.")
    selected_piece: tuple[int, int] | None = None
    while True:
        display_current_board(state)
        display_available_moves(state, selected_piece)
        cmd = input('> ').strip().lower()
        match cmd:
            case 'q':
                print('Goodbye')
                break
            case 'help':
                display_help(selected_piece)
            case 'cancel':
                selected_piece = clear_selected_piece(selected_piece)
            case 'moves':
                list_current_player_moves(state, selected_piece)
            case _:
                if selected_piece:
                    selected_piece = perform_move(state, selected_piece, cmd)
                else:
                    selected_piece = select_piece(state, cmd) 

def display_current_board(state: State) -> None:
    print('\n' + render_board(state.board) + '\n')
    print(f"Current player: {'WHITE' if state.current_player == Player.WHITE else 'BLACK'}")

def display_available_moves(state: State, selected_piece: tuple[int, int] | None) -> None:
    if selected_piece:
        moves = get_moves_for_piece(state, selected_piece[0], selected_piece[1])
        print(f"Selected piece at ({selected_piece[0]}, {selected_piece[1]}). Available moves:")
        for i, move in enumerate(moves):
            print(f"  {i}: -> ({move.new_x}, {move.new_y})")
        print("Type move number, 'cancel' to deselect, or 'help' for options")
    else:
        print("Select a piece: enter 'x y' (e.g., '0 2'), or type 'help'")

def display_help(selected_piece: tuple[int, int] | None) -> None:
    print("Commands: 'help' (this), 'q' (quit)")
    if selected_piece:
        print("Enter a move number to make that move, or 'cancel' to deselect")
    else:
        print("Enter 'x y' to select a piece, or 'moves' to see all possible moves")

def clear_selected_piece(selected_piece: tuple[int, int] | None) -> None:
    if selected_piece:
        print("Piece deselected")
    return None

def list_current_player_moves(state: State, selected_piece: tuple[int, int] | None) -> None:
    if not selected_piece:
        print("All possible moves for current player:")
        for move in state.get_possible_moves():
            print(f"  ({move.piece.x}, {move.piece.y}) -> ({move.new_x}, {move.new_y})")
    else:
        print("Cannot show all moves while a piece is selected. Type 'cancel' to deselect.")

def select_piece(state: State, cmd: str) -> tuple[int, int] | None:
    try:
        parts = cmd.split()
        if len(parts) == 2:
            x, y = map(int, parts)
            piece = state.board.get_piece(x, y)
            if piece is None:
                print(f"No piece at ({x}, {y})")
                return None
            elif piece.player != state.current_player:
                print(f"That piece belongs to the other player")
                return None
            else:
                selected_piece = (x, y)
                print(f"Selected piece at ({x}, {y})")
                return selected_piece
        else:
            print("Invalid input. Enter 'x y' to select a piece")
            return None
    except ValueError:
        print("Invalid input. Type 'help' for options")
        return None

def perform_move(state: State, selected_piece: tuple[int, int], cmd: str) -> tuple[int, int] | None:
    try:
        move_idx = int(cmd)
        moves = get_moves_for_piece(state, selected_piece[0], selected_piece[1])
        if 0 <= move_idx < len(moves):
            move: Move = moves[move_idx]
            state.make_move(move)
            print("Move made!")
            return None
        else:
            print("Invalid move number")
            return selected_piece
    except ValueError:
        print("Invalid input. Enter a move number or 'cancel'")
        return selected_piece


if __name__ == '__main__':
    play_loop()
