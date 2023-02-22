from tkinter import *
import math
# -------------------------- CONSTANTS ----------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# --------------------------- TIMER RESET -------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
    check_marks.config(text="")
    


# ---------------------------- TIMER MECHANISM ---------------------- #
def start_timer():
    global reps
    reps+=1

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if(reps%8==0):
        title_label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
                
    #if its the 1st/3rd/5th/7th rep:
    elif(reps%2!=0):
        title_label.config(text="work",fg=GREEN)
        count_down(work_sec)
        

    # #if its the 2nd/4th/6th rep:
    else:
        title_label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)




# --------------------------- COUNTDOWN MECHANISM ------------------- #
def count_down(count):
    minute = math.floor(count/60)
    sec = count%60
    if sec<10:
        sec="0"+str(sec)
    if minute<10:
        minute="0"+str(minute)
    
    canvas.itemconfig(timer_text,text=f"{minute}:{sec}")    #canvas item
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1 )
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks+='✔'
        check_marks.config(text=marks)
        


# --------------------------- UI SETUP ------------------------------ #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)

#timer label
title_label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(row = 0, column = 1)


#canvas

canvas = Canvas(width = 200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png") #way to read through a file and get hold of a particular image

canvas.create_image(100,112,image=tomato_img) #canvas item

timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold")) #canvas item


canvas.grid(row=1,column=1)



#start button
Start_button =Button(text="Start",highlightthickness=0,command=start_timer)
Start_button.grid(row = 2,column = 0)

#reset button
Reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
Reset_button.grid(row = 2,column = 2)

#check mark
check_marks = Label(text='',fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3) 

window.mainloop()
