### Debugging ###

# Try catch error

# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
#     age = int(input("How old are you? "))

# if age > 18:
#     print(f"You cam drive at the age of {age}.")

# use debugger to find the bug

# import random
# import math

# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1,3)
#         new_item = math.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])