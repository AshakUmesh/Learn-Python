import json
from tkinter import *
from tkinter import messagebox

import List
import random
windows = Tk()
windows.title("Password Manager")
windows.config(padx=30, pady=30,bg="black")

def add_password():
    """This funtion is used to add password toi a file """
    website_name = website_name_input.get()
    user_name = email_name_input.get()
    password = password_input.get()
    new_data = {website_name: {"email": user_name,
                              "password": password}}
    if not website_name or not user_name or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_okay = messagebox.askokcancel(title=website_name, message=f"These are the details entered \n user_name: {user_name}\n password: {password}\n is it okay to save")

    """check if user_name and password are already present in the file"""
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            for site, creds in data.items():
                if creds["email"] == user_name and creds["password"] == password:
                    messagebox.showerror("Duplicate Password", "This email & password already exist!")
                    return
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

    if is_okay:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file , indent=4)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        else:
            data.update(new_data)

        with open("data.json", mode="w") as file:
            json.dump(data , file,indent=4)


    password_input.delete(0, END)
    website_name_input.delete(0, END)
    email_name_input.delete(0, END)
def search():
    website_name = website_name_input.get()
    user_name = email_name_input.get()
    with open("data.json", mode="r") as file:
        data = json.load(file)
    if website_name in data and user_name in data[website_name]["email"]:
        email = data[website_name]["email"]
        password = data[website_name]["password"]
        messagebox.showinfo(title=website_name,message=f"Email: {email}\nPassword: {password}")
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for '{website_name}' found.")





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
canvas = Canvas(width=200, height=224, highlightthickness=0, bg="black")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=lock_img)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))


website_label = Label(text="Website:", bg="black", fg="white", font=("Segoe UI", 10))
website_label.grid(row=1, column=0, sticky="e", pady=5)
website_name_input = Entry(width=32)
website_name_input.grid(row=1, column=1, pady=5, sticky="w")
website_name_input.focus()
search_button = Button(text="Search", width=14, command=search, bg="#5dbea3", fg="white")
search_button.grid(row=1, column=2, padx=10, sticky="w")


email_name = Label(text="Email/Username:", bg="black", fg="white", font=("Segoe UI", 10))
email_name.grid(row=2, column=0, sticky="e", pady=5)
email_name_input = Entry(width=51)
email_name_input.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")


password_label = Label(text="Password:", bg="black", fg="white", font=("Segoe UI", 10))
password_label.grid(row=3, column=0, sticky="e", pady=5)
password_input = Entry(width=32)
password_input.grid(row=3, column=1, pady=5, sticky="w")
password_generate = Button(text="Generate Password", width=14, command=generate_password, bg="#5dbea3", fg="white")
password_generate.grid(row=3, column=2, padx=10, sticky="w")


add_button = Button(text="Add", width=43, command=add_password, bg="#5dbea3", fg="white")
add_button.grid(row=4, column=1, columnspan=2, pady=15, sticky="w")


label = Label(text="", bg="black")
label.grid(row=5, column=1, columnspan=2)

windows.mainloop()

