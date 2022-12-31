from turtle import Turtle,Screen

t = Turtle()
t.color = "red"

for i in range(4):
    t.forward(100)
    t.right(90)

screen = Screen()
screen.exitonclick()