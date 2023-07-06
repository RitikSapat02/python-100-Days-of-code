from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500,height=300)

#Label comp
# onent
my_label = Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack()
# my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(expand = True)

my_label["text"] = "New Text"  #text is a keyword argument
my_label.config(text = "New text")

#button component

def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)
    print()

button = Button(text = "click me" ,command=button_clicked)
button.pack() #pack the component on screen

#Entry component
entry = Entry(width = 30)
entry.insert(END,string="Some text to begin with.")
entry.pack()

#Textbox component
text = Text(height=5,width=30)
text.focus()   #puts cursor in textbox.
text.insert(END,"Example of multi-line text entry.")   #add some text to begin with
print(text.get("1.0",END))
text.pack()

#spinbox component
def spinbox_used():
    print(spinbox.get()) #get current value in spinbox.

spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
spinbox.pack()


#scale component
def scale_used(value):
    print(value)

scale = Scale(from_ = 0,to=100,command=scale_used)
scale.pack()

#checkbutton
def checkbutton_used():
    '''prints 1 if On button checked,otherwise 0'''
    print(check_state.get())

check_state = IntVar() #variable to hold on to checked state,0 is off,1 is on. 
checkbutton = Checkbutton(text="Is on?",variable=check_state,command=checkbutton_used)
check_state.get()
checkbutton.pack()

#radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar() #variable to hold on to which radio button value is checked.
radio_button1 = Radiobutton(text = "Option1",command=radio_used,value=1,variable=radio_state)
radio_button2 = Radiobutton(text = "Option2",command=radio_used,value=2,variable=radio_state)
radio_button1.pack()
radio_button2.pack()

#listbox component
def listbox_used(event):
    '''gets current selection from listbox'''
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height = 4)
fruits = ["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",listbox_used)
listbox.pack()

window.mainloop()