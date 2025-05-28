from turtle import *

# W->move forward ,S->move backward ,A->to move counterclockwise ,d->to move clockwise
my_turtle = Turtle()
screen = Screen()
my_turtle.speed(5)


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def move_left():
    my_turtle.left(10)


def move_right():
    my_turtle.right(10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun = clear)
screen.exitonclick()
