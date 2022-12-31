from turtle import Turtle,Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    # new_heading = t.heading() + 10
    # t.setheading(new_heading)
    t.left(10)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)
    # t.right(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()                             #listen karo keyboard vagera ko

screen.onkey(move_forwards,"w");
screen.onkey(move_backwards,"s");
screen.onkey(turn_left,"a");
screen.onkey(turn_right,"d");
screen.onkey(clear,"c");
screen.exitonclick()