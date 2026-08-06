from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Classic")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    s = Turtle(shape="square")
    s.color("white")
    s.goto(position)

screen.exitonclick()