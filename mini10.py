from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageGrab

root = Tk()
root.title("Font Preview Tool")

canvas = Canvas(root, width=400, height=200, bg="white")
canvas.pack()

# Font families and default settings
font_families = list(tkFont.families())
text_id = None

def update_preview(event=None):
    global text_id
    font_name = font_combo.get()
    font_size = int(size_spin.get())

    canvas.delete("preview")
    preview_font = (font_name, font_size)
    text_id = canvas.create_text(200, 100, text="The quick brown fox jumps over the lazy dog",
                                 font=preview_font, tags="preview")

def save_image():
    # Coordinates of the canvas relative to screen
    x = root.winfo_rootx() + canvas.winfo_x()
    y = root.winfo_rooty() + canvas.winfo_y()
    x1 = x + canvas.winfo_width()
    y1 = y + canvas.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("font_preview.png")

# Font selector
font_combo = ttk.Combobox(root, values=font_families)
font_combo.set("Arial")
font_combo.pack()
font_combo.bind("<<ComboboxSelected>>", update_preview)

# Size selector
size_spin = Spinbox(root, from_=8, to=72)
size_spin.pack()
size_spin.bind("<KeyRelease>", update_preview)
size_spin.bind("<ButtonRelease-1>", update_preview)

# Save Button
Button(root, text="Save Preview", command=save_image).pack(pady=5)

update_preview()  # Initial draw

root.mainloop()
