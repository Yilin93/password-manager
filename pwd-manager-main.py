from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pwd_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    pwd = pwd_entry.get()

    if len(web) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Oops", message="Please enter something valid!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"There are details entered: \nEmail: {email}\n"
                                                  f"Password: {pwd}\nIs it ok to save?")
        if is_ok:
            with open("pwd-manager-User_Info.txt", "a") as datafile:
                datafile.write(f"{web} | {email} | {pwd}\n")

    website_entry.delete(0, END)
    pwd_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="pwd-manager-logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
web_lable = Label(text="Website:")
web_lable.grid(column=0, row=1)

user_lable = Label(text="Email/Username:")
user_lable.grid(column=0, row=2)

pwd_lable = Label(text="Password:")
pwd_lable.grid(column=0, row=3)

# entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "guyilin966688@gmail.com")

pwd_entry = Entry(width=20)
pwd_entry.grid(column=1, row=3)


# buttons
generate_button = Button(text="Generate Password", width=11, command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()