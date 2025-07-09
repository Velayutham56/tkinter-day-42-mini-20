from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Polling App")


polls = {
    "Favorite Fruit": {"Apple": 0, "Banana": 0, "Orange": 0, "Mango": 0},
    "Preferred Language": {"Python": 0, "Java": 0, "C++": 0, "JavaScript": 0},
    "Best Sport": {"Cricket": 0, "Football": 0, "Tennis": 0, "Hockey": 0}
}

current_options = {}

def update_options(event=None):
    question = poll_combo.get()
    options = polls.get(question, {})
    current_options.clear()
    current_options.update(options)
    
    option_listbox.delete(0, END)
    for opt, count in current_options.items():
        option_listbox.insert(END, f"{opt} ({count} votes)")

def submit_vote():
    selected = option_listbox.curselection()
    if selected:
        item_text = option_listbox.get(selected[0])
        opt = item_text.split(" (")[0]
        current_options[opt] += 1
        update_options()

# Combobox for poll questions
poll_combo = ttk.Combobox(root, values=list(polls.keys()))
poll_combo.set("Choose Poll Question")
poll_combo.pack(pady=5)
poll_combo.bind("<<ComboboxSelected>>", update_options)

# Listbox + Scrollbar for options
list_frame = Frame(root)
list_frame.pack()

option_listbox = Listbox(list_frame, height=10, width=40)
option_listbox.pack(side=LEFT)

scroll = Scrollbar(list_frame)
scroll.pack(side=RIGHT, fill=Y)
option_listbox.config(yscrollcommand=scroll.set)
scroll.config(command=option_listbox.yview)


Button(root, text="Submit Vote", command=submit_vote).pack(pady=5)

root.mainloop()
