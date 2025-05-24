from turtle import *
import random
y_index = 0
my_turtle = Turtle()
screen = Screen()
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r,g,b)
    return turtle_color



for i in range(10):
    for j in range(10):
        my_turtle.color(random_color())
        my_turtle.down()
        my_turtle.dot(20)
        my_turtle.up()
        my_turtle.forward(50)
    y_index += 50
    my_turtle.setposition(0, y_index)

screen.exitonclick()