from tkinter import *

root = Tk()
root.title("Fitness Repetition Counter")

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

reps_spin = Spinbox(root, from_=1, to=50)
reps_spin.pack()

count_label = Label(root, text="Reps: 0")
count_label.pack()

reps_total = 0
current_rep = 0
running = False
stick_id = None
direction = 1

def draw_stick_figure(x, y):
    global stick_id
    canvas.delete("stick")
    # Head
    stick_id = canvas.create_oval(x-10, y-30, x+10, y-10, fill="black", tags="stick")
    # Body
    canvas.create_line(x, y-10, x, y+30, tags="stick")
    # Arms
    canvas.create_line(x-15, y, x+15, y, tags="stick")
    # Legs
    canvas.create_line(x, y+30, x-10, y+50, tags="stick")
    canvas.create_line(x, y+30, x+10, y+50, tags="stick")

def animate():
    global current_rep, running, direction
    if running and current_rep < reps_total:
        y_offset = 150 - 20 if direction > 0 else 150 + 20
        draw_stick_figure(150, y_offset)
        direction *= -1
        if direction > 0:
            current_rep += 1
            count_label.config(text=f"Reps: {current_rep}")
        root.after(500, animate)
    elif current_rep >= reps_total:
        draw_stick_figure(150, 150)
        count_label.config(text="Workout Complete!")

def toggle_timer():
    global running, reps_total, current_rep
    if not running:
        reps_total = int(reps_spin.get())
        current_rep = 0
        running = True
        animate()
    else:
        running = False
        draw_stick_figure(150, 150)
        count_label.config(text=f"Reps: {current_rep}")

Button(root, text="Start/Stop", command=toggle_timer).pack(pady=5)

draw_stick_figure(150, 150)
root.mainloop()
