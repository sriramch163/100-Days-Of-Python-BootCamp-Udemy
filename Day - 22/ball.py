from turtle import Turtle
import time
from ball_color import get_random_color

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(get_random_color())
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.movement = 0.1

        self.normal_size = 1.0
        self.small_size = 0.5
        self.shapesize(self.normal_size)

        self.effect_active = False
        self.effect_end_time = None

    def move(self):
        if self.effect_active and time.time() >= self.effect_end_time:
            self.end_shrink_effect()

        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.change_color()

    def bounce_x(self):
        self.x_move *= -1
        self.movement *= 0.9
        self.change_color()

    def reset_game(self):
        self.goto(0, 0)
        self.movement = 0.1
        self.bounce_x()
        self.change_color()

    def change_color(self):
        self.color(get_random_color())

    def start_shrink_effect(self, seconds=10):
        self.effect_active = True
        self.effect_end_time = time.time() + seconds
        self.shapesize(self.small_size)

    def end_shrink_effect(self):
        self.effect_active = False
        self.effect_end_time = None
        self.shapesize(self.normal_size)
