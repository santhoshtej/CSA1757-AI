# Tic Tac Toe Game in Python

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

# Main function to handle the game play
def play_game():
    current_player = "X"
    while True:
        display_board()
        
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        # Place the move on the board
        board[move] = current_player

        # Check if the current player has won
        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break

        # Check if the board is full (a draw)
        if is_board_full():
            display_board()
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
play_game()
