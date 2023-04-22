from board import *

#arrays to keep track of ebfs every time an agent is run
random_ebf = []
order_ebf = []

def order_moves(board, moves, evaluate, player):
    """
    Order the given list of valid moves for the given Othello board, based on the
    evaluation function.
    """
    scored_moves = []
    for move in moves:
        new_board = step(board, player, move[0], move[1])
        score = evaluate(new_board, player)
        scored_moves.append((move, score))
    # Sort the moves in descending order of score
    scored_moves.sort(key=lambda x: x[1], reverse=True)
    # Return the ordered list of moves
    return [move for move, score in scored_moves]

def max_value(board, depth, alpha, beta, evaluate, player, ordering=None):
    global node_count
    node_count += 1
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    if depth == 0 or check_over(board):
        return evaluate(board, player), None
    max_value = float('-inf')
    best_move = None
    if ordering is not None:
        moves = ordering(board, list_moves(board), evaluate, player)
    else:
        moves = list_moves(board)
    for move in moves:
        new_board = step(board, player, move[0], move[1])
        value, _ = min_value(new_board, depth - 1, alpha, beta, evaluate, opponent, ordering)
        if value > max_value:
            max_value = value
            best_move = move
            alpha = max(alpha, max_value)
        if max_value >= beta:
            break
    return max_value, best_move

def min_value(board, depth, alpha, beta, evaluate, player, ordering=None):
    global node_count
    node_count += 1
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    if depth == 0 or check_over(board):
        return evaluate(board, player), None
    min_value = float('inf')
    best_move = None
    if ordering is not None:
        moves = ordering(board, list_moves(board), evaluate, player)
    else:
        moves = list_moves(board)
    for move in moves:
        new_board = step(board, player, move[0], move[1])
        value, _ = max_value(new_board, depth - 1, alpha, beta, evaluate, opponent, ordering)
        if value < min_value:
            min_value = value
            best_move = move
            beta = min(beta, min_value)
        if min_value <= alpha:
            break
    return min_value, best_move

def agent(board, player, evaluate, depth=16, ordering=None):
    global node_count
    node_count = 0
    global order_ebf
    global random_ebf
    alpha = float('-inf')
    beta = float('inf')
    new_board = [[cell for cell in row] for row in board] 
    _, move = max_value(new_board, depth, alpha, beta, evaluate, player, ordering)
    if ordering is None:
        random_ebf.append((node_count)**(1/depth))
    else:
        order_ebf.append((node_count)**(1/depth))
    return move
