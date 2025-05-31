
import random

def solve_n_queens_backtracking(n):
    board = [["x"] * n for _ in range(n)]
    solutions = []

    def is_safe(board, row, col):
        for j in range(col):
            if board[row][j] == "Q":
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        x, y = row, col
        while x < n and y >= 0:
            if board[x][y] == "Q":
                return False
            x += 1
            y -= 1

        return True

    def add_solution(board):
        solution = []
        for row in board:
            if "Q" in row:
                solution.append(row.index("Q"))
        solutions.append(solution)

    def solve(board, col):
        if col == n:
            add_solution(board)
            return

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = "Q"
                solve(board, col + 1)
                board[i][col] = "x"  # backtrack

    solve(board, 0)

    print(f"\n🎯 the number of all solutions for n = {n}: {len(solutions)}")
    for idx, sol in enumerate(solutions):
        print(f"answer{idx+1}: {sol}")

    if not solutions:
        return None
    return random.choice(solutions)
