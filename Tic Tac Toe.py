import math

# Board setup
board = [' ' for _ in range(9)]  # 3x3 Tic-Tac-Toe board

# Display the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a winner
def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diags
    ]
    for condition in win_conditions:
        if all(brd[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_full(brd):
    return ' ' not in brd

# Minimax algorithm with Alpha-Beta Pruning
def minimax(brd, depth, is_maximizing, alpha, beta):
    if check_winner(brd, 'O'):
        return 1
    elif check_winner(brd, 'X'):
        return -1
    elif is_full(brd):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                eval = minimax(brd, depth + 1, False, alpha, beta)
                brd[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                eval = minimax(brd, depth + 1, True, alpha, beta)
                brd[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

# Get the best move for the AI
def best_move():
    best_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Main game loop
def play():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Human move
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board()

        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI is making a move...")
        ai_move = best_move()
        board[ai_move] = 'O'
        print_board()

        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play()
