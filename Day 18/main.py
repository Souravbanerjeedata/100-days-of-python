# # Turtle Graphics, Tuple and Importing Modules

# # from turtle import Turtle, Screen
# # import random

# # t = Turtle()

# # colors = ["silver", "royal blue", "steel blue", "medium sea green", "dark green", "saddle brown", "dark red", "red", "purple", "dark orchid", "dark slate blue"]

# # def draw_shape(num_sides):
# #     angle = 360 / num_sides
# #     for _ in range(num_sides):
# #         t.forward(100)
# #         t.right(angle)


# # for each_angle in range(3,11):
# #     t.color(random.choice(colors))
# #     draw_shape(each_angle)

# # screen = Screen()
# # screen.exitonclick()


# from turtle import Turtle, Screen
# from random import random, choice, randint

# t = Turtle()
# t.colormode(255)

# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# fd_or_bk = ["forword", "backword"]
# left_or_right = ["right", "left"]


# for i in range(100):
#     t.color(random_color())
#     directions = [0, 90, 180, 270]
    
#     t.speed("fastest")
#     t.pensize(15)

#     if choice(left_or_right) == "right":
#         t.right(choice(directions))
#     else:
#         t.left(choice(directions))

#     if choice(fd_or_bk) == 'forword':
#         t.fd(20)
#     else:
#         t.bk(20)
    
    
    





# screen = Screen()
# screen.exitonclick()