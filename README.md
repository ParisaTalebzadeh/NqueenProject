N-Queens Problem Solver
A Python implementation solving the N-Queens puzzle using Backtracking and Genetic Algorithms, visualized with Tkinter GUI.

📖 Overview
The N-Queens problem requires placing N chess queens on an N×N board such that no two queens threaten each other. This project implements two distinct algorithms:

Backtracking - Exhaustively finds all valid solutions.

Genetic Algorithm - Uses evolutionary principles to find a valid solution efficiently.
Solutions are visualized on an interactive chessboard via Tkinter.

⚙️ Features
Backtracking Algorithm

Finds all possible solutions for N queens.

Demonstrates DFS traversal with backtracking.

Genetic Algorithm

Tournament selection, order crossover, and swap mutation.

Configurable parameters (population size, mutation rate, etc.).

Tkinter GUI

Visualizes queens on a colored chessboard.

Toggle between backtracking/genetic solutions.

Dynamic board resizing for any N.

🧠 Algorithms
1. Backtracking
Approach: Depth-First Search (DFS) with backtracking.

Key Functions:

is_safe(): Checks queen placement validity.

solve(): Recursively places queens column-wise.

Output: All valid board configurations.

2. Genetic Algorithm
Workflow:

Initialization: Random population generation.

Fitness Calculation: Counts diagonal conflicts.

Selection: Tournament selection for parents.

Crossover: Order crossover to produce offspring.

Mutation: Random swaps with probability p_mutation.

Exit Condition: Zero conflicts or max generations reached.

🛠️ Requirements
Python 3.x

Libraries: numpy, tkinter

🚀 Installation & Usage
Clone the repository:

bash
git clone https://github.com/<your-username>/n-queens-solver.git  
cd n-queens-solver  
Run the program:

bash
python n_queens_gui.py  
GUI Instructions
Enter N (e.g., 4, 8, 10).

Select an algorithm:

Backtracking: Displays all solutions (use arrows to navigate).

Genetic: Shows solution evolution per generation.

Click Solve to visualize!

🖼️ Sample GUI Output
Backtracking Solution (N=8)	Genetic Algorithm Evolution
Backtracking Solution	Genetic Algorithm
📄 Code Structure
n_queens_backtracking.py: Backtracking implementation.

n_queens_genetic.py: Genetic algorithm implementation.

n_queens_gui.py: Tkinter GUI for visualization.

