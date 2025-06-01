from turtle import *
from player import Player
from scoreboard import Levels
import time
from cars import CarsManagers

screen = Screen()
screen.setup(height=600 , width=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


player = Player()
g_level = Levels()
screen.listen()
car = CarsManagers()
screen.onkey(player.up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    car.create_car()
    time.sleep(0.1)
    car.move_cars()
    screen.update()
    for car_instance in car.all_cars:
        if player.distance(car_instance) < 20:
            g_level.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.reset_position()
        g_level.update_levels()
        car.increase_speed()

screen.exitonclick()

