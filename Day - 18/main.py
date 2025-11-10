from turtle import Turtle, Screen
import colorgram
import random

t = Turtle()
s = Screen()
s.bgcolor("black")
t.hideturtle()
t.speed("fastest")
t.penup()
s.colormode(255)



rgb_colors = []
colors = colorgram.extract('1.jpg', 6)  # Extract 6 colors from the image

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)







t.goto(-250, -250)

t.setheading(0)
number_of_dots = 101
for dot_count in range(1, number_of_dots):

    t.dot(20, random.choice(rgb_colors))
    t.fd(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.fd(50)
        t.setheading(180)
        t.fd(500)
        t.setheading(0)




s.exitonclick()