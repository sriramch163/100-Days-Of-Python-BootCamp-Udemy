from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from small_ball import SmallBall
from score_board import Scoreboard
import time
import winsound


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# ---------------- INPUTS ----------------
left_name = screen.textinput("Player", "Enter LEFT paddle name:") or "Left"
right_name = screen.textinput("Player", "Enter RIGHT paddle name:") or "Right"

points_str = screen.textinput("Play to", "How many points to win? (ex: 10)")
try:
    WINNING_SCORE = int(points_str)
    if WINNING_SCORE <= 0:
        WINNING_SCORE = 10
except:
    WINNING_SCORE = 10

# ---------------- OBJECTS ----------------
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard(left_name, right_name)



small_ball = SmallBall()
small_ball.place()

# ---------------- KEY HOLD SYSTEM ----------------
keys = {"Up": False, "Down": False, "w": False, "s": False}

def press_up(): keys["Up"] = True
def release_up(): keys["Up"] = False
def press_down(): keys["Down"] = True
def release_down(): keys["Down"] = False
def press_w(): keys["w"] = True
def release_w(): keys["w"] = False
def press_s(): keys["s"] = True
def release_s(): keys["s"] = False

screen.listen()
screen.onkeypress(press_up, "Up")
screen.onkeyrelease(release_up, "Up")
screen.onkeypress(press_down, "Down")
screen.onkeyrelease(release_down, "Down")
screen.onkeypress(press_w, "w")
screen.onkeyrelease(release_w, "w")
screen.onkeypress(press_s, "s")
screen.onkeyrelease(release_s, "s")

# ---------------- GAME LOOP ----------------
running = True
while running:

    # Continuous paddle movement
    if keys["Up"]: right_paddle.go_up()
    if keys["Down"]: right_paddle.go_down()
    if keys["w"]: left_paddle.go_up()
    if keys["s"]: left_paddle.go_down()

    small_ball.check_respawn()

    time.sleep(ball.movement)
    screen.update()
    ball.move()

    # Wall bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        winsound.Beep(600, 40)
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        winsound.Beep(750, 40)
        ball.bounce_x()

    # Score detection
    if ball.xcor() > 380:
        winsound.Beep(400, 100)
        ball.reset_game()
        score.left_point()

    if ball.xcor() < -380:
        winsound.Beep(400, 100)
        ball.reset_game()
        score.right_point()

    # Winner check
    if score.left_score >= WINNING_SCORE:
        score.show_winner(left_name)
        break
    if score.right_score >= WINNING_SCORE:
        score.show_winner(right_name)
        break

    # Power-up hit
    if small_ball.active and ball.distance(small_ball) < 30:
        small_ball.collect()
        ball.start_shrink_effect(10)

screen.exitonclick()
