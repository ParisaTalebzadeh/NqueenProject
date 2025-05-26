def draw_board(canvas, n, queens):
    canvas.delete("all")
    size = min(canvas.winfo_width(), canvas.winfo_height()) // n
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            x0, y0 = j * size, i * size
            x1, y1 = x0 + size, y0 + size
            canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            if queens[i] == j:
                canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="red")
