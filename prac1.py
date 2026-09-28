# #prac 1 question 1 

def tower_of_hanoi(n,source,auxillary,target):
    if n==1:
        print(f"Move disk 1 from {source} to {target}")
        return

    tower_of_hanoi(n-1,source,target,auxillary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1,auxillary,source,target)

num_discs=3
tower_of_hanoi(num_discs, 'A','B','C')

# # write python code to solve n queens problem

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_n_queens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1
    return False


def print_solution(board):
    for row in board:
        print(' '.join('Q' if col == row else '.' for col in range(len(board))))


n = int(input("Enter number of queens (n): "))
board = [-1] * n

if solve_n_queens(board, 0, n):
    print(f"A solution for {n}-queens problem:")
    print_solution(board)
else:
    print(f"No solution exists for {n}-queens problem.")





#Algorithm:
# 1. Move n-1 disks from the source rod to the auxiliary rod, using the target rod as temporary.
# 2. Move the nth (largest) disk directly from source to target.
# 3. Move the n-1 disks from the auxiliary rod to the target rod, using the source rod as temporary.
# 4. Base case: when only 1 disk remains, move it directly from source to target.
# Explanation:
# Tower of Hanoi is a classic recursion problem in which you move a stack of disks from one rod to another, moving one disk at a time so that a larger disk is never placed on a smaller one.


# Algorithm:
# 1. Represent the board as an array where board[row] = column of the queen placed in that row.
# 2. For each row, try placing a queen in every column.
# 3. A position is safe if no previously placed queen shares the same column or same diagonal with it (is_safe).
# 4. Place the queen, then recursively move to the next row (solve_n_queens).
# 5. If placing in a column does not lead to a solution, undo the placement (backtrack) and try the next column.
# 6. When all n rows are filled, the solution board is printed.
# Explanation:
# The N-Queens problem places N queens on an N x N chessboard so that no two queens attack each other. Backtracking tries to place one queen per row and undoes any placement that leads to a dead end.
