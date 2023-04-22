from os import system, name
from math import floor
import random

def list_moves(board:list[list[int]])->list[tuple[int, int]]:
    size = len(board)
    moves = []
    for i in range(0, size):
        for j in range(0, size):
            if board[i][j] == 0:
                moves.append((i, j))
    random.shuffle(moves) #gives a random ordering
    return moves

#initializes board
def initialize_board(player1, player2, size=8)->list[list[int]]:
    board =  [[0 for i in range(size)] for j in range(size)]
    mid = floor(size/2)
    board[mid][mid-1] = player1
    board[mid-1][mid] = player1
    board[mid][mid] = player2
    board[mid-1][mid-1] = player2
    return board

def count(board:list[list[int]], Player:int)->int: #count of a players pieces on board
    size  = len(board)
    count = 0
    for i in range(size):
        for j in range(size):
            if board[i][j] == Player:
                count += 1
    return count

def print_board(board:list[list[int]]): #print board
    size = len(board)
    print("  ", end="")
    for i in range(size):
        print(i, end=" ")
    print()
    for i in range(size):
        print(i, end=" ")
        for j in range(size):
            print(board[i][j], end=" ")
        print()

def check_valid(board, x, y)->bool: #check if a move is valid (empty cell + in boundaries)
    if x<0 or y<0 or x>=len(board) or y>=len(board):
        return False
    if board[x][y] != 0:
        return False
    return True

def check_over(board)->bool: #checks if game is over
    size = len(board)
    for i in range(size):
        for j in range(size):
            if board[i][j] == 0:
                return False
    return True

def check_modify(board, x, y)->bool: #util function for step. if its an occupied cell it has a chance of being flipped over after a move.
    if x<0 or y<0 or x>=len(board) or y>=len(board):
        return False
    if board[x][y] == 0:
        return False
    return True

def step(board : list[list[int]], Player:int, row:int, col:int): #modifies the board after a move. flips pieces accordingly.
    board[row][col] = Player
    directions = [[1, 0], [0, 1], [1, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1]]
    for dir in directions:
      dr = dir[0]
      dc = dir[1]

      tr = row + dr
      tc = col + dc

      while check_modify(board, tr, tc):
        
        if board[tr][tc] == Player:
          while tc != col or tr != row:
            board[tr][tc] = Player
            tr -= dr
            tc -= dc
          break
        tr += dr
        tc += dc
    return board

