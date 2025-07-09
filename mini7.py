from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Drawing Game")

# Canvas setup
canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Object selector
shape_combo = ttk.Combobox(root, values=["Star", "Ball", "Square"])
shape_combo.set("Select Shape")
shape_combo.pack()

# Log listbox + scrollbar
log_frame = Frame(root)
log_frame.pack()
log_listbox = Listbox(log_frame, width=50, height=10)
log_listbox.pack(side=LEFT)
scroll = Scrollbar(log_frame)
scroll.pack(side=RIGHT, fill=Y)
log_listbox.config(yscrollcommand=scroll.set)
scroll.config(command=log_listbox.yview)

# Tracking drawings
drawn_objects = []

def draw_shape(event):
    shape = shape_combo.get()
    x, y = event.x, event.y
    item = None

    if shape == "Ball":
        item = canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")
    elif shape == "Square":
        item = canvas.create_rectangle(x-10, y-10, x+10, y+10, fill="green")
    elif shape == "Star":
        item = canvas.create_polygon(x, y-10, x+5, y, x, y+10, x-5, y, fill="gold")

    if item:
        drawn_objects.append(item)
        log_listbox.insert(END, f"{shape} at ({x},{y})")

def undo_last():
    if drawn_objects:
        canvas.delete(drawn_objects.pop())
        log_listbox.delete(END)

canvas.bind("<Button-1>", draw_shape)

Button(root, text="Undo", command=undo_last).pack()

root.mainloop()
