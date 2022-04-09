from board import Board
from game import Game
import pygame 
import time
import numpy as np
from const import *
import sys

COLORS = {
    'min': (139,26,26),
    'max': (255,185,15),
    'black': (0,0,0),
    'font': (15,153,102),
    'board': (16,78,139)
}
class PyGame(Game):
    def __init__(self, row, col, starting = PLAYER_MAX, strike = 4, min_alg = "rand", max_alg = "rand", min_depth = 1, max_depth = 1, draw = False, save = False):
        super().__init__(row, col, starting, strike, min_alg, max_alg, min_depth, max_depth, draw)
        self.__SIZE = 80
        self.__RADIUS = int(self.__SIZE/2 - 20)
        self.__init_pygame()
        self.save = save


    def __init_pygame(self):
        pygame.init()
        pygame.font.init()
        self.__screen = pygame.display.set_mode((self.col * self.__SIZE, (self.row) * self.__SIZE))
        self.__font = pygame.font.SysFont("monospace", 15)
    def __draw_fragment(self,r,c,piece):
        if piece == PIECE_MAX: 
            color = COLORS["max"]
        elif piece == PIECE_MIN:
            color = COLORS["min"]
        else: 
            color = COLORS["black"]

        (x,y) = self.__SIZE * c, self.__SIZE * r
        pygame.draw.rect(self.__screen, COLORS["board"], (x, y, self.__SIZE, self.__SIZE))
        pygame.draw.circle(self.__screen, color, (int(x + self.__SIZE/2), int(y + self.__SIZE/2)), self.__RADIUS)

    def __pydraw_board(self):
        board = self.board.board
        for c in range(self.col):
            for r in range(self.row):
                self.__draw_fragment(r,c, board[r][c])
        pygame.display.update()


    def play(self):
        turn_id = self.starting
        while not self.game_over:
            for event in pygame.event.get():
                if self.game_over:
                    break
                pygame.time.wait(300)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    break
                if turn_id == PLAYER_MAX:
                    print('__________MOVE MAX_______')
                    super().player_move(PLAYER_MAX)    
                    self.board.print_board()
                    self.__pydraw_board()

                elif turn_id == PLAYER_MIN:
                    print('__________MOVE MIN_______')
                    self.player_move(PLAYER_MIN)      
                    self.board.print_board()
                    self.__pydraw_board()
                    
                
                turn_id +=1  
                turn_id = turn_id%2
                if self.save:
                    pygame.image.save(self.__screen, f'pygame_{self.move_idx}.png')

