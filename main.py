from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./data/french_words.csv")
data_dict = data.to_dict(orient="records")

current_card = {}

try:
    words_to_learn = pd.read_csv('./data/words_to_lean.csv')
except FileNotFoundError:
    words_to_learn = pd.DataFrame(data_dict)
    words_to_learn.to_csv('./data/words_to_lean.csv', index=False)
else:
    words_to_learn_list = words_to_learn.to_dict(orient='records')
    

#-------------------random words-----------------
def french_word():
    global current_card, words_to_learn_list, delay
    windom.after_cancel(delay)
    current_card = random.choice(words_to_learn_list)
    words = current_card['French']
    canvas.itemconfigure(card_image, image = photo_front)
    canvas.itemconfigure(card_word, text = words)
    canvas.itemconfigure(card_text, text = "French")
    delay = windom.after(3000, func=flip_card)
    
    
def flip_card():
    global current_card
    word = current_card['English']
    canvas.itemconfigure(card_image, image = phot0_back)
    canvas.itemconfigure(card_word, text = word)
    canvas.itemconfigure(card_text, text = "English")
    
def is_known():
    global words_to_learn_list, current_card
    words_to_learn_list.remove(current_card)
    words_to_learn_list.to_csv('./data/words_to_lean.csv', index=False)
    french_word()
    
    
    

windom = Tk()
windom.minsize()
windom.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
phot0_back = PhotoImage(file='./images/card_back.png')
photo_front = PhotoImage(file="./images/card_front.png")

card_image = canvas.create_image(400, 263, image = photo_front)
card_text = canvas.create_text(400, 150, text="French", font=("ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Hello', font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

delay = windom.after(3000, french_word)
    

right_icon = PhotoImage(file="./images/right.png")
left_icon = PhotoImage(file="./images/wrong.png")

right_buttom = Button(image=right_icon, command=french_word)
right_buttom.grid(row=1,column=0)

wrong_button = Button(image=left_icon, command=flip_card)
wrong_button.grid(row=1, column=1)
windom.mainloop()


