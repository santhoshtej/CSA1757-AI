import math

# Initialize the board
board = [" " for _ in range(9)]

# Function to display the board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if a player has won
def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Minimax algorithm with Alpha-Beta Pruning
def minimax(alpha, beta, is_maximizing):
    if check_winner("O"):  # AI wins
        return 1
    if check_winner("X"):  # Human wins
        return -1
    if is_board_full():    # Draw
        return 0

    if is_maximizing:  # AI's turn to maximize
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cut-off
        return max_eval
    else:  # Human's turn to minimize
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(alpha, beta, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cut-off
        return min_eval

# Function to find the best move for the AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(-math.inf, math.inf, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game function
def play_game():
    while True:
        display_board()

        # Human player (X) move
        try:
            human_move = int(input("Choose your position (1-9): ")) - 1
            if human_move < 0 or human_move > 8 or board[human_move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        board[human_move] = "X"
        if check_winner("X"):
            display_board()
            print("Human wins!")
            break
        if is_board_full():
            display_board()
            print("It's a draw!")
            break

        # AI (O) move
        print("Computer's turn...")
        ai_move = best_move()
        board[ai_move] = "O"
        if check_winner("O"):
            display_board()
            print("Computer wins!")
            break
        if is_board_full():
            display_board()
            print("It's a draw!")
            break

# Start the game
play_game()
