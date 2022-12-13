from tkinter import *
from tkinter import messagebox
from random import *
import json


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


#----Search-----


def find():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error" , message="No data file found")

    else:
        if website in data:
             email = data[website]["email"]
             password = data[website]["password"]
             messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


#----Save Pass----


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
         "email": email,
         "password": password,}

    }

    if len(website) ==0 or len(password) ==0 or len(email) == 0:
        messagebox.showinfo(title="Warning!", message="You left some fields empty.")
    else:

        is_ok = messagebox.askokcancel(title="Confirmation", message=f"Details for password: \n\nWebsite: {website} \nEmail: {email}"
                                                                     f"\nPassword: {password}\n\nDo you want to save them?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ----UI Setup----


website = Label(text="Website: ")
website.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1 ,columnspan=2)
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

search = Button(text="Search", width=15, command=find)
search.grid(column=2, row=1)












window.mainloop()
