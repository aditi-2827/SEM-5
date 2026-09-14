# def tower_of_hanoi(n,source,auxillary,target):
#     if n==1:
#         print(f"Move disk 1 from {source} to {target}")
#         return

#     tower_of_hanoi(n-1,source,target,auxillary)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n-1,auxillary,source,target)

# num_discs=3
# tower_of_hanoi(num_discs, 'A','B','C')


# write python code to solve n queens problem

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

