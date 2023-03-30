import requests
import tkinter



window = tkinter.Tk()
window.title("Kanye Quote App")
window.config(padx=50,pady=50)

def quote_generate():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    canvas.itemconfig(Quote,text=data['quote'])

canvas = tkinter.Canvas(width=300,height=414)
Quote = canvas.create_text(150,207,text="Kayne Quote Goes HERE",width=250)
canvas.grid(row=0,column=0)


Button = tkinter.Button(text="Quote",command=quote_generate)
Button.grid(row=1,column=0)


window.mainloop()


