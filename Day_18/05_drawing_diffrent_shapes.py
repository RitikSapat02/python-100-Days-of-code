from turtle import Turtle,Screen
import random

colors = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]

t = Turtle()

angle = 360

for side in range(3,10):
    t.color(random.choice(colors))
    angle = 360/side
    for i in range(side):
        t.forward(100)
        t.right(angle)