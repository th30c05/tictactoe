"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for rown in board:
        for cell in rown:
            if cell == X:
                x_counter += 1
            elif cell == O:
                o_counter += 1
            elif cell is None:
                pass

    if x_counter > o_counter:
        return O
    elif x_counter <= o_counter:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_cells = set()
    num_row = 0
    num_cell = 0

    finish = False
    while not finish:
        next_action = (board[num_row])[num_cell]

        if next_action is None:
            empty_cells.add((num_row, num_cell))

        num_cell += 1

        if num_cell == 3:
            num_cell -= 3
            num_row += 1

        if num_row == 3:
            finish = True

    return empty_cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)

    if not (result_board[action[0]])[action[1]] is None:
        raise NameError("Invalid Action")
    else:
        (result_board[action[0]])[action[1]] = player(board)
        return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win = None

    if board[0][0] == board[0][1] == board[0][2]:
        win = board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        win = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        win = board[2][0]

    if board[0][0] == board[1][0] == board[2][0]:
        win = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        win = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        win = board[0][2]

    if board[0][0] == board[1][1] == board[2][2]:
        win = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        win = board[0][2]

    return win


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0

    for rown in board:
        for cell in rown:
            if cell == X:
                counter += 1
            elif cell == O:
                counter += 1
            elif cell is None:
                counter += 0

    if counter == 9:
        return True
    elif winner(board) == X or winner(board) == O:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    AI = player(board)
    best_value = float("-inf") if AI == X else float("inf")

    if terminal(board):
        return None

    else:
        for action in actions(board):
            new_value = utility(result(board, action))

            if AI == X:
                new_value = max(new_value, best_value)
            elif AI == O:
                new_value = min(new_value, best_value)

            if new_value != best_value:
                best_value = new_value
                best_action = action

            best_value = float("-inf") if AI == O else float("inf")

            for actionn in actions(result(board,best_action)):
            
                new_value = utility(result(board, actionn))

                if AI == X:
                    new_value = min(new_value, best_value)
                elif AI == O:
                    new_value = max(new_value, best_value)

                if new_value != best_value:
                    best_value = new_value
                    best_action = action

        return best_action
