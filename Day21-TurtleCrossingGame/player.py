from turtle import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.reset_position()

    def up(self):
        self.forward(10)

    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(0, -280)


