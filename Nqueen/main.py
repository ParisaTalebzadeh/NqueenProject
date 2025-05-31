import tkinter as tk
from tkinter import ttk
from board_gui import draw_board
from backtrack import solve_n_queens_backtracking
from csp_solver import solve_n_queens_csp
from genetic import solve_n_queens_genetic

def show_genetic_fields(show: bool):
    if show:
        genetic_frame.grid(row=2, column=0, columnspan=3, pady=5)
    else:
        genetic_frame.grid_remove()

def solve(method: str):
    output_label.config(text="")
    try:
        n_val = int(entry_n.get())
        if n_val < 4:
            output_label.config(text="⚠️ n must be greater than or equal to 4.")
            return

        solution = None

        if method == "Genetic":
            try:
                pop_size = int(entry_population.get())
                max_gen = int(entry_max_gen.get())
                if pop_size <= 0 or max_gen <= 0:
                    raise ValueError
            except ValueError:
                output_label.config(text="⚠️ Please enter valid positive integers for population and generations.")
                return
            sol_genetic = solve_n_queens_genetic(
                n_val,
                pop_size=pop_size,
                generations=max_gen
            )
            if sol_genetic is not None:
                solution = [q - 1 for q in sol_genetic]

        elif method == "Backtracking":
            solution = solve_n_queens_backtracking(n_val)

        else:
            solution = solve_n_queens_csp(n_val)
        if solution is not None and isinstance(solution, list) and len(solution) == n_val:
            draw_board(canvas, n_val, solution)
            output_label.config(text="✅ Solution found.")
        else:
            output_label.config(text="❌ No solution found.")

    except ValueError:
        output_label.config(text="⚠️ Please enter a valid integer for n.")

root = tk.Tk()
root.title("N-Queens Solver")
frame = ttk.Frame(root, padding="10")
frame.pack()

# ------------ Input for board size (n) ------------
ttk.Label(frame, text="n:").grid(row=0, column=0, sticky="w")
entry_n = ttk.Entry(frame, width=5)
entry_n.grid(row=0, column=1, padx=5)

# ------------ Method selection buttons ------------
def on_method_click(m: str):
    show_genetic_fields(m == "Genetic")
    solve(m)

methods = ["Backtracking", "Genetic", "CSP"]
for idx, method in enumerate(methods):
    btn = ttk.Button(frame, text=method, command=lambda m=method: on_method_click(m))
    btn.grid(row=1, column=idx, padx=5, pady=5)

# ------------ Genetic settings frame ------------
genetic_frame = ttk.Frame(frame)

ttk.Label(genetic_frame, text="Population Size:").grid(row=0, column=0, padx=5, sticky="w")
entry_population = ttk.Entry(genetic_frame, width=7)
entry_population.grid(row=0, column=1)
entry_population.insert(0, "100")

ttk.Label(genetic_frame, text="Max Generations:").grid(row=0, column=2, padx=5, sticky="w")
entry_max_gen = ttk.Entry(genetic_frame, width=7)
entry_max_gen.grid(row=0, column=3)
entry_max_gen.insert(0, "500")

show_genetic_fields(False)

# ------------ Canvas for drawing the chessboard ------------
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(pady=10, expand=True, fill="both")

# ------------ Output label ------------
output_label = ttk.Label(root, text="", font=("Helvetica", 11))
output_label.pack(pady=(0, 10))

# ------------ Start the Tkinter main loop ------------
root.mainloop()
