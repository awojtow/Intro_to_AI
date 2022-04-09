import numpy as np
from board import Board
import random
# import pygame
import time
from const import *

random.seed(SEED)
import sys


  

class Game:
    def __init__(self, row, col, starting = PLAYER_MAX, strike = 4, min_alg = "rand", max_alg = "rand", min_depth = 1, max_depth = 1, draw = False):
        self.row = row
        self.col = col
        self.board = Board(row, col)
        self.strike = strike
        self.starting = starting
        self.game_over = False
        self.won = None
        self.alg = [max_alg,min_alg]
        self.depth = [max_depth, min_depth]
        self.move_idx = 0
        self.draw = draw
    
    def player_move(self, player):
        self.move_idx += 1
        other_player = 1 - player
       
        if self.board.winning_move(PIECES[other_player], self.strike):
            # print(f'winning player {PLAYER_NAME[other_player]}')
            self.won = other_player
            self.game_over = True
            return
        elif self.board.terminal():
            # print('terminal')
            self.game_over = True
            self.won = -1
            return
        else:
            if self.alg[player] == "rand":
                self.board.random_move(piece = PIECES[player])
            elif self.alg[player] == "mmx":
                self.board.minimax_move(depth = self.depth[player], strike = self.strike, piece = PIECES[player], player = player, draw = self.draw, move_idx = self.move_idx)
              

            
    def play(self):
        turn_id = self.starting
        while not self.game_over:
            if turn_id == PLAYER_MAX:
                    # print('__________MOVE MAX_______')
                    self.player_move(PLAYER_MAX)    
                    # self.board.print_board()
                    # print()

            elif turn_id == PLAYER_MIN:
                    # print('__________MOVE MIN_______')
                    self.player_move(PLAYER_MIN)      
                    # self.board.print_board()
                    # print()
            turn_id +=1  
            turn_id = turn_id%2
    
