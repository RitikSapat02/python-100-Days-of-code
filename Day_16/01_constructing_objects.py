import another_module

print(another_module.another_variable)
import turtle

timmy = turtle.Turtle()            #turtle = module    #Turtle() = class
                                    # timmy is a object of Turtle() class
#from turtle import Turtle()
# tmmy = Turtle()
print(timmy)
timmy.shape("turtle")             #shape() is method
timmy.color("green")              #color() is method
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

my_screen = turtle.Screen()       #Screen = class
print(my_screen.canvheight)
my_screen.exitonclick()              #screen hatao click hote hi
