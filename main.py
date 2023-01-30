from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    checkmarks_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    work_sec = WORK_MIN * 60
    work_range = (1, 3, 5, 7)
    short_break_sec = SHORT_BREAK_MIN * 60
    short_brake_range = (2, 4, 6)
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    if reps in work_range:
        timer_label.config(text="Work", fg=RED)
        count_down(work_sec)
    elif reps in short_brake_range:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text="Break", fg=GREEN)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 1:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        marks = ""
        for sessions in range(math.floor(reps / 2)):
            marks += "✔"
        checkmarks_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=50, bg=YELLOW)

# label1 = Label(image=bg)
# label1.place(x="center", y=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
bg = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=bg)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", width=5, highlightthickness=0, command=start_count)
start_button.grid(row=2, column=0)
restart_button = Button(text="Restart", width=5, highlightthickness=0, command=reset_timer)
restart_button.grid(row=2, column=2)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)
checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmarks_label.grid(row=3, column=1)
window.mainloop()
