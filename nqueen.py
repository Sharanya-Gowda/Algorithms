global N
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def isSafe(board, row, col):
    # Check if there is a queen in the current row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # If all queens are placed successfully
    if col >= N:
        printSolution(board)
        print()  # Blank line between solutions
        return

    # Try placing this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Place queen

            # Recur to place rest of the queens
            solveNQUtil(board, col + 1)

            # Backtrack
            board[i][col] = 0

def solveNQ():
    board = [[0] * N for _ in range(N)]

    solveNQUtil(board, 0)

    #if not any(1 in row for row in board):
    #    print("No solutions exist")


solveNQ()
