from tkinter import *
from tkinter import ttk, filedialog, simpledialog
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Photo Gallery Viewer")

image_files = []
current_images = []

# --- Load images from folder (you can customize this) ---
def load_images(folder="."):
    global image_files
    image_files.clear()
    for f in os.listdir(folder):
        if f.lower().endswith((".png", ".jpg", ".jpeg")):
            image_files.append(f)
    apply_filter()

# --- Apply filter based on Combobox selection ---
def apply_filter():
    selected_type = filter_combo.get()
    listbox.delete(0, END)
    current_images.clear()
    for f in image_files:
        if selected_type == "All" or f.lower().endswith(selected_type.lower()):
            listbox.insert(END, f)
            current_images.append(f)

# --- Show image on canvas ---
def show_image(event=None):
    selection = listbox.curselection()
    if selection:
        file_name = current_images[selection[0]]
        img_path = os.path.join(".", file_name)
        img = Image.open(img_path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        canvas.image = img_tk
        canvas.create_image(150, 150, image=img_tk)

# --- Delete image ---
def delete_image():
    selection = listbox.curselection()
    if selection:
        file_name = current_images[selection[0]]
        os.remove(file_name)
        load_images()

# --- Rename image ---
def rename_image():
    selection = listbox.curselection()
    if selection:
        old_name = current_images[selection[0]]
        new_name = simpledialog.askstring("Rename", "Enter new name with extension:")
        if new_name:
            os.rename(old_name, new_name)
            load_images()

# --- Widgets ---
filter_combo = ttk.Combobox(root, values=["All", ".jpg", ".png"])
filter_combo.set("All")
filter_combo.pack()
filter_combo.bind("<<ComboboxSelected>>", lambda e: apply_filter())

# Listbox with scrollbar
frame = Frame(root)
frame.pack()
listbox = Listbox(frame, width=40, height=10)
listbox.pack(side=LEFT)

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

listbox.bind("<Double-Button-1>", show_image)

# Canvas display
canvas = Canvas(root, width=300, height=300, bg="gray")
canvas.pack(pady=5)

# Buttons
Button(root, text="Delete Image", command=delete_image).pack(pady=2)
Button(root, text="Rename Image", command=rename_image).pack(pady=2)

load_images()  # Initial load

root.mainloop()
