from turtle import *
import random
size_of_gap = int(input("Enter the size of gap required for your spirograph : "))
my_turtle = Turtle()
my_turtle.pensize(2)
screen = Screen()
colormode(255)
my_turtle.speed(30)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    turtle_color = (r,g,b)
    return turtle_color

def draw_spirograph(size_of_gap):
    for i in range(360//size_of_gap):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


draw_spirograph(size_of_gap)


screen.exitonclick()