from turtle import Turtle
#import winsound

MOVE_DISTANCE = 20
JUMP_DISTANCE = 40
FINISH_LINE_Y = 260


class Player(Turtle):

    def __init__(self, start_pos, color):
        super().__init__()
        self.shape("turtle")
        self.color(color)
        self.penup()
        self.setheading(90)
        self.start_pos = start_pos
        self.goto_start()

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        #winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

    def go_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def jump(self):
        self.forward(JUMP_DISTANCE)
        #winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

    def goto_start(self):
        self.goto(self.start_pos)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
