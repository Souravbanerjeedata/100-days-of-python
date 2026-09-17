from tkinter import *

window = Tk()

window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label 
my_label = Label(text="Hello, Sourav!", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(text="Hello.")

def new_button_handler():
    print('New Button')
new_button = Button(text="New Button", command=new_button_handler)
new_button.grid(column=2, row=0)

def button_handler():
    my_label.config(text=input.get())

button = Button(text="Click me", command=button_handler)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3,row=2)

window.mainloop()