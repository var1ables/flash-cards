from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('french_words.csv')
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000,func=flip)


def flip():
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image=card_back)


def known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flash Cards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(900, 900)

flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)


card_front = PhotoImage(file='images/card_front.png')
card_background = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR ,highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_back = PhotoImage(file='images/card_back.png')

card_title = canvas.create_text(400,150, text='', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

next_card()

green_check = PhotoImage(file='images/right.png')
right = Button(image=green_check, command=known)
right.grid(row=1, column=1)

red_x = PhotoImage(file='images/wrong.png')
wrong = Button(image=red_x, command=next_card)
wrong.grid(row=1, column=0)

window.mainloop()
