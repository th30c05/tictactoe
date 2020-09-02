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

    for cell in board:
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
    actions = set()
    finish = False
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

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
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
