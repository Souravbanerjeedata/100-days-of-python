from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.fd(10)

def move_backward():
    t.bk(10)

def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.reset()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_right, 'd')
screen.onkey(turn_left, 'a')    
screen.onkey(clear, 'c')    
screen.exitonclick()