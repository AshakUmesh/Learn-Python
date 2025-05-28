import random
from turtle import *


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
positions = [90, 60, 30, 0, -30, -60, -90]
turtle_list = []
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color : ")
if user_bet:
    is_race_on = True
if user_bet not in colors:
    print("Invalid color entered. Please choose from:", ", ".join(colors))
    is_race_on = False

for color, y_pos in zip(colors, positions):
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-240, y_pos)
    turtle_list.append(t)

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            color = turtle.pencolor()
            if color == user_bet:
                print(f"You won the bet , {color} turtle won ")
                break
            else:
                print(f"you lost the bet , {color} turtle won ")
                break
            print(color)
            break
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
