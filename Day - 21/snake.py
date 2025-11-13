from turtle import Turtle, Screen

screen = Screen()
SNAKE_POSITIONS = [(0, 0), (-15, 0), (-30, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("lightgreen")
        snake_segment.shapesize(stretch_len=0.8, stretch_wid=0.3)  # Slim snake
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend_snake(self, count=1):
        for _ in range(count):
            self.add_snake(self.segments[-1].position())

    def reduce_snake(self, count=3):
        for _ in range(count):
            if len(self.segments) > 1:
                segment = self.segments.pop()
                segment.hideturtle()

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def control_snake(self):
        screen.listen()
        screen.onkey(self.up, "w")
        screen.onkey(self.down, "s")
        screen.onkey(self.left, "a")
        screen.onkey(self.right, "d")

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
