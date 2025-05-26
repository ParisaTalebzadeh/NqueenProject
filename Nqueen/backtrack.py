def solve_n_queens_backtracking(n):
    solutions = []

    def is_safe(queens, row, col):
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row, queens):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens[row] = col
                backtrack(row + 1, queens)

    backtrack(0, [0]*n)
    return solutions[0] if solutions else None
