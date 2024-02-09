import time, os
from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    vocab_DF = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    vocab_DF = pandas.read_csv('data/greek_words.csv')

to_learn = vocab_DF.to_dict(orient='records')

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
flash_front = PhotoImage(file="images/card_front.png")
flash_back = PhotoImage(file="images/card_back.png")
flashcard = canvas.create_image(400, 263, image=flash_front)
lang_text = canvas.create_text(400, 150, text="Greek", fill='black', font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Flashcard Word", fill='black', font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


def flip_card():
    canvas.itemconfig(flashcard, image=flash_back)
    word = current_card['english']
    canvas.itemconfig(word_text, text=word, fill="white")
    canvas.itemconfig(lang_text, text='English', fill="white")


def get_random_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    canvas.itemconfig(flashcard, image=flash_front)
    current_card = random.choice(to_learn)
    word = current_card['greek']
    canvas.itemconfig(word_text, text=word, fill='black')
    canvas.itemconfig(lang_text, text='Greek', fill='black')

    flip_timer = window.after(3000, flip_card)


def know_word():
    global to_learn
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        end_of_list()
    else:
        df = pandas.DataFrame(to_learn)
        df.to_csv('data/words_to_learn.csv', index=False)
        get_random_word()

def end_of_list():
    global to_learn, flip_timer
    window.after_cancel(flip_timer)
    b_wrong["state"] = DISABLED
    b_right["state"] = DISABLED
    os.remove('data/words_to_learn.csv')
    canvas.itemconfig(flashcard, image=flash_front)
    canvas.itemconfig(lang_text, text='List Complete!', fill='black')
    canvas.itemconfig(word_text, text='No more words to learn!', fill='black')

cross = PhotoImage(file="images/wrong.png")
b_wrong = Button(image=cross, highlightthickness=0, borderwidth=0, command=get_random_word)
b_wrong.grid(row=1, column=0)

check = PhotoImage(file="images/right.png")
b_right = Button(image=check, highlightthickness=0, borderwidth=0, command=know_word)
b_right.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
get_random_word()

window.mainloop()
