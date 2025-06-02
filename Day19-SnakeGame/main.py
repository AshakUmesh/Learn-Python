from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard



screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


snake_food = Food()
snake = Snake()
snake_score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake.create_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend()
        snake_score.increase_score()
    if 280 < snake.head.xcor() or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake_score.reset_score()
        snake.reset_snake()



    for segment in  snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            snake.reset_snake()
screen.exitonclick()
