import tkinter as tk

window = tk.Tk()
window.title("Animation Playground")


is_paused = False
rect_id = None
speed_var = tk.IntVar(value=50)


top_frame = tk.Frame(window)
top_frame.pack(pady=10)

tk.Label(top_frame, text="Speed (ms):").pack(side="left", padx=5)
speed_spinbox = tk.Spinbox(top_frame, from_=10, to=1000, increment=10, textvariable=speed_var, width=5)
speed_spinbox.pack(side="left", padx=5)

pause_button = tk.Button(top_frame, text="Pause", width=10)
resume_button = tk.Button(top_frame, text="Resume", width=10)
pause_button.pack(side="left", padx=5)
resume_button.pack(side="left", padx=5)


canvas = tk.Canvas(window, width=500, height=300, bg="white")
canvas.pack(pady=10)

position_label = tk.Label(window, text="X: --, Y: --")
position_label.pack()


rect_id = canvas.create_rectangle(10, 100, 60, 150, fill="blue")
rect_speed = 5

def update_position_label(x, y):
    position_label.config(text=f"X: {x}, Y: {y}")

def animate():
    if not is_paused:
        canvas.move(rect_id, rect_speed, 0)
        coords = canvas.coords(rect_id)
        x, y = coords[0], coords[1]
        update_position_label(int(x), int(y))
        if x < canvas.winfo_width():
            delay = speed_var.get()
            window.after(delay, animate)
        else:
            canvas.coords(rect_id, 10, 100, 60, 150) 

def pause():
    global is_paused
    is_paused = True

def resume():
    global is_paused
    if is_paused:
        is_paused = False
        animate()

pause_button.config(command=pause)
resume_button.config(command=resume)


animate()
window.mainloop()
