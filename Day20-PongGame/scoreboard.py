from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.game = "GAME OVER"
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-200, 260)
        self.write(f"Score : {self.l_score}", align="center", font=("Arial", 24, "normal"))
        self.goto(200, 260)
        self.write(f"Score : {self.r_score}", align="center", font=("Arial", 24, "normal"))


    def increase_lscore(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
    def increase_rscore(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))
