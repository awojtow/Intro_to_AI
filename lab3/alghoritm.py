
import numpy as np
from heuristisc import heuristics, winning_heuristisc
from cmath import inf
import random
from node import Node
from const import *
'''function  minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −∞
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
        return value
    else (* minimizing player *)
        value := +∞
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
        return value'''

def minimax(node: Node, board, depth, player, strike):
    if depth == 0:
        score = heuristics(board, strike)
        node.score = score 
        return node

    elif board.winning_move(PIECE_MIN, strike) or board.winning_move(PIECE_MAX, strike):
        node.winning = True
        score = winning_heuristisc(player)
        node.score = score
        return node
    elif board.terminal():
        node.terminal = True
        node.score = 0
        node.heuristic_score = 0
        return node


    if player == PLAYER_MIN:
        board_children = board.board_childern(PIECE_MIN)
        node.score = inf
        for (move, child_board) in board_children:
            child_node = Node(board = child_board, move = move, depth = depth - 1)
            child_node  = minimax(child_node, child_board, strike = strike, depth = depth - 1, player = PLAYER_MAX)  
            node.append_child(child_node)
            node.score = min(node.score, child_node.score)

        return node
    elif player == PLAYER_MAX:
        board_children = board.board_childern(PIECE_MAX)
        node.score = -inf
        for (move, child_board) in board_children:
            child_node = Node(board = child_board, move = move, depth = depth - 1)   
            child_node = minimax(child_node, child_board, depth = depth - 1, strike = strike, player = PLAYER_MIN)
            node.append_child(child_node)
            node.score = max(node.score, child_node.score)

        return node


from board import Board




def find_move(root, player):
    final_score = root.children[0].get_score()
    final_move = root.children[0].move

    if player == PLAYER_MIN:
        for child in root.children:
            # print(f"move is {child.move}, with score {child.score}")
            if child.get_score() == final_score:
                if random.random() > 0.5:
                    final_score = child.get_score()
                    final_move = child.move
            elif child.get_score() < final_score:
                final_score = child.get_score()
                final_move = child.move

    if player == PLAYER_MAX:
        for child in root.children:
            # print(f"move  {child.move}, with score {child.score}")
            if child.get_score() == final_score:
                if random.random() > 0.5:
                    final_score = child.get_score()
                    final_move = child.move
            elif child.get_score() > final_score:
                final_score = child.get_score()
                final_move = child.move
    # print(f"FINAL move is {final_move}, with score {final_score}")
    return final_move



def do_minimax(board: Board, depth, player, strike, draw, move_idx):
    root = Node(board = board, depth = depth)
    root = minimax(root, board, depth, player, strike)
    if draw: 
        root.draw_tree(move_idx)
    if root.winning or root.terminal:
        return None
    else:
        return find_move(root, player)
 


