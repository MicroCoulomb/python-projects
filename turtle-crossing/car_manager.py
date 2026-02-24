from turtle import Turtle
import random

STARTING_SPEED = 5
SPEED_INCREMENT = 10
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_SPEED

    def create_car(self):
        random_spawn = random.randint(1, 6)
        if random_spawn == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            if car.xcor() > -320:
                new_x = car.xcor() - self.car_speed
                car.goto(new_x, car.ycor())
            else:
                self.all_cars.remove(car)

    def increase_speed(self):
        self.car_speed += SPEED_INCREMENT