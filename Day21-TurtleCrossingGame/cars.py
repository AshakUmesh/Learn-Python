import random
from turtle import *

colormode(255)


class CarsManagers:
    def __init__(self):
        self.all_cars = []
        self.speed = 5

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            new_car.color(self.random_color())
            self.all_cars.append(new_car)

    def random_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += 5