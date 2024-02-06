#!/usr/bin/python3
"""N queens task"""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column up to the current row"""
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens_util(board, row, N):
    """function solve queens"""
    if row == N:
        print([[i, board[i].index(1)] for i in range(N)])
        return True
    res = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            res = solve_nqueens_util(board, row + 1, N) or res
            board[row][col] = 0
    return res


def solve_nqueens(N):
    """function solve n queens"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * N for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("No solution exists")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
