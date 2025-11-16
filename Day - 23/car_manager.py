from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "white", "cyan"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2




class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))

            new_car.shapesize(random.uniform(0.8, 1.5), random.uniform(1.5, 2.5))

            random_y = random.randint(-200, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self, can_move):
        if can_move:
            for car in self.all_cars:
                car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
