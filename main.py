from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
texts = {}
stored_words = []

# ---------------------------- DATA EXTRACTION ------------------------------- #
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
    if data.empty: #empty(self) return a bool
        raise ValueError("All words Learned")
except (FileNotFoundError, ValueError):
    data = pandas.read_csv('./data/french_words.csv')

data_list = data.to_dict(orient='records')

# ---------------------------- DATA POPULATION FUNCTIONS ------------------------------- #
def show_fr():
    global texts, flip_effect
    window.after_cancel(flip_effect)

    if len(stored_words) == len(data_list):
        canvas.itemconfig(title, text="Done!", fill='black')
        canvas.itemconfig(word_text, text="All words learned!", fill='black')
        canvas.itemconfig(canvas_background, image=fr_image)
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")
        return

    texts = random.choice(data_list)
    while texts['French'] in stored_words:
        texts = random.choice(data_list)

    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word_text, text=texts['French'], fill='black')
    canvas.itemconfig(canvas_background, image=fr_image)
    flip_effect = window.after(3000, show_en)

def show_en():
    global texts
    canvas.itemconfig(canvas_background, image=en_image)
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word_text, text=texts['English'], fill='white')

# ---------------------------- LISTENER FUNCTIONS ------------------------------- #
def right_clicked():
    global texts
    stored_words.append(texts)
    show_fr()
    remove_known_words()

def wrong_clicked():
    show_fr()

# ---------------------------- REMOVE AND UPDATE CSV ------------------------------- #
def remove_known_words():
    data_list.remove(texts)
    words_to_learn = pandas.DataFrame(data_list)
    words_to_learn.to_csv('./data/words_to_learn.csv', index=False)
    # index=False = to not add the index numbers everytime when the words are stored in the csv file.

# ---------------------------- UI DESIGN ------------------------------- #
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_effect = window.after(3000, show_en)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

#Card Background:
fr_image = PhotoImage(file='./images/card_front.png')
canvas_background = canvas.create_image(400, 264, image=fr_image)
en_image = PhotoImage(file='./images/card_back.png')
canvas.grid(column=0, row=1, columnspan=2)

#Card Labels:
title = canvas.create_text(400, 150, text='Title', font=("Ariel", 40, 'italic'))
word_text = canvas.create_text(400, 250, text='Word', font=("Ariel", 60, 'bold'))

#Buttons:
right_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_clicked)
right_button.grid(column=1, row=2, pady=10)

wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong_clicked)
wrong_button.grid(column=0, row=2, pady=10)

show_fr()

window.mainloop()