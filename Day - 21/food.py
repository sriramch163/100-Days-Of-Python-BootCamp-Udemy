from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self, food_type="normal"):
        super().__init__()
        self.food_type = food_type
        self.penup()
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

        # Set appearance based on type
        if self.food_type == "normal":
            self.shape("circle")
            self.color("red")
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        elif self.food_type == "bonus":
            self.shape("triangle")
            self.color("gold")
            self.shapesize(stretch_len=0.7, stretch_wid=0.7)

        elif self.food_type == "bomb":
            self.shape("circle")
            self.color("blue")
            self.shapesize(stretch_len=0.8, stretch_wid=0.8)
