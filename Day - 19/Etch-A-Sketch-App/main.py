from turtle import Turtle, Screen

t = Turtle()
s = Screen()

# --- Control flags ---
move_forward = False
move_backward = False
turn_left = False
turn_right = False


# --- Movement function ---
def move():
    if move_forward:
        t.forward(10)
    if move_backward:
        t.backward(10)
    if turn_left:
        t.left(10)
    if turn_right:
        t.right(10)
    s.ontimer(move, 100)  # repeat every 100 ms


# --- Key press events ---
def start_forward():
    global move_forward
    move_forward = True

def stop_forward():
    global move_forward
    move_forward = False

def start_backward():
    global move_backward
    move_backward = True

def stop_backward():
    global move_backward
    move_backward = False

def start_left():
    global turn_left
    turn_left = True

def stop_left():
    global turn_left
    turn_left = False

def start_right():
    global turn_right
    turn_right = True

def stop_right():
    global turn_right
    turn_right = False


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


# --- Bind keys ---
s.listen()
s.onkeypress(start_forward, "w")
s.onkeyrelease(stop_forward, "w")
s.onkeypress(start_backward, "s")
s.onkeyrelease(stop_backward, "s")
s.onkeypress(start_left, "a")
s.onkeyrelease(stop_left, "a")
s.onkeypress(start_right, "d")
s.onkeyrelease(stop_right, "d")
s.onkey(clear_screen, "c")


# --- Start continuous loop after all functions are defined ---
move()

s.exitonclick()
