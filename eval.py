def evaluate_simple(board, player):
    player_score = [board[i][j] == player for i in range(len(board)) for j in range(len(board))].count(True)
    opponent_score = len(board)**2 - player_score -[board[i][j] == 0 for i in range(len(board)) for j in range(len(board))].count(True)
    return player_score - opponent_score

def get_valid_moves(board, player):
    size = len(board)
    valid_moves = []
    for r in range(size):
        for c in range(size):
            if board[r][c] == 0:
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= size or nc < 0 or nc >= size or board[nr][nc] == player:
                        continue
                    while nr >= 0 and nr < size and nc >= 0 and nc < size and board[nr][nc] != 0:
                        if board[nr][nc] == player:
                            valid_moves.append((r, c))
                            break
                        nr += dr
                        nc += dc
    return valid_moves

def evaluate_improved(board, player):

    opponent = 1 if player == 2 else 2
    size = len(board)
    
    # weights for each square on the board
    weights = [[100, -20, 10, 5, 5, 10, -20, 100],
               [-20, -50, -2, -2, -2, -2, -50, -20],
               [10, -2, -1, -1, -1, -1, -2, 10],
               [5, -2, -1, -1, -1, -1, -2, 5],
               [5, -2, -1, -1, -1, -1, -2, 5],
               [10, -2, -1, -1, -1, -1, -2, 10],
               [-20, -50, -2, -2, -2, -2, -50, -20],
               [100, -20, 10, 5, 5, 10, -20, 100]]

    # number of pieces owned by each player
    player_score = sum([board[i][j] == player for i in range(size) for j in range(size)])
    opponent_score = sum([board[i][j] == opponent for i in range(size) for j in range(size)])
    
    # mobility (number of legal moves)
    player_legal_moves = len(get_valid_moves(board, player))
    opponent_legal_moves = len(get_valid_moves(board, opponent))

    # corners (bonus for occupying corner squares)
    player_corners = sum([board[i][j] == player for i, j in [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]])
    opponent_corners = sum([board[i][j] == opponent for i, j in [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]])

    # weighted sum of features
    player_value = player_score + player_legal_moves + 10 * player_corners# + 100 * player_stability
    opponent_value = opponent_score + opponent_legal_moves + 10 * opponent_corners# + 100 * opponent_stability
    return player_value - opponent_value


