from turtle import Screen
import time
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()