from turtle import Turtle

class Levels(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.color("black")
        self.update_levels()

    def update_levels(self):
        self.goto(-230, 240)
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
