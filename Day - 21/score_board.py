from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, player_name):
        super().__init__()
        self.score = 0
        self.player_name = player_name
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.player_name} | Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, value=1):
        self.score += value
        self.update_scoreboard()

    def decrease_score(self, value=3):
        self.score -= value
        if self.score < 0:
            self.score = 0
        self.update_scoreboard()
