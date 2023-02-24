from tkinter import *
from tkinter import messagebox
import random
import pyperclip




# ------------------- PASSWORD GENERATOR -------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pass():
    password_letters = [random.choice(letters) for i in range(random.randint(8,10))]

    password_numbers = [random.choice(numbers) for i in range(random.randint(2,4))]

    password_symbols = [random.choice(symbols) for i in range(random.randint(2,4))]
    
    password_list = password_letters + password_numbers + password_symbols

    #shuffle the list
    random.shuffle(password_list)

    password = ''.join(password_list)

    
    pass_entry.insert(0,password)
    pyperclip.copy(password)  #copy to clipboard




# -------------------- SAVE PASSWORD ------------------------------ #
def save_data():
    website = website_entry.get()
    user_name = user_name_entry.get()
    password = pass_entry.get()

    if(not user_name or not website or not password ):
        messagebox.showinfo(title="Failed",message="Please don't leave any field Empty!")
        return

    is_ok = messagebox.askokcancel(title="website",message=f"These are the details entered: \nEmail: {user_name}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        with open("data.txt",'a') as data_file:
            data_file.write(f"{website} | {user_name} | {password}\n")
            website_entry.delete(0,END)
            pass_entry.delete(0,END)

# ------------------------ UI SETUP --------------------------------#
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#canvas
canvas = Canvas(width=200,height=200)
img = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=img)

canvas.grid(row=0,column=1)


# Website 
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

website_entry = Entry(width = 42)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

# Email/Username
user_name_label = Label(text="Email/Username:")
user_name_label.grid(row=2,column=0)

user_name_entry = Entry(width = 42)
user_name_entry.insert(0,"ritik@gmail.com")
user_name_entry.grid(row=2,column=1,columnspan=2)

#password
pass_label = Label(text="Password:")
pass_label.grid(row=3,column=0)

pass_entry = Entry(width=24)
pass_entry.grid(row=3,column=1)

#generate password button
generate_btn = Button(text="Generate Password",command=generate_pass)
generate_btn.grid(row=3,column=2)

# add button
add_btn = Button(text="Add",width=36,command=save_data)
add_btn.grid(row=4,column=1,columnspan=2)


window.mainloop()