from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

#Label 
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.config(text = "New text")
my_label.grid(column=0,row=0)
my_label.config(padx=50,pady=50)

#button 
new_button = Button(text="new btn")
new_button.grid(row=0,column=2)

button = Button(text = "click me" ,command=button_clicked)
button.grid(column=1,row=1)

#Entry component
entry = Entry(width = 30)
entry.insert(END,string="Some text to begin with.")
entry.grid(column=3,row=2)

window.mainloop()