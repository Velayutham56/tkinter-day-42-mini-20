from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Grocery Order Interface")

# Product categories and items
products = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Vegetables": ["Carrot", "Broccoli", "Spinach"],
    "Drinks": ["Water", "Juice", "Soda"]
}

def update_product_list(event):
    category = combo.get()
    product_listbox.delete(0, END)
    for item in products[category]:
        product_listbox.insert(END, item)

def add_to_cart():
    selected = product_listbox.get(ACTIVE)
    quantity = qty_spinbox.get()
    cart_listbox.insert(END, f"{selected} x {quantity}")

# Category selector
combo = ttk.Combobox(root, values=list(products.keys()))
combo.set("Select Category")
combo.pack()
combo.bind("<<ComboboxSelected>>", update_product_list)

# Product Listbox with Scrollbar
frame1 = Frame(root)
frame1.pack()
product_listbox = Listbox(frame1, height=5)
product_listbox.pack(side=LEFT)
scroll1 = Scrollbar(frame1)
scroll1.pack(side=RIGHT, fill=Y)
product_listbox.config(yscrollcommand=scroll1.set)
scroll1.config(command=product_listbox.yview)

# Quantity selector
qty_spinbox = Spinbox(root, from_=1, to=10)
qty_spinbox.pack()

# Add to Cart Button
add_btn = Button(root, text="Add to Cart", command=add_to_cart)
add_btn.pack()

# Cart Listbox with Scrollbar
frame2 = Frame(root)
frame2.pack()
cart_listbox = Listbox(frame2, height=5)
cart_listbox.pack(side=LEFT)
scroll2 = Scrollbar(frame2)
scroll2.pack(side=RIGHT, fill=Y)
cart_listbox.config(yscrollcommand=scroll2.set)
scroll2.config(command=cart_listbox.yview)

root.mainloop()
