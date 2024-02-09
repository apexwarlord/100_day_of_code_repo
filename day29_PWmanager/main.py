from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from pwgen import generate_password

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


# def check_file():
#     if not os.path.exists("data.json"):
#         open("data.json", 'x')

def find_pw():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        messagebox.showerror("Data not found", "No details for the website exist.")
        return
    except FileNotFoundError:
        messagebox.showerror("Data not found", "No details for the website exist.")
        return
    else:
        for website in data.keys():
            if website == entry_website.get().title():
                messagebox.showinfo(title=f"{website} credentials", message=f"Username: {data[website]['username']}\n\n"
                                                                        f"Password: {data[website]['password']}\n"
                                                                            "(password copied to clipboard)")
                pyperclip.copy(data[website]['password'])
                return
        messagebox.showerror("Data not found", "No details for the website exist. Make sure you've entered the name correctly.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    random_pw = generate_password()
    entry_password.delete(0, END)
    entry_password.insert(0, random_pw)
    pyperclip.copy(random_pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():
    addwebsite = entry_website.get()
    addusername = entry_username.get()
    addpassword = entry_password.get()
    new_data = {addwebsite.title(): {
        "username": addusername,
        "password": addpassword,
    }
    }
    if not addwebsite or not addusername or not addpassword:
        messagebox.showerror("MISSING FIELDS!", "Please complete all three fields")
        return
    is_okay = messagebox.askokcancel(title=addwebsite,
                                     message=f"Here are the details you entered:\n\nEmail/username:\n{addusername}"
                                             f"\n\nPassword:\n{addpassword}\n\nDo you want to proceed?")
    if not is_okay:
        return

    try:
        with open("data.json", 'r') as file:
            # read old data
            data = json.load(file)
    except json.decoder.JSONDecodeError:
        data = new_data
    except FileNotFoundError:
        data = new_data
    # update with new data
    else:
        data.update(new_data)

    with open("data.json", 'w') as file:
        # save updated data
        json.dump(data, file, indent=4)

    # with open("data.txt", "w") as file:
    #     file.write(f"{addwebsite} || {addusername} || {addpassword}\n")
    entry_website.delete(0, END)
    entry_password.delete(0, END)
    messagebox.showinfo(title="SUCCESS", message="Your login credentials have been saved.")


# ---------------------------- UI SETUP ------------------------------- #

website = Label(text="Website:", anchor='e')
website.grid(row=1, column=0)

username = Label(text="email/username:")
username.grid(row=2, column=0)

password = Label(text="password:")
password.grid(row=3, column=0)

entry_website = Entry(width=21)
entry_website.grid(row=1, column=1)

entry_username = Entry(width=36)
entry_username.grid(row=2, column=1, columnspan=2)
entry_username.insert(END, "apexchaosliege@gmail.com")

entry_password = Entry(width=21)
entry_password.grid(row=3, column=1)

button_pw = Button(text="Generate Password", width=11, command=gen_pw)
button_pw.grid(row=3, column=2)

button_add = Button(text="Add to Manager", width=28, command=add_pw)
button_add.grid(row=4, column=1, columnspan=2)

button_search = Button(text="Search", width=11, command=find_pw)
button_search.grid(row=1, column=2)

# check_file()

window.mainloop()
