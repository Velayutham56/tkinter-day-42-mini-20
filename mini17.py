from tkinter import *

root = Tk()
root.title("Canvas Grid Game")

canvas = Canvas(root, width=250, height=250, bg="white")
canvas.pack()

# Grid setup
grid_size = 5
cell_size = 50
marked_cells = {}

def draw_grid():
    for row in range(grid_size):
        for col in range(grid_size):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", tags=f"cell_{row}_{col}")

def canvas_click(event):
    col = event.x // cell_size
    row = event.y // cell_size
    key = (row, col)
    if key not in marked_cells:
        x1 = col * cell_size
        y1 = row * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", outline="black")
        marked_cells[key] = True
        log_listbox.insert(END, f"Marked cell: ({row}, {col})")

def reset_grid():
    canvas.delete("all")
    marked_cells.clear()
    log_listbox.delete(0, END)
    draw_grid()

# Log Listbox + Scrollbar
log_frame = Frame(root)
log_frame.pack()
log_listbox = Listbox(log_frame, width=40, height=10)
log_listbox.pack(side=LEFT)

scroll = Scrollbar(log_frame)
scroll.pack(side=RIGHT, fill=Y)
log_listbox.config(yscrollcommand=scroll.set)
scroll.config(command=log_listbox.yview)

# Reset button
Button(root, text="Reset Grid", command=reset_grid).pack(pady=5)

canvas.bind("<Button-1>", canvas_click)
draw_grid()

root.mainloop()
