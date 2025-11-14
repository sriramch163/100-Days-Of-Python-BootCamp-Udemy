from turtle import Turtle
import winsound
import time
import random

# ---------------- SMALL POWER-UP BALL ----------------
class SmallBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gold")
        self.shapesize(0.5)
        self.penup()
        self.hideturtle()
        self.active = False
        self.respawn_delay = 5
        self.next_respawn = None

    def place(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)
        self.showturtle()
        self.active = True

    def collect(self):
        winsound.Beep(900, 100)
        self.hideturtle()
        self.active = False
        self.next_respawn = time.time() + self.respawn_delay

    def check_respawn(self):
        if not self.active and self.next_respawn:
            if time.time() >= self.next_respawn:
                self.place()
                self.next_respawn = None