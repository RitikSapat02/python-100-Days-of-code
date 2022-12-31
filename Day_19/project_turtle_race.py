from turtle import Turtle,Screen
import random

t = Turtle()
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet",prompt="which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [70,40,10,-20,-50,-80]
all_turtles = []

screen.title("Turtle-bidding game")
screen.bgcolor("black")

for turtle_index in range(6):
    t = Turtle(shape = "turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()