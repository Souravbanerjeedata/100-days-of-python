from tkinter import *
import os

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#e7305b"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "logo.png")
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=logo_path)
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

# Input span
# Labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
username_entry = Entry(width=35)
username_entry.insert(0, 'sourav@email.com')
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text='Generate Password',width=14)
generate_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()