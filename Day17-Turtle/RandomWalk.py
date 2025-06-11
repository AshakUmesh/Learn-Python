import turtle as t
import random
from turtle import Screen
my_turtle = t.Turtle()
screen = Screen()
my_turtle.speed(10)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
my_turtle.pensize(10)

while True:
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))
    my_turtle.color(random.choice(colours))


