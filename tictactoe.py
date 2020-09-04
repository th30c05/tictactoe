"""
Tic Tac Toe Player
"""

import math

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
    finish = False
    num_row = 0
    num_cell = 0

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
    i = action[0]
    j = action[1]
    goal_position = ((i*3)+j)
    actual_position = 0
    result_board = board
    finish = False

    while not finish:
        if actual_position == goal_position:
            result_board[goal_position] = player(board)
            finish = True
        else:
            finish = False

        actual_position += 1

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    next = 0

    while not finish:
        cell = board[next]

        if cell is None:
            num = next
            if 3 < num <= 6:
                num -= 3
                actions.add(1, num)
            elif 6 < num <= 9:
                num -= 6
                actions.add(2, num)
            elif num <= 3:
                actions.add(0, num)

        next += 1

        if next == 10:
            finish = True
        else:
            finish = False




        #up = ((i+3, j-1),(i+3, j),(i+3,j+1))


    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
