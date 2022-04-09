import numpy as np
# from board import Board
from cmath import inf
from const import *


def state(board, row, col, piece, strike = 4):
        score = 0
        for c in range(col - strike + 1):
            for r in range(row):
                if np.all(board[r, c:c + strike] == piece):
                    score+=1
                    
        for c in range(col):
            for r in range(row - strike + 1):
                if np.all(board[r:r+strike,c] == piece):
                    score+=1
                   
        for c in range(col-strike+1):
            for r in range(row - strike + 1):
                for s in range(strike):
                    if board[r+s][c+s] != piece:
                        break
                    if s == strike - 1: 
                        score +=1
        for c in range(col-strike+1):
            for r in range(strike - 1, row):
                for s in range(strike):
                    if board[r-s][c+s] != piece:
                        break
                    if s == strike - 1:  
                        score +=1
        return score

def player_heuristics(board, player, strike):
    row = board.row
    col = board.column
    piece = PIECES[player]
    weight = [-1000, 1000][player]
    strike_1 = state(board.board, row, col, piece, strike-1) * weight
    if strike_1: 
        return strike_1
    strike_2 = state(board.board, row, col, piece, strike-2) * weight/board.board.size**2
    if strike_2:
        return strike_2
    else: 
        return 0

def winning_heuristisc(player):
    weight = [-1000, 1000][player]
    return inf * weight

def heuristics(board, strike):
    return max(player_heuristics(board, PLAYER_MIN, strike), player_heuristics(board, PLAYER_MAX, strike), key=abs)

