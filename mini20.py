import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime


events = {
    (2025, 7, 10): "Project Deadline",
    (2025, 7, 15): "Doctor Appointment",
    (2025, 7, 25): "Friend's Birthday"
}

def draw_calendar():
    canvas.delete("all")
    month = months.index(month_cb.get()) + 1
    year = int(year_spin.get())
    first_weekday, num_days = calendar.monthrange(year, month)
   

    today = datetime.today()
    highlight_today = (today.year == year and today.month == month)

    cell_width = 60
    cell_height = 40

    # Draw header row (day names)
    for i, day in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]):
        canvas.create_text(i * cell_width + 30, 15, text=day, font=("Helvetica", 10, "bold"))

    day = 1
    for row in range(6):
        for col in range(7):
            grid_x = col * cell_width
            grid_y = row * cell_height + 30
            cell_id = (year, month, day)

            if (row == 0 and col < first_weekday) or day > num_days:
                continue

            # Highlight today
            if highlight_today and day == today.day:
                canvas.create_rectangle(grid_x, grid_y, grid_x + cell_width, grid_y + cell_height, fill="#a3d2ca", outline="black")
            else:
                canvas.create_rectangle(grid_x, grid_y, grid_x + cell_width, grid_y + cell_height, outline="gray")

            canvas.create_text(grid_x + 30, grid_y + 20, text=str(day))
            canvas.tag_bind(canvas.create_text(grid_x + 30, grid_y + 20, text=str(day)), "<Button-1>", lambda e, d=day: show_event_info(year, month, d))
            day += 1

def show_event_info(y, m, d):
    msg = events.get((y, m, d), "No event for this date.")
    info_label.config(text=f"{d}-{months[m-1]}-{y}: {msg}")

root = tk.Tk()
root.title("Interactive Calendar Picker")

months = list(calendar.month_name)[1:]

month_cb = ttk.Combobox(root, values=months, state="readonly", width=10)
month_cb.current(datetime.today().month - 1)
month_cb.grid(row=0, column=0, padx=5, pady=5)

year_spin = tk.Spinbox(root, from_=1900, to=2100, width=8)
year_spin.delete(0, "end")
year_spin.insert(0, datetime.today().year)
year_spin.grid(row=0, column=1, padx=5, pady=5)

load_btn = tk.Button(root, text="Load Calendar", command=draw_calendar)
load_btn.grid(row=0, column=2, padx=5, pady=5)

canvas = tk.Canvas(root, width=7 * 60, height=6 * 40 + 30, bg="white")
canvas.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

info_label = tk.Label(root, text="Click a date to see notes...", font=("Helvetica", 10), fg="blue")
info_label.grid(row=2, column=0, columnspan=3, pady=5)

draw_calendar()  

root.mainloop()
