from tkinter import messagebox
from tkinter import *
import string
from random import randint, shuffle, choice
import pyperclip
import json

FONT = ("Arial", 10)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_generator():
    pw_entry.delete(0, END)
    letter_chars = string.ascii_uppercase + string.ascii_lowercase
    number_chars = string.digits
    symbol_chars = string.punctuation
    # print(pw_len)
    pw_gen_letters = [choice(letter_chars) for _ in range(randint(8,10))]
    pw_gen_numbers = [choice(number_chars) for _ in range(randint(2,4))]
    pw_gen_symbols = [choice(symbol_chars) for _ in range(randint(2,4))]
    pw_gen_all = pw_gen_letters + pw_gen_numbers + pw_gen_symbols
    shuffle(pw_gen_all)
    password = ''.join(pw_gen_all)
    pw_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = email_entry.get()
    pw = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }

    if not website or not email or not pw:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_save = messagebox.askyesno(title=website, message=f"These are the details entered: \n"
                                                   f"Email/User: {email}\n"
                                                   f"Password: {pw}\n"
                                                   f"Are you sure to save?")
        if is_save:
            try:
                with open("data.json", mode="r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                pw_entry.delete(0, END)

def search():
    website = str(website_entry.get())
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror("Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            pw = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {pw}")
        else:
            messagebox.showwarning("Error", message="No saved Info for this website.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg="white")
window.grid_columnconfigure(1, minsize=120)
window.grid_columnconfigure(2, minsize=80)

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT, bg="white")
website_label.grid(row=1, column=0, sticky='w')
website_entry = Entry(width=27, justify="left")
website_entry.grid(row=1, column=1, sticky='we')

email_label = Label(text="Email/Username:", font=FONT, bg="white")
email_label.grid(row=2, column=0, sticky='w')
email_entry = Entry(width=35, justify="left")
email_entry.grid(row=2, column=1, columnspan=2, sticky='we')

email_entry.insert(0, "rbpalmiano@gmail.com")

def on_focus_in(event):
    if email_entry.get() == "rbpalmiano@gmail.com":
        email_entry.delete(0, END)

def on_focus_out(event):
    if not email_entry.get():  # Only restore if truly empty
        email_entry.insert(0, "rbpalmiano@gmail.com")

email_entry.bind("<FocusIn>", on_focus_in)
email_entry.bind("<FocusOut>", on_focus_out)

#
# email_entry.delete(0, END)

pw_label = Label(text="Password:", font=FONT, bg="white")
pw_label.grid(row=3, column=0,sticky='w')
pw_entry = Entry(width=27)
pw_entry.grid(row=3, column=1, sticky='we')

gen_pw_button = Button(text="Gen PW", command=pw_generator, width=6)
gen_pw_button.grid(row=3, column=2, sticky='we')

add_button = Button(text="Add", width=29, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky='we')

search_button = Button(text="Search", width=6, command=search)
search_button.grid(row=1, column=2, sticky='we')

window.mainloop()