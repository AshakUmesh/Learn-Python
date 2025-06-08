import tkinter
from tkinter import *
from tkinter import messagebox

import List
import random
windows = Tk()
windows.title("Password Manager")
windows.config(padx=100, pady=50,bg="black")

def add_password():
    """This funtion is used to add password toi a file """
    website_name = website_name_input.get()
    user_name = email_name_input.get()
    password = password_input.get()

    if not website_name or not user_name or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_okay = messagebox.askokcancel(title=website_name, message=f"These are the details entered \n user_name: {user_name}\n password: {password}\n is it okay to save")

    """check if user_name and password are already present in the file"""
    with open("data.txt", "r") as file1:
        existing_data = file1.readlines()
        for line in existing_data:
            if f"| {user_name} | {password}\n" in line:
                messagebox.showerror("Duplicate Password", "This password has already been saved!")
                return
    if is_okay:
        with open("data.txt", mode="a") as file:
            file.write(f"{website_name} | {user_name} | {password}\n")

    password_input.delete(0, END)
    website_name_input.delete(0, END)
    email_name_input.delete(0, END)



def generate_password():
    """This funtion is used to generate password"""

    password_input.delete(0, END)
    lower_case_n = random.randint(4, 6)
    upper_case_n = random.randint(4, 6)
    number_n = random.randint(1, 4)
    specialchar_n = random.randint(1, 3)
    total_n = lower_case_n + upper_case_n + number_n + specialchar_n
    character_list = []
    for n in range(0, 4):
        character_list.append(random.choice(List.alphabetlist))
    for n in range(0, 2):
        character_list.append(random.choice(List.numberlist))
        character_list.append(random.choice(List.symbollist))
        character_list.append(random.choice(List.alphabetlistcapital))
    for total_n in character_list:
        n = random.choice(character_list)
        password = "" + str(n)
        password_input.insert(0, password)


# ----------------------------------------setup UI-----------------------------------------------------
canvas = tkinter.Canvas(width=200, height=224, highlightthickness=0,bg="black")
lock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:",bg="black",fg="white", font=("Segoe UI", 10))
website_label.grid(row=1, column=0)
website_name_input = Entry(width=35)
website_name_input.grid(row=1, column=1, columnspan=2)
website_name_input.focus()
email_name = Label(text="Email/Username:",bg="black",fg="white", font=("Segoe UI", 10))
email_name.grid(row=2, column=0)
email_name_input = Entry(width=35)
email_name_input.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:",bg="black",fg="white", font=("Segoe UI", 10))
password_label.grid(row=3, column=0)
password_input = Entry(width=25)
password_input.grid(row=3, column=1)
password_generate = Button(text="Generate Password",command=generate_password, bg="#5dbea3", fg="white")
password_generate.grid(row=3, column=2)
add_button = Button(text="Add", width=36,command=add_password, bg="#5dbea3", fg="white")
add_button.grid(row=4, column=1, columnspan=2)

windows.mainloop()
