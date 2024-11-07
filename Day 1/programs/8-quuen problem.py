def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row - 1, -1, -1), range(col + 1, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve(board, row):
    n = len(board)
    if row == n: 
        print_solution(board)  
        return True
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1 
            if solve(board, row + 1):
                return True  
            board[row][col] = 0 
    
    return False 

def solve_8_queens():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)] 
    
    if not solve(board, 0): 
        print("No solution exists.") 
    else:
        print("Solution found!") 

solve_8_queens()
