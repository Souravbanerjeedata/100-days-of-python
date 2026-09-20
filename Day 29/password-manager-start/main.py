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
# window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

# logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=logo_path)
canvas.create_image(100,100, image=logo_img)
canvas.pack()



window.mainloop()