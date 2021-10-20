from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFB085"
RED = "#8E0505"
GREEN = "#9bdeac"
YELLOW = "#F5F7B2"
BROWN = "#864000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(my_timer)
    # Canvas text
    canvas.itemconfig(timer_text, text="00:00")
    # Head Label
    timer.config(text="Timer", fg=BROWN)
    # Check
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = round(WORK_MIN * 60)
    short_break_sec = round(SHORT_BREAK_MIN * 60)
    long_break_sec = round(LONG_BREAK_MIN * 60)

    if reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        timer.config(text="Work", fg=BROWN)
        countdown(work_sec)

    if reps % 2 == 0 or reps % 8 == 0:
        check["text"] += "🗹"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

# https://colorhunt.co/

window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Timer
timer = Label(text="Timer", font=(FONT_NAME, 22, "bold"))
timer.grid(column=2, row=1)
timer.config(padx=30, bg=YELLOW, fg="#864000")

# Start
start = Button(text="Start", font=(FONT_NAME, 15), command=start_timer)
start.grid(column=1, row=3)
start.config(bg="white", fg="GREEN")

# Reset
reset = Button(text="Reset", font=(FONT_NAME, 15), command=reset_timer)
reset.grid(column=3, row=3)
reset.config(bg="white", fg="GREEN")

# Check
check = Label(font=(FONT_NAME, 25))
check.grid(column=2, row=4)
check.config(bg=YELLOW, fg="#FFB085")

window.mainloop()
