# from turtle import Turtle, Screen

# t = Turtle()
# screen = Screen()


# def move_forward():
#     t.fd(10)

# def move_backward():
#     t.bk(10)

# def turn_left():
#     new_heading = t.heading() + 10
#     t.setheading(new_heading)

# def turn_right():
#     new_heading = t.heading() - 10
#     t.setheading(new_heading)

# def clear():
#     t.reset()


# screen.listen()
# screen.onkey(move_forward, 'w')
# screen.onkey(move_backward, 's')
# screen.onkey(turn_right, 'd')
# screen.onkey(turn_left, 'a')    
# screen.onkey(clear, 'c')    
# screen.exitonclick()


# turtle race game
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_axis = 50
game_on = False
for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230, y=y_axis)
    y_axis += -30
    turtles.append(t)

if user_bet:
    game_on = True

while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()