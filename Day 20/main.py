from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Classic")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

snakes = []

for position in starting_positions:
    s = Turtle(shape="square")
    s.color("white")
    s.penup()
    s.goto(position)
    snakes.append(s)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for snake_index in range(len(snakes) - 1, 0, -1):
        new_x = snakes[snake_index - 1].xcor()
        new_y = snakes[snake_index - 1].ycor()
        snakes[snake_index].goto(new_x, new_y)
    snakes[0].forward(20)
    snakes[0].left(90)

screen.exitonclick()