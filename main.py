from tkinter import *
from tkinter import messagebox
from random import *


window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo)
canvas.grid(column=1, row=0)

#----Password Generator-----

def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)



#----Save Pass----

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) ==0 or len(password) ==0 or len(email) == 0:
        messagebox.showinfo(title="Warning!", message="You left some fields empty.")
    else:

        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Details for password: \n\nWebsite: {website} \nEmail: {email}"
                                                                     f"\nPassword: {password}\n\nDo you want to save them?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----UI Setup----


website = Label(text="Website: ")
website.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1 , columnspan=2)
website_entry.focus()


email = Label(text="Email/Username")
email.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)


password = Label(text="Password")
password.grid(column=0, row=3)

password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)


generate = Button(text="Generate Password", width=15, command=generate_password)
generate.grid(column=2 , row=3)

add = Button(text="Add", width=7, command=save)
add.grid(column=1, row=4, columnspan=2)










window.mainloop()
