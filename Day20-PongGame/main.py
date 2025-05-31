import time
from turtle import *
from paddle import Paddle
from ball import PongBall
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = PongBall()
score = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.b_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        score.increase_rscore()

    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        score.increase_lscore()


    if ball.xcor() > 380:
        ball.reset_position()
        score.game_over()
        game_is_on = False


    if ball.xcor() < -380:
        ball.reset_position()
        score.game_over()
        game_is_on = False
screen.exitonclick()
