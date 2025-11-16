import time
#import winsound
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from traffic_light import TrafficLight
from controls import setup_controls


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#2b2b2b")
screen.tracer(0)
screen.title("Crossroads Game")


# Ask user players count
players = screen.numinput("Players", "Enter number of players (1 or 2):", minval=1, maxval=2)

# Create players based on choice
player1 = Player(start_pos=(0, -260), color="white")

player2 = None
if players == 2:
    player2 = Player(start_pos=(-50, -260), color="cyan")

cars = CarManager()
scoreboard = Scoreboard()
traffic_light = TrafficLight()

# Setup controls
setup_controls(screen, player1, player2)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Traffic light
    traffic_light.update_light()

    # Car creation + movement
    cars.create_car()
    cars.move_cars(traffic_light.can_cars_move())

    # Check collision for player1
    for car in cars.all_cars:
        if car.distance(player1) < 20:
            #winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            game_is_on = False
            scoreboard.game_over()

        # Check player2 collision if exists
        if player2 is not None and car.distance(player2) < 20:
            #winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
            game_is_on = False
            scoreboard.game_over()

    # Level-up logic
    if player1.is_at_finish_line():
        #winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        player1.goto_start()
        cars.level_up()
        scoreboard.increase_level()

    if player2 is not None:
        if player2.is_at_finish_line():
            #winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            player2.goto_start()
            cars.level_up()
            scoreboard.increase_level()

screen.mainloop()
