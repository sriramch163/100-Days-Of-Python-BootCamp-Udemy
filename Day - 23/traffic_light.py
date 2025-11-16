from turtle import Turtle
import time

class TrafficLight:

    def __init__(self):
        self.light = Turtle()
        self.light.penup()
        self.light.goto(200, 250)
        self.light.shape("circle")
        self.light.shapesize(2)
        self.state = "green"
        self.last_switch = time.time()

    def update_light(self):
        if time.time() - self.last_switch > 4:
            self.state = "red" if self.state == "green" else "green"
            self.last_switch = time.time()

        if self.state == "red":
            self.light.color("red")
        else:
            self.light.color("green")

    def can_cars_move(self):
        return self.state == "green"
