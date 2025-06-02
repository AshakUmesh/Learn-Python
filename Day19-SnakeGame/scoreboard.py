from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore_maintain") as file:
            content = file.read()
            if content:
                self.highscore = int(content)
            else:
                self.highscore = 0
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  HighScore : {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            with open("highscore_maintain", mode="w") as file:
                file.write(f"{self.highscore}")
            self.update_scoreboard()

