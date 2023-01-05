def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # The position is safe
    return True

def solve(board, row, N):
    # Base case: all queens have been placed
    if row == N:
        return True

    # Try placing a queen in each column of the current row
    for col in range(N):
        # Check if it is safe to place a queen at board[row][col]
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Move on to the next row
            if solve(board, row + 1, N):
                return True

            # Backtrack: remove the queen and try a different position
            board[row][col] = 0

    # No solution was found
    return False

def n_queens(N):
    # Initialize the board to all zeros
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the problem
    if not solve(board, 0, N):
        print("No solution found.")
        return

    # Print the solution
    for row in board:
        print(row)
n = int(input("Enter matrix:  "))
# Test the n_queens function
n_queens(n)
