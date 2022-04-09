import random
import numpy as np
from const import *
class Board:
    def __init__(self, row, column, board = None, available = None):
        if board is None:
            self.board = np.zeros((row, column))
        else: 
            self.board = board.copy()
        
        if available is None:
            self.available = [i for i in range(column)]
        else: 
            self.available = available.copy()
        self.row = row
        self.column = column
        


    def __free_place(self, move):
        free = np.flatnonzero(self.board[:,move] == 0)[-1]
        if free == 0:  
            self.available.remove(move)
        return free


    def print_board(self):
        print(self.board)
        
    def place_move(self, move, piece):
        self.board[self.__free_place(move), move] = piece

    def minimax_move(self, piece, player, depth, strike, draw, move_idx):
        move = do_minimax(self, depth, player, strike, draw, move_idx)
        if move != None:
            self.place_move(move, piece)

        

    def random_move(self,piece):
        move = random.choice(self.available)
        self.place_move(move, piece)


    def board_childern(self, piece):
        children = []
        for move in self.available:
            ch_board = Board(self.row, self.column, self.board, self.available)
            ch_board.place_move(move, piece)
            children.append((move, ch_board))
        return children


    def terminal(self):
        return len(self.available) == 0

    def winning_move(self, piece, strike):
        for c in range(self.column - strike + 1):
            for r in range(self.row):
                if np.all(self.board[r, c:c + strike] == piece):
                    # print('horizontal')
                    return True
        
        for c in range(self.column):
            for r in range(self.row - strike + 1):
                if np.all(self.board[r:r+strike,c] == piece):
                    # print('vertical')
                    return True

        for c in range(self.column- strike+1):
            for r in range(self.row - strike + 1):
                for s in range(strike):
                    if self.board[r+s][c+s] != piece:
                        break
                    if s == strike - 1: 
                        # print('positive sloped diag')
                        return True

        for c in range(self.column-strike+1):
            for r in range(strike - 1, self.row):
                for s in range(strike):
                    if self.board[r-s][c+s] != piece:
                        break
                    if s == strike - 1:  
                        # print('negative sloped diag')
                        return True

from alghoritm import do_minimax
