from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Canvas Whiteboard")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()


shape_listbox = Listbox(root)
shape_listbox.insert(END, "Circle", "Rectangle")
shape_listbox.pack()

color_combo = ttk.Combobox(root, values=["Red", "Green", "Blue"])
color_combo.set("Select Color")
color_combo.pack()

drawn_shapes = []
undo_stack = []
redo_stack = []

def draw_shape(event):
    shape_type = shape_listbox.get(ACTIVE)
    color = color_combo.get()
    x, y = event.x, event.y
    obj = None

    if shape_type == "Circle":
        obj = canvas.create_oval(x-20, y-20, x+20, y+20, fill=color)
    elif shape_type == "Rectangle":
        obj = canvas.create_rectangle(x-20, y-20, x+20, y+20, fill=color)

    if obj:
        drawn_shapes.append(obj)
        undo_stack.append(obj)
        log_listbox.insert(END, f"{shape_type} at ({x},{y})")

def delete_selected():
    index = log_listbox.curselection()
    if index:
        obj_id = drawn_shapes[index[0]]
        canvas.delete(obj_id)
        log_listbox.delete(index[0])
        drawn_shapes.pop(index[0])

def undo():
    if undo_stack:
        obj = undo_stack.pop()
        canvas.itemconfig(obj, state="hidden")
        redo_stack.append(obj)

def redo():
    if redo_stack:
        obj = redo_stack.pop()
        canvas.itemconfig(obj, state="normal")
        undo_stack.append(obj)

def save_canvas():
    canvas.postscript(file="whiteboard.ps")


log_frame = Frame(root)
log_frame.pack()
log_listbox = Listbox(log_frame, width=50, height=5)
log_listbox.pack(side=LEFT)
scroll = Scrollbar(log_frame)
scroll.pack(side=RIGHT, fill=Y)
log_listbox.config(yscrollcommand=scroll.set)
scroll.config(command=log_listbox.yview)

# Buttons
Button(root, text="Delete", command=delete_selected).pack(pady=2)
Button(root, text="Undo", command=undo).pack(pady=2)
Button(root, text="Redo", command=redo).pack(pady=2)
Button(root, text="Save", command=save_canvas).pack(pady=2)

canvas.bind("<Button-1>", draw_shape)

root.mainloop()
