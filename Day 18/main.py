# Turtle Graphics, Tuple and Importing Modules

from turtle import Turtle, Screen
import random

t = Turtle()

colors = ["silver", "royal blue", "steel blue", "medium sea green", "dark green", "saddle brown", "dark red", "red", "purple", "dark orchid", "dark slate blue"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)


for each_angle in range(3,11):
    t.color(random.choice(colors))
    draw_shape(each_angle)












screen = Screen()
screen.exitonclick()