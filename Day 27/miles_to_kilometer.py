from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=200, height=100)
window.config(padx=30, pady=20)

entry = Entry(width=10)
entry.grid(row=0, column=1)

miles_unit_label = Label(text="Miles")
miles_unit_label.config(padx=10)
miles_unit_label.grid(row=0,column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_label = Label(text="0")
km_label.config(padx=10)
km_label.grid(row=1, column=1)

km_unit_label = Label(text="Km")
km_unit_label.grid(row=1, column=2)

def converter():
    miles = int(entry.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")
calculate_button = Button(text="Calculate", command=converter)
calculate_button.grid(row=2, column=1)

window.mainloop()