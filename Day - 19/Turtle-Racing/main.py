from turtle import Turtle, Screen
import random
import time

# --- Setup Screen ---
screen = Screen()
screen.bgcolor("black")
screen.setup(width=750, height=750)



# --- Game Setup ---
colours = ["red", "orange", "white", "pink", "blue", "green"]
positions = [-250, -150, -50, 50, 150, 250]
participants = []

# --- Let user pick with visible color list ---
color_list = ", ".join(colours)
user_bet = screen.textinput(
    title="🐢 Make Your Bet!",
    prompt=f"Which turtle will win the race?\n\nAvailable colors: {color_list}\n\nEnter a color:"
)

# --- Create Turtles ---
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[index])
    new_turtle.penup()
    new_turtle.goto(x=positions[index], y=-350)
    new_turtle.setheading(90)
    participants.append(new_turtle)

# --- Start Race if User Made a Bet ---
race_on = bool(user_bet)

# --- Race Loop ---
winner = None
while race_on:
    for turtle in participants:
        steps = random.randint(10, 20)
        turtle.forward(steps)

        # 🏁 Check only ONE winner, stop instantly
        if turtle.ycor() > 360:
            winner = turtle.pencolor()
            race_on = False
            break  # stop checking others immediately

# --- Show result ---
if winner:
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.color("white")
    writer.goto(0, 0)
    if winner.lower() == user_bet.lower():
        writer.write(f"🏁 YOU WON!\nThe {winner} turtle is the winner!", align="center", font=("Arial", 18, "bold"))
    else:
        writer.write(f"😢 YOU LOST!\nThe {winner} turtle is the winner!", align="center", font=("Arial", 18, "bold"))

    # Wait 3 seconds then close automatically
    time.sleep(3)
    screen.bye()
