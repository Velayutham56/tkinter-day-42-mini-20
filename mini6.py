from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Shape Animation Editor")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

shapes = []
running = False

def create_shape():
    shape = shape_combo.get()
    direction = dir_combo.get()
    speed = int(speed_spin.get())

    x, y = 50, 50
    if shape == "Circle":
        obj = canvas.create_oval(x, y, x+30, y+30, fill="blue")
    elif shape == "Square":
        obj = canvas.create_rectangle(x, y, x+30, y+30, fill="green")
    
    shapes.append({"id": obj, "dir": direction, "speed": speed})

def animate_shapes():
    if not running:
        return
    for shape in shapes:
        dx, dy = 0, 0
        if shape["dir"] == "Right": dx = shape["speed"]
        elif shape["dir"] == "Left": dx = -shape["speed"]
        elif shape["dir"] == "Down": dy = shape["speed"]
        elif shape["dir"] == "Up": dy = -shape["speed"]
        canvas.move(shape["id"], dx, dy)
    root.after(50, animate_shapes)

def start_animation():
    global running
    running = True
    animate_shapes()

def pause_animation():
    global running
    running = False

# Shape selector
shape_combo = ttk.Combobox(root, values=["Circle", "Square"])
shape_combo.set("Select Shape")
shape_combo.pack()

# Direction selector
dir_combo = ttk.Combobox(root, values=["Up", "Down", "Left", "Right"])
dir_combo.set("Direction")
dir_combo.pack()

# Speed control
speed_spin = Spinbox(root, from_=1, to=10)
speed_spin.pack()

# Buttons
Button(root, text="Create Shape", command=create_shape).pack()
Button(root, text="Start", command=start_animation).pack()
Button(root, text="Pause", command=pause_animation).pack()

root.mainloop()
