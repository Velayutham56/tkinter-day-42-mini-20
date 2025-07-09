import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Task Manager")


filename = "tasks.txt"


def load_tasks():
    try:
        with open(filename, "r") as f:
            for line in f:
                task_list.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass


def save_tasks():
    with open(filename, "w") as f:
        for i in range(task_list.size()):
            f.write(task_list.get(i) + "\n")


def add_task():
    task = entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Please enter a task")


def remove_task():
    selected = task_list.curselection()
    for i in selected[::-1]:  
        task_list.delete(i)
    save_tasks()


def toggle_completed(event):
    index = task_list.curselection()
    if index:
        idx = index[0]
        current_text = task_list.get(idx)
        if current_text.startswith("[✓] "):
            task_list.delete(idx)
            task_list.insert(idx, current_text[4:])
        else:
            task_list.delete(idx)
            task_list.insert(idx, "[✓] " + current_text)
        save_tasks()


top_frame = tk.Frame(window)
top_frame.pack(pady=10)

entry = tk.Entry(top_frame, width=40)
entry.pack(side="left", padx=5)

add_btn = tk.Button(top_frame, text="Add Task", command=add_task)
add_btn.pack(side="left", padx=5)

remove_btn = tk.Button(window, text="Remove Selected", command=remove_task)
remove_btn.pack(pady=5)


list_frame = tk.Frame(window)
list_frame.pack()

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

task_list = tk.Listbox(list_frame, width=50, height=10, yscrollcommand=scrollbar.set, selectmode=tk.MULTIPLE)
task_list.pack()
scrollbar.config(command=task_list.yview)


task_list.bind("<Double-Button-1>", toggle_completed)

load_tasks()

window.mainloop()
