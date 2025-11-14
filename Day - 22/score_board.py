from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, left_name="Left", right_name="Right"):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.left_name = left_name
        self.right_name = right_name
        self.left_score = 0
        self.right_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        font = ("Courier", 40, "bold")

        self.goto(-150, 200)
        self.write(f"{self.left_name}: {self.left_score}",
                   align="center", font=font)

        self.goto(150, 200)
        self.write(f"{self.right_name}: {self.right_score}",
                   align="center", font=font)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def show_winner(self, winner):
        self.clear()
        self.goto(0, 50)
        self.write(f"Winner: {winner}!", align="center",
                   font=("Courier", 36, "bold"))
        self.goto(0, -20)
        self.write("Click to exit", align="center",
                   font=("Courier", 18, "normal"))
