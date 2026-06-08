"""
Tic-Tac-Toe Game
================
A two-player command-line Tic-Tac-Toe game where players take turns placing
their characters ('X' or 'O') on a 3x3 game board until one player wins.
"""


class InvalidCharacterException(Exception):
    """Raised when a player chooses an invalid character (not 'X' or 'O')."""
    pass


class InvalidGameBoardPositionException(Exception):
    """Raised when a player enters an invalid board position (not 1-9)."""
    pass


player_one = input("Player one name: ")
player_two = input("Player two name: ")

game_board = []

# Maps board position numbers (1-9) to their corresponding row index (0-2)
row_index_dict = {
    1: 0,
    2: 0,
    3: 0,
    4: 1,
    5: 1,
    6: 1,
    7: 2,
    8: 2,
    9: 2
}

# Maps board position numbers (1-9) to their corresponding column index (0-2)
col_index_dict = {
    1: 0,
    4: 0,
    7: 0,
    2: 1,
    5: 1,
    8: 1,
    3: 2,
    6: 2,
    9: 2
}

player_one_char = input(f"{player_one} would you like to play with 'X' or 'O'? ")
if player_one_char not in ("X", "O"):
    raise InvalidCharacterException(f"Invalid character {player_one_char}. Please choose 'X' or 'O'.")
# Automatically assign the opposite character to player two
player_two_char = ("X" if player_one_char == "O" else "O")
print(player_one_char, player_two_char)


def init_game_board():
    """
    Initialize the game board with position numbers 1 through 9.

    Resets the global game_board to a 3x3 grid where each cell contains
    its corresponding position number as a string.
    """
    global game_board
    game_board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]


def print_game_board(show_numbers=False):
    """
    Print the current state of the game board to the console.

    :param show_numbers: If True, displays position numbers for empty cells.
                         If False, displays a blank space for empty cells.
                         Cells occupied by a player always show their character.
    :type show_numbers: bool
    """
    for row in range(len(game_board)):
        print("| ", end="")
        for col in range(len(game_board[row])):
            if show_numbers:
                elem_show = game_board[row][col]
            else:
                # Show blank space for unoccupied cells, player char otherwise
                elem_show = (' ' if str(game_board[row][col]).isdigit() else game_board[row][col])
            print(f"{elem_show}", end=' | ')
        print()


def check_for_winner(input_char):
    """
    Check whether the given character has won the game.

    Evaluates all 8 possible winning combinations: 3 rows, 3 columns,
    and 2 diagonals.

    :param input_char: The player's character ('X' or 'O') to check for a win.
    :type input_char: str
    :return: True if the given character has a winning combination, False otherwise.
    :rtype: bool
    """
    global game_board
    return game_board[0][0] == game_board[0][1] == game_board[0][2] == input_char or \
        game_board[1][0] == game_board[1][1] == game_board[1][2] == input_char or \
        game_board[2][0] == game_board[2][1] == game_board[2][2] == input_char or \
        game_board[0][0] == game_board[1][0] == game_board[2][0] == input_char or \
        game_board[0][1] == game_board[1][1] == game_board[2][1] == input_char or \
        game_board[0][2] == game_board[1][2] == game_board[2][2] == input_char or \
        game_board[0][0] == game_board[1][1] == game_board[2][2] == input_char or \
        game_board[0][2] == game_board[1][1] == game_board[2][0] == input_char


def is_game_board_cell_free(cell):
    """
    Check whether a specific board cell is still unoccupied.

    A cell is considered free if it still holds its original position number
    (i.e., it has not been replaced by a player's character).

    :param cell: The position number as a string (e.g., '1' through '9').
    :type cell: str
    :return: True if the cell is free, False if it has already been taken.
    :rtype: bool
    """
    global game_board
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == cell:
                return True
    return False


def play(player, player_sign):
    """
    Handle a single player's turn.

    Prompts the player to choose a free position (1-9) on the board,
    validates the input, places their character on the board, and checks
    for a winner. Keeps prompting until a valid, unoccupied position is chosen.

    :param player: The name of the current player.
    :type player: str
    :param player_sign: The character assigned to the player ('X' or 'O').
    :type player_sign: str
    :raises InvalidGameBoardPositionException: If the input is not a digit
        or is outside the range 1-9.
    """
    global game_board
    while True:
        player_next_move = input(f"{player} choose a free position [1-9]: ")
        if not player_next_move.isdigit() or int(player_next_move) < 1 or int(player_next_move) > 9:
            raise InvalidGameBoardPositionException(
                f"Invalid position {player_next_move}. Please choose a number between 1 and 9.")

        if is_game_board_cell_free(player_next_move):
            row = row_index_dict[int(player_next_move)]
            col = col_index_dict[int(player_next_move)]
            game_board[row][col] = player_sign
            print_game_board(show_numbers=False)

            if check_for_winner(player_sign):
                print(f"{player} won!")
                exit(0)

            break
        else:
            print("This position is already taken. Please choose another one.")


# --- Game Entry Point ---

# Set up the board and display initial state with position numbers
init_game_board()
print("This is the numeration of the board:")
print_game_board(show_numbers=True)
print(f"{player_one} starts first!")

# Main game loop: alternate turns between player one and player two
while True:
    # Player one turn
    play(player_one, player_one_char)

    # Player two turn
    play(player_two, player_two_char)
