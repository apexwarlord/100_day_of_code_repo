from tkinter import *
from math import floor
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
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

window = Tk()
window.title("Pomodoro")
window.config(padx=40, pady=20, bg=YELLOW)
canvas = Canvas(width=220, height=228, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(110, 115, image=tomato_img)
timer_text = canvas.create_text(113, 135, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_pomodoro():
    global reps
    global timer
    try:
        window.after_cancel(timer)
    except ValueError as err:
        print(err)
    label_timer.config(text=f"TIMER", fg=GREEN)
    label_checks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pomodoro():
    global reps
    reps += 1
    if reps % 8 == 0:
        label_timer.config(text=f"BREAK", fg=RED)
        messagebox.showinfo(title="Long break!", message="You can take a long break. You've earned it!.")
        minutes = LONG_BREAK_MIN
    elif reps % 2 == 0:
        label_timer.config(text=f"BREAK", fg=PINK)
        messagebox.showinfo(title="Break time!", message="It's time for a short break.")
        minutes = SHORT_BREAK_MIN
    else:
        label_timer.config(text=f"TIMER", fg=GREEN)
        minutes = WORK_MIN
    countdown(6 * minutes)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    canvas.itemconfig(timer_text, text=f'{floor(count / 60)}:{count % 60:02d}')
    if count > 0:
        global timer
        timer = window.after(30, countdown, count - 1)
    else:
        checks = int(((reps % 8) / 2) + 0.5)
        label_checks.config(text='✔'*checks)
        start_pomodoro()


# ---------------------------- UI SETUP ------------------------------- #


label_timer = Label(text="TIMER", font=('courier', 40, 'bold italic',), bg=YELLOW, fg=GREEN)
label_timer.grid(column=1, row=0)
label_timer.config(pady=10)

button_start = Button(text="START", font=(FONT_NAME, 16, 'normal'))
button_start.grid(column=0, row=2)
button_start.config(command=start_pomodoro)

button_reset = Button(text="RESET", font=(FONT_NAME, 16, 'normal'))
button_reset.grid(column=2, row=2)
button_reset.config(command=reset_pomodoro)

label_checks = Label(text="", bg=YELLOW, fg=GREEN, font=('courier', 45, 'bold'))
label_checks.grid(column=1, row=3)

"""✔✔✔✔✔✔✔✔✔"""

window.mainloop()
