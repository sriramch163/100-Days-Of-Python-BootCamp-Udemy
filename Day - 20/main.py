from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating the Snake
snake = Snake()

# Controls the Snake
snake.control_snake()


# Moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move_snake()





screen.exitonclick()