from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Live Scoreboard")

canvas = Canvas(root, width=400, height=200, bg="black")
canvas.pack(pady=10)

# Comboboxes for team names
team_a_combo = ttk.Combobox(root, values=["Team A", "Falcons", "Warriors", "Riders"])
team_a_combo.set("Team A")
team_a_combo.pack()

team_b_combo = ttk.Combobox(root, values=["Team B", "Tigers", "Knights", "Panthers"])
team_b_combo.set("Team B")
team_b_combo.pack()

# Spinboxes for scores
score_a_spin = Spinbox(root, from_=0, to=100, width=5)
score_a_spin.pack()

score_b_spin = Spinbox(root, from_=0, to=100, width=5)
score_b_spin.pack()

def draw_scoreboard():
    canvas.delete("all")
    team_a = team_a_combo.get()
    team_b = team_b_combo.get()
    score_a = score_a_spin.get()
    score_b = score_b_spin.get()

    canvas.create_text(100, 80, text=f"{team_a}: {score_a}", font=("Arial", 24), fill="white")
    canvas.create_text(300, 80, text=f"{team_b}: {score_b}", font=("Arial", 24), fill="white")

def reset_scores():
    score_a_spin.delete(0, END)
    score_b_spin.delete(0, END)
    score_a_spin.insert(0, "0")
    score_b_spin.insert(0, "0")
    draw_scoreboard()

Button(root, text="Reset Scores", command=reset_scores).pack(pady=5)

# Bind updates
team_a_combo.bind("<<ComboboxSelected>>", lambda e: draw_scoreboard())
team_b_combo.bind("<<ComboboxSelected>>", lambda e: draw_scoreboard())
score_a_spin.bind("<KeyRelease>", lambda e: draw_scoreboard())
score_b_spin.bind("<KeyRelease>", lambda e: draw_scoreboard())
score_a_spin.bind("<ButtonRelease-1>", lambda e: draw_scoreboard())
score_b_spin.bind("<ButtonRelease-1>", lambda e: draw_scoreboard())

draw_scoreboard()

root.mainloop()
