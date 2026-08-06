from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            s = Turtle(shape="square")
            s.color("white")
            s.penup()
            s.goto(position)
            self.snakes.append(s)

    def move(self):
        for snake_index in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_index - 1].xcor()
            new_y = self.snakes[snake_index - 1].ycor()
            self.snakes[snake_index].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)