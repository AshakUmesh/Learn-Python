import tkinter as tk
import math
from playsound import playsound

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def flash_window():
    window.lift()
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)
    window.focus_force()


def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50))
    check_marks.config(text="")



def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 50))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK, font=(FONT_NAME, 50))
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 50))




def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        window.bell()
        flash_window()
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # Add check mark for completed work sessions
        marks = ""
        sessions = math.floor(reps / 2)
        for _ in range(sessions):
            marks += "✓"
        check_marks.config(text=marks)
        start_timer()



window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=3, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=3, column=2)

check_marks = tk.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
check_marks.grid(row=4, column=1)

window.mainloop()
