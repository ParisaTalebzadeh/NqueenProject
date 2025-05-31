def draw_board(canvas, n, queens):
    canvas.delete("all")
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    board_size = min(canvas_width, canvas_height)
    cell = board_size / n

    offset_x = (canvas_width - board_size) / 2
    offset_y = (canvas_height - board_size) / 2

    for row in range(n):
        for col in range(n):
            x0 = offset_x + col * cell
            y0 = offset_y + row * cell
            x1 = x0 + cell
            y1 = y0 + cell

            color = "white" if (row + col) % 2 == 0 else "gray"
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

    padding = cell * 0.1
    for col, row in enumerate(queens):
        x0 = offset_x + col * cell + padding
        y0 = offset_y + row * cell + padding
        x1 = x0 + cell - 2 * padding
        y1 = y0 + cell - 2 * padding
        canvas.create_oval(x0, y0, x1, y1, fill="red", outline="black")
