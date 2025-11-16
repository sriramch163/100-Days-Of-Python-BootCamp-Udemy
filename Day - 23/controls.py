def setup_controls(screen, player1, player2):
    screen.listen()

    # Player 1 (Arrow keys)
    screen.onkey(player1.go_up, "Up")
    screen.onkey(player1.go_left, "Left")
    screen.onkey(player1.go_right, "Right")
    screen.onkey(player1.jump, "Down")

    if player2 is not None:
        # Player 2 (WASD keys)
        screen.onkey(player2.go_up, "w")
        screen.onkey(player2.go_left, "a")
        screen.onkey(player2.go_right, "d")
        screen.onkey(player2.jump, "s")
