from tkinter import *


def button_clicked():
    miles = entry.get()
    try:
        km = round(float(miles) * 1.61, 2)
    except ValueError:
        km = '*invalid*'
    my_label11.config(text=f'{km}')


window = Tk()
window.title("Convert Miles to Km")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

# entry
entry = Entry()
entry.grid(column=1, row=0)
entry.config(width=10)
entry.insert(END, string="0")

# Labeles 1 2 and 3
my_label20 = Label(text="Miles", font=("Arial", 18, 'bold'))
my_label20.grid(column=2, row=0)

my_label01 = Label(text="is equal to", font=("Arial", 18, 'bold'))
my_label01.grid(column=0, row=1)

my_label11 = Label(text="", font=("Arial", 18, 'bold'))
my_label11.grid(column=1, row=1)

my_label21 = Label(text="Km", font=("Arial", 18, 'bold'))
my_label21.grid(column=2, row=1)

# button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)

window.mainloop()
