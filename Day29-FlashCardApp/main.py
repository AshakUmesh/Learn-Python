from tkinter import *
import pandas
import random

data = pandas.read_csv("data/kannada_english_hindi_words.csv")
word_list = data.to_dict(orient="records")
current_word = {}

BACKGROUND_COLOR = "#B1DDC6"
windows = Tk()
windows.title("Flashy")
windows.configure(bg=BACKGROUND_COLOR, pady=50, padx=50)


def display_new_word():
    global current_word, flip_timer
    windows.after_cancel(flip_timer)
    current_word = random.choice(word_list)
    canvas.itemconfig(card_title, text="Kannada", fill="black")
    canvas.itemconfig(card_word, text=current_word["Kannada"], fill="black")
    canvas.itemconfig(card_bg, image=old_image)
    flip_timer = windows.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="Hindi", fill="white")
    canvas.itemconfig(card_word, text=current_word["Hindi"], fill="white")
    canvas.itemconfig(card_bg, image=new_image)


def correct():
    global word_list, current_word
    word_list.remove(current_word)
    data_to_learn = pandas.DataFrame(word_list)
    data_to_learn.to_csv("data/word_to_learn.csv", index=False)
    display_new_word()


def wrong():
    display_new_word()


# -------------------------------------------UI------------------------------------------------
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=new_image)
card_bg = canvas.create_image(400, 263, image=old_image)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="Kannada", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

right_img = PhotoImage(file="images/right.png")
correct_button = Button(image=right_img, command=correct, highlightthickness=0)
correct_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=wrong, highlightthickness=0)
wrong_button.grid(row=1, column=0)

flip_timer = windows.after(3000, flip_card)
display_new_word()

windows.mainloop()
