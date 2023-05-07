from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_e = website_entry.get()
    email_e = email_entry.get()
    password_e = password_entry.get()

    if len(email_e) == 0 or len(password_e) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(title=website_e, message=f"These are the details entered: \n "
                                                                f"Email: {email_e} \n "
                                                                f"Password: {password_e} \n Is it okay save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_e} | {email_e} | {password_e} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Canvas & Images
canvas_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(row=0, column=1)

# Label
website = Label(text="Website:")
website.grid(row=1, column=0)

user = Label(text="Email/Username:")
user.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.insert(0, "wizard@icloud.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
