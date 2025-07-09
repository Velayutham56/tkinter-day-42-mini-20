import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Color Picker App")


top_frame = tk.Frame(window)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Choose Color:").pack(side="left", padx=5)

color_var = tk.StringVar()
color_combo = ttk.Combobox(top_frame, textvariable=color_var, state="readonly")
color_combo["values"] = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
color_combo.current(0)
color_combo.pack(side="left", padx=5)


status_label = tk.Label(window, text="Click on canvas", font=("Arial", 12))
status_label.pack()


canvas = tk.Canvas(window, width=500, height=400, bg="white")
canvas.pack(pady=10)

cell_size = 20  

def paint(event):
    color = color_combo.get()
    x = event.x - (event.x % cell_size)
    y = event.y - (event.y % cell_size)
    canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill=color, outline=color)
    status_label.config(text=f"Painted ({x},{y}) with {color}")

def erase(event):
    x = event.x - (event.x % cell_size)
    y = event.y - (event.y % cell_size)
    canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill="white", outline="white")
    status_label.config(text=f"Erased color at ({x},{y})")

canvas.bind("<Button-1>", paint)     
canvas.bind("<Button-3>", erase)     

window.mainloop()
