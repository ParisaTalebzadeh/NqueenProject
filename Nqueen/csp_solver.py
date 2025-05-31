from constraint import Problem, AllDifferentConstraint

def solve_n_queens_csp(n):

    problem = Problem()
    cols = range(n)
    problem.addVariables(cols, cols)

    problem.addConstraint(AllDifferentConstraint())
    def no_diagonal_factory(c1, c2):
        def no_diagonal(q1, q2):
            return abs(q1 - q2) != abs(c1 - c2)
        return no_diagonal
    for i in cols:
        for j in cols:
            if i < j:
                problem.addConstraint(no_diagonal_factory(i, j), (i, j))

    solution = problem.getSolution()

    if solution:
        return [solution[i] for i in range(n)]

    return None
