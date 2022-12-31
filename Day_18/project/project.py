import turtle 
import random

color_list = [(202, 163, 98), (45, 97, 147), (168, 49, 80), (222, 210, 108), (141, 92, 64), (118, 172, 203), (173, 163, 40), (210, 133, 171), (208, 67, 105), (223, 78, 56), (91, 106, 193), (143, 33, 60), (31, 139, 94), (57, 172, 105), (124, 218, 205), (228, 170, 186), (47, 186, 197), (126, 191, 168), (100, 50, 42), (34, 61, 117), (223, 208, 22), (148, 207, 225), (169, 187, 225), (233, 173, 163), (49, 57, 66), (41, 75, 78)]

turtle.colormode(255)

t = turtle.Turtle()
t.speed("fastest")
t.penup()                 #dot banate rahega bass pen up rahega line nahi ani chahiye isliye
t.hideturtle()            #hide the turtle


#set the starting position of turtle on screen
t.setheading(225)
t.forward(325)
t.setheading(0)

number_of_dots = 101
for dot_count in range(1,number_of_dots):
    t.dot(20,random.choice(color_list))
    t.forward(50)

    #har 10th dot ke bad new line
    if dot_count%10 == 0:
        #get to new line
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = turtle.Screen()
screen.exitonclick()