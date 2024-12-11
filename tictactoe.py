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
    number_X =0
    number_O =0
    for item  in board:
        number_X+=item.count(X)
        number_O+=item.count(O)
    if number_O == number_X:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = list()
    for i,_ in enumerate(board):
        for j,__ in enumerate(_):
            if __ == EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_turn = player(board)
    i = action[0]
    j = action[1]
    board[i][j] = player_turn 
    return board 

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_ = who_wins(board)
    if winner_ != None:
        return winner_
    rows_vericaly = []
    for k in range(3):
        rows = []
        for l in range(3):
            rows.append(board[l][k])
        rows_vericaly.append(rows)
    winner_ = who_wins(rows_vericaly)
    if winner_ != None:
        return winner_
    rows_diagonally_right = []
    rows_diagonally_left = []

    
    rows = []
    rows_ = []
    n =2
    for l in range(3):
        rows.append(board[l][l])
        rows_.append(board[l][n])
        n-=1
    rows_diagonally_right.append(rows)
    rows_diagonally_left.append(rows_)

    winner_ = who_wins(rows_diagonally_right)

    if winner_!=None:
        return winner_
    
    winner_ = who_wins(rows_diagonally_left)

    if winner_!=None:
        return winner_
    return None


def  who_wins(horizantal_board):
    for i in horizantal_board:
        if i.count(X) == 3:
            return X
        if i.count(O) ==3:
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None:
        return True

    for item in board:
        if item.__contains__(EMPTY):
            return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)!=None:
        if winner(board) == X:
            return 1
        else:
            return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_ = player(board)
    actions_ = actions(board)
    max_actoins = {}
    min_actoins = {}

    if player_ == X:
        for _,a in enumerate(actions_):
            board1 = result(board,a)
            max_actoins[_] = [max_value(board1),a]
        return max(max_actoins.values())[1]
    else :
        for _,a in enumerate(actions_):
            board1 = result(board,a)
            min_actoins[_] = [min_value(board1),a]
        return min(min_actoins.values())[1]

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -1
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v



