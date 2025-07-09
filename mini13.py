from tkinter import *
import time
import winsound  

root = Tk()
root.title("Canvas Timer")

canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack()

time_spinbox = Spinbox(root, from_=1, to=300, width=5)
time_spinbox.pack()


timer_running = False
paused = False
remaining_time = 0
circle_id = None
text_id = None

def start_timer():
    global timer_running, paused, remaining_time
    remaining_time = int(time_spinbox.get())
    timer_running = True
    paused = False
    update_timer()

def pause_resume():
    global paused
    paused = not paused
    if not paused:
        update_timer()

def update_timer():
    global remaining_time, circle_id, text_id
    if timer_running and not paused:
        canvas.delete("all")  
        
        radius = int(remaining_time) * 1.5
        circle_id = canvas.create_oval(150 - radius, 150 - radius, 150 + radius, 150 + radius, fill="skyblue")
        text_id = canvas.create_text(150, 150, text=str(remaining_time), font=("Arial", 24))
        remaining_time -= 1
        if remaining_time >= 0:
            root.after(1000, update_timer)
        else:
            winsound.Beep(1000, 500)  
Button(root, text="Start Timer", command=start_timer).pack(pady=5)
Button(root, text="Pause/Resume", command=pause_resume).pack(pady=5)

root.mainloop()
