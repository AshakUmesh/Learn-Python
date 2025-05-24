from turtle import *
import random

my_turtle = Turtle()
my_turtle.speed(2)
my_turtle.setposition(-10,0)
my_turtle.shape("arrow")
my_turtle.pensize(5)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
my_turtle.setposition(-20,0)
for i in range(3):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(120)

screen = Screen()
my_turtle.clear()

for i in range(4):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(90)
my_turtle.clear()

for i in range(5):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(72)
my_turtle.clear()

for i in range(6):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(60)
my_turtle.clear()

for i in range(7):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(360/7)
my_turtle.clear()

for i in range(8):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(360/8)
my_turtle.clear()

for i in range(9):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(360/9)
my_turtle.clear()

for i in range(10):
    my_turtle.color(random.choice(colours))
    my_turtle.forward(100)
    my_turtle.left(36)
my_turtle.clear()

screen.exitonclick()