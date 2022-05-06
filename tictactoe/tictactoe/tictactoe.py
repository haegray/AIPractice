"""
Tic Tac Toe Player
"""

import math
import numpy as np
import copy
import time

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
    num_x = 0
    num_o = 0
    turn = ''
    for i in board:
        for j in i:
            if j == X:
                num_x += 1
            elif j == O:
                num_o += 1
    
    if num_x <= num_o:
        turn = X
    else:
        turn = O
    return turn


def actions(board):
    possible_actions = []
    for i,x in enumerate(board):
        for j,y in enumerate(x):
            if y == EMPTY:
                possible_actions.append((i,j))
    return possible_actions

def result(board, action):
    board_new = [x[:] for x in board]
    try:
        i,j = action
        board_new[i][j] = player(board)
    except TypeError:
        "Invalid move"
    return board_new

def winner(board):
    winner = None
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X) or (board[0][0] == X and board[0][1] == X and board[0][2] == X) or (board[1][0] == X and board[1][1] == X and board[1][2] == X) or (board[2][0] == X and board[2][1] == X and board[2][2] == X) or (board[0][0] == X and board[1][0] == X and board[2][0] == X) or (board[0][1] == X and board[1][1] == X and board[2][1] == X) or (board[0][2] == X and board[1][2] == X and board[2][2] == X):
            winner = X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O) or (board[0][0] == O and board[0][1] == O and board[0][2] == O) or (board[1][0] == O and board[1][1] == O and board[1][2] == O) or (board[2][0] == O and board[2][1] == O and board[2][2] == O) or (board[0][0] == O and board[1][0] == O and board[2][0] == O) or (board[0][1] == O and board[1][1] == O and board[2][1] == O) or (board[0][2] == O and board[1][2] == O and board[2][2] == O):
            winner = O
    return winner

def terminal(board):
    return (not any(EMPTY in row for row in board)) or winner(board) != None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    num = 0
    result = winner(board)
    if result == X:
        num = 1
    elif result == O:
        num = -1
    return num

def minimax(board):
    _, action = minimax_aux(board)
    return action

def minimax_aux(board):
    best_action = []
    if terminal(board):
        last_action = (-1, -1)
        v = utility(board)
    else:
        mark = player(board)
        if mark == X:
            v = -1* math.inf
            for action in actions(board):
                v = max(v, minimax_aux(result(board, action))[0])
                best_action.append((v,action))
            last_action =  max(best_action,key=lambda item:item[0])[1]
        elif mark == O:
            v = math.inf
            for action in actions(board):
                v = min(v, minimax_aux(result(board, action))[0])
                best_action.append((v,action))
            last_action =  min(best_action,key=lambda item:item[0])[1]
    return v, last_action
