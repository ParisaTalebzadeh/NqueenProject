import tkinter as tk
from tkinter import ttk
from board_gui import draw_board
from backtrack import solve_n_queens_backtracking
from genetic import solve_n_queens_genetic
from csp_solver import solve_n_queens_csp

def solve(method):
    try:
        n = int(entry.get())
        if n < 4:
            output_label.config(text="n باید >= 4 باشد")
            return
        if method == "Backtracking":
            solution = solve_n_queens_backtracking(n)
        elif method == "Genetic":
            solution = solve_n_queens_genetic(n)
        else:
            solution = solve_n_queens_csp(n)

        if solution:
            draw_board(canvas, n, solution)
            output_label.config(text="solved")
        else:
            output_label.config(text="solution not found")
    except ValueError:
        output_label.config(text="enter the valid number")

root = tk.Tk()
root.title("n-Queens Solver")

frame = ttk.Frame(root, padding="10")
frame.pack()

ttk.Label(frame, text="n :").grid(row=0, column=0)
entry = ttk.Entry(frame, width=5)
entry.grid(row=0, column=1)
entry.insert(0, "8")

for i, method in enumerate(["Backtracking", "Genetic", "CSP"]):
    ttk.Button(frame, text=method, command=lambda m=method: solve(m)).grid(row=1, column=i)

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(pady=10)

output_label = ttk.Label(root, text="")
output_label.pack()

root.mainloop()
