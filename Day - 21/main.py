from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time
import random
from tkinter import simpledialog, messagebox

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Ask player name
player_name = simpledialog.askstring("Player Name", "Enter your name to start the game:")

# Create game objects
snake = Snake()
food = Food("normal")
bonus_food = Food("bonus")
bomb = Food("bomb")
score_board = Scoreboard(player_name)

# Controls
snake.control_snake()

# Game loop
game_is_on = True
last_bomb_time = time.time()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # ---- Normal Food Collision ----
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend_snake(1)
        score_board.increase_score(1)

    # ---- Bonus Food Collision ----
    if snake.head.distance(bonus_food) < 15:
        bonus_food.new_food()
        snake.extend_snake(5)
        score_board.increase_score(5)

    # ---- Bomb Appearance ----
    if time.time() - last_bomb_time > 5:
        bomb.new_food()
        last_bomb_time = time.time()

    # ---- Bomb Collision ----
    if snake.head.distance(bomb) < 15:
        bomb.new_food()
        snake.reduce_snake(3)
        score_board.decrease_score(3)

    # ---- Wall Collision ----
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_is_on = False

    # ---- Self Collision ----
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

# Game Over Message Box
messagebox.showinfo("Game Over", f"Game Over {player_name}! Your final score is {score_board.score}")
screen.bye()
