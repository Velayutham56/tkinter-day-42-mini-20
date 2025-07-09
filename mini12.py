from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Customer Feedback Collector")


feedback_list = []


def submit_feedback():
    name = name_entry.get()
    msg = message_entry.get()
    category = category_combo.get()
    if name and msg and category:
        entry = f"{category} - {name}: {msg}"
        feedback_list.append((category, entry))
        feedback_box.insert(END, entry)
        name_entry.delete(0, END)
        message_entry.delete(0, END)


def filter_feedback():
    selected = category_combo.get()
    feedback_box.delete(0, END)
    for cat, text in feedback_list:
        if cat == selected:
            feedback_box.insert(END, text)


Label(root, text="Name:").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Message:").pack()
message_entry = Entry(root)
message_entry.pack()

category_combo = ttk.Combobox(root, values=["Service", "Product", "Delivery"])
category_combo.set("Select Category")
category_combo.pack()

Button(root, text="Submit", command=submit_feedback).pack(pady=5)
Button(root, text="Filter by Category", command=filter_feedback).pack()


frame = Frame(root)
frame.pack()
feedback_box = Listbox(frame, width=60, height=10)
feedback_box.pack(side=LEFT)
scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)
feedback_box.config(yscrollcommand=scroll.set)
scroll.config(command=feedback_box.yview)

root.mainloop()
