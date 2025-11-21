from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global REPS, TIMER
    if TIMER:
        window.after_cancel(TIMER)

    canvas.itemconfig(time_text, text="00:00")
    title_label.config(text="TIMER", fg="black")
    check_marks.config(text="")
    REPS = 0
    TIMER = None

    # Re-enable start button
    start_button.config(state="normal")


# --------------------------------- BEEP SOUND ------------------------------- #

def play_sound():
    winsound.Beep(1000, 500)  # frequency, duration


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1

    # Disable start button so user can't start multiple timers
    start_button.config(state="disabled", bg="#d3d3d3")


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="LONG BREAK", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global TIMER
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        play_sound()
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS / 2)):
            marks += "✅"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=50, bg=YELLOW)

title_label = Label(text="TIMER", fg="black", bg=YELLOW, font=(FONT_NAME, 45, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)  # centered perfectly
time_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg="black", bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(column=1, row=3)

window.mainloop()
