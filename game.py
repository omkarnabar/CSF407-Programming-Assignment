from board import *
from agent import *
from eval import *
from time import sleep

def game(p1depth, p2depth, p1eval, p2eval, ordering = None):

    player1 = 1
    player2 = 2

    board = initialize_board(player1, player2)
    #print_board(board)

    game_length = len(board)**2-4
    player =1

    for i in range(game_length):

        if check_over(board):
            break
        
        if player == 1:
            #print("Player 1's turn")
            #x = -1
            #y = -1
            #while not check_valid(board, x, y):
            #    x = int(input("Enter row: "))
            #    y = int(input("Enter column: "))
            #step(board, player, int(x), int(y))
            move = agent(board, player, p1eval, p1depth, ordering)
            if move == None:
                break
            row = move[0]
            col = move[1]
            #print(f"Player 1's turn: ({row}, {col})")
            step(board, player, row, col)
        
        elif player == 2:
            move = agent(board, player, p2eval, p2depth, ordering)
            if move == None:
                break
            row = move[0]
            col = move[1]
            #print(f"Player 2's turn: ({row}, {col})")
            step(board, player, row, col)

        #print_board(board)
        #sleep(10)
        #clear()

        if player == 1:
            player = 2
        else:
            player = 1
    
    #print("Final board state:")
    #print_board(board)

    #print("Game Over!")

    p1cnt = [board[i][j] == player1 for i in range(len(board)) for j in range(len(board))].count(True)
    p2cnt = [board[i][j] == player2 for i in range(len(board)) for j in range(len(board))].count(True)
    if p1cnt > p2cnt:
        #print("Player 1 wins!")
        return 1
    elif p2cnt > p1cnt:
        #print("Player 2 wins!")
        return 2
    else:
        #print("It's a tie!")
        return 0
 

if __name__ == "__main__":
    print("Test different depths")
    runs = 1000
    p1 = 0
    p2 = 0
    t = 0
    for i in range(runs):
        x = game(10, 20, evaluate_simple, evaluate_simple)
        if x ==0:
            t+=1
        elif x==1:
            p1+=1
        else:
            p2+=1

    print(f"Player 1 wins:{p1}")
    print(f"Player 2 wins:{p2}")
    print(f"Ties:{t}")

    print("Test Different Evaluatio Functions")
    runs = 100
    p1 = 0
    p2 = 0
    t = 0
    for i in range(runs):
        x = game(10, 10, evaluate_simple, evaluate_improved)
        if x ==0:
            t+=1
        elif x==1:
            p1+=1
        else:
            p2+=1

    print(f"Player 1 wins:{p1}")
    print(f"Player 2 wins:{p2}")
    print(f"Ties:{t}")

    print("Test Move Ordering")
    import timeit
    exec_time_no_order = timeit.timeit(lambda: game(10, 10, evaluate_simple, evaluate_simple), number = 10)
    exec_time_order = timeit.timeit(lambda: game(10, 10, evaluate_simple, evaluate_simple, order_moves), number = 10)

    print(f"Execution time without ordering: {exec_time_no_order}")
    print(f"Execution time with ordering: {exec_time_order}")

    print("Average EBF without ordering: ", sum(random_ebf)/len(random_ebf))
    print("Average EBF with ordering: ", sum(order_ebf)/len(order_ebf))