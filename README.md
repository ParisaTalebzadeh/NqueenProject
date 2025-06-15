---
🧠 N-Queens Problem Solver

A Python implementation solving the N-Queens puzzle using three approaches: Backtracking, Genetic Algorithms, and Constraint Satisfaction Problem (CSP) — all visualized with a Tkinter GUI.
---
📖 Overview

The N-Queens problem requires placing N chess queens on an N×N board such that no two queens threaten each other. That means no two queens can be on the same row, column, or diagonal.

This project implements and visualizes three distinct algorithms:

Backtracking – Exhaustively finds all valid solutions using DFS.

Genetic Algorithm – Uses evolutionary strategies to quickly approximate a solution.

CSP (Constraint Satisfaction Problem) – Models the problem declaratively using constraints and solves using a CSP solver.


All results are visualized on an interactive chessboard via a Tkinter-based GUI.

---
⚙️ Features

✅ Backtracking Algorithm

Exhaustive search to find all valid configurations.

Implements Depth-First Search (DFS) with backtracking.

Clearly illustrates the algorithmic search process.

🧬 Genetic Algorithm

Uses evolutionary computation:

Tournament selection, order crossover, swap mutation.

Parameters are configurable (population size, mutation rate, etc.).

Stops on solution discovery or max generations.


🧩 CSP (Constraint Satisfaction Problem)

Elegant declarative solution using Python-constraint library.

Models the board as variables with:

AllDifferent constraint for row/column uniqueness.

Diagonal constraints using lambda functions.


Efficiently finds a single valid solution.


🖼️ Tkinter GUI

Interactive GUI for entering N and choosing algorithm.

Color-coded chessboard with visual queen placement.

Toggle between Backtracking, Genetic, or CSP.

Dynamic board resizing for any N.

---

🧠 Algorithms

🔁 Backtracking Approach

A classic recursive solution using DFS.

Key Functions:

is_safe(row, col): Verifies whether a queen can be placed.

solve(col): Recursively places queens column-wise.


Output: List of all valid board configurations.

---

🧬 Genetic Algorithm Workflow

Initialization: Random generation of candidate solutions.

Fitness Evaluation: Fewer diagonal conflicts = higher fitness.

Selection: Tournament selection for parent candidates.

Crossover: Order crossover (OX) to produce offspring.

Mutation: Swap mutation with a small probability.

Termination: Stop when a solution has zero conflicts or after max generations.

---

🧩 Constraint Satisfaction Problem (CSP) Approach

Solves the N-Queens problem by declaring constraints instead of writing search logic.

Steps:

1. Each column is a variable (value = row index of queen).


2. Apply AllDifferentConstraint() to ensure no two queens share a row.


3. Add diagonal constraints using:



def no_diagonal_factory(c1, c2):
    def no_diagonal(q1, q2):
        return abs(q1 - q2) != abs(c1 - c2)
    return no_diagonal

4. Solve with problem.getSolution() to obtain one valid placement.

Advantages:

Clean and scalable.

Leverages a CSP solver for constraint propagation and inference.

---

🛠️ Requirements

Python 3.x

Libraries:

numpy

tkinter (comes with Python)

python-constraint (for CSP)



Install required packages via:

pip install numpy python-constraint


---

🚀 Installation & Usage

1. Clone the repository:



git clone https://github.com/yourusername/n-queens-solver.git
cd n-queens-solver

2. Run the GUI:

python n_queens_gui.py
---

🖱️ GUI Instructions

Enter the value of N (e.g., 4, 8, 10).

Select an algorithm:

Backtracking: Shows all solutions (navigate with arrows).

Genetic: Shows live evolution of a solution.

CSP: Shows a single valid solution quickly.


Click Solve to visualize the solution on the chessboard!

---

📄 Code Structure

n_queens_backtracking.py   # Backtracking logic
n_queens_genetic.py        # Genetic algorithm logic
n_queens_gui.py            # GUI and visualization logic
n_queens_csp.py            # CSP solver implementation
