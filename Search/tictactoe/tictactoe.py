"""
Tic Tac Toe Player game
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
    return X if sum(row.count(X) for row in board) <= sum(row.count(O) for row in board) else O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] is EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action")
    new_board = [row.copy() for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None
    best_value = -math.inf if current_player == X else math.inf

    for action in actions(board):
        new_board = result(board, action)
        value = minimax_value(new_board, current_player)

        if (current_player == X and value > best_value) or (current_player == O and value < best_value):
            best_value = value
            best_action = action

    return best_action

def minimax_value(board, current_player):
    """
    Returns the minimax value of the board for the current player.
    """
    if terminal(board):
        return utility(board)

    if current_player == X:
        best_value = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board, O)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = math.inf
        for action in actions(board):
            new_board = result(board, action)
            value = minimax_value(new_board, X)
            best_value = min(best_value, value)
        return best_value
