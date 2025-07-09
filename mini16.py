from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Employee Shift Scheduler")


emp_frame = Frame(root)
emp_frame.pack()

Label(root, text="Select Employee:").pack()
employee_list = Listbox(emp_frame, height=8)
employee_list.pack(side=LEFT)

emp_scroll = Scrollbar(emp_frame)
emp_scroll.pack(side=RIGHT, fill=Y)
employee_list.config(yscrollcommand=emp_scroll.set)
emp_scroll.config(command=employee_list.yview)

# Sample Employees
employees = ["Anand", "Meena", "Kumar", "Priya", "Suresh", "Lakshmi", "Raj", "Geeta", "Naveen", "Divya"]
for emp in employees:
    employee_list.insert(END, emp)

# Shift Details
Label(root, text="Shift Type:").pack()
shift_combo = ttk.Combobox(root, values=["Morning", "Evening", "Night"])
shift_combo.set("Select Shift")
shift_combo.pack(pady=3)

Label(root, text="Hours Assigned:").pack()
hours_spin = Spinbox(root, from_=1, to=12)
hours_spin.pack(pady=3)

# Shift Assignment Listbox + Scrollbar
shift_frame = Frame(root)
shift_frame.pack()

Label(root, text="Assigned Shifts:").pack()
shift_listbox = Listbox(shift_frame, width=50, height=8)
shift_listbox.pack(side=LEFT)

shift_scroll = Scrollbar(shift_frame)
shift_scroll.pack(side=RIGHT, fill=Y)
shift_listbox.config(yscrollcommand=shift_scroll.set)
shift_scroll.config(command=shift_listbox.yview)

# Assign Logic
def assign_shift():
    selected_emp = employee_list.get(ACTIVE)
    shift = shift_combo.get()
    hours = hours_spin.get()
    if selected_emp and shift != "Select Shift":
        shift_info = f"{selected_emp} → {shift} Shift ({hours} hrs)"
        shift_listbox.insert(END, shift_info)

Button(root, text="Assign Shift", command=assign_shift).pack(pady=5)

root.mainloop()
