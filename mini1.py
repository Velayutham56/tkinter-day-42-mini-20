import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Simple Drawing Tool")


top_frame = tk.Frame(window)
top_frame.pack(side="top", pady=10)


def create_shape(event):
    shape = combo.get()
    color = combocolor.get()
    thickness = int(spinbox.get())
    x, y = event.x, event.y

    if shape == "rectangle":
        canvas.create_rectangle(x-30, y-30, x+30, y+30, outline=color, width=thickness)
    elif shape == "circle":
        canvas.create_oval(x-30, y-30, x+30, y+30, outline=color, width=thickness)
    elif shape == "line":
        canvas.create_line(x-30, y-30, x+30, y+30, fill=color, width=thickness)
    elif shape == "draw":
        
        canvas.create_oval(x, y, x+1, y+1, fill=color, outline=color, width=thickness)


combo = ttk.Combobox(top_frame)
combo["values"] = ["draw", "rectangle", "circle", "line"]
combo.current(0)
combo.pack(side="left", padx=5)


combocolor = ttk.Combobox(top_frame)
combocolor["values"] = ["black", "red", "green", "orange", "lightgray"]
combocolor.current(0)
combocolor.pack(side="left", padx=5)

spinbox = tk.Spinbox(top_frame, from_=1, to=20, increment=1)
spinbox.pack(side="left", padx=5)


canvas = tk.Canvas(window, width=500, height=500, bg='white')
canvas.pack(pady=10)
canvas.bind("<Button-1>", create_shape)  

window.mainloop()
