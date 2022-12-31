from turtle import Turtle,Screen

t = Turtle()


#event listeners
screen = Screen()      #screen object

def move_forwards():
    t.forward(10)

screen.listen()
screen.onkey(key = "space",fun = move_forwards)     #here we do not use () as () will call function instatly and we want that the function will calll once space is clicked

screen.exitonclick()