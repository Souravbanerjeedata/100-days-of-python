#  day 3: conditional statements, logical operator, code blocks and scope

# task 1 : a person can ride a rollercoaster if he/she is over 120 cm tall. print can't ride if below, print can ride if over 120cm tall.

# print("Welcome to the rollercoaster!")
# height = float(input("What is your height in centimeter?\n"))
# if height <= 120:
#     print("Can't ride")
# else:
#     print("Can ride")

# task 2: check if the input number is even or odd

# num = int(input("Enter your number.\n"))
# if num % 2 == 0:
#     print("Your number is an even number")
# else:
#     print("Your number is an odd number")

# Task 3: if higher than 120cm and over 18 then to ride roller coaster pay $12, if 18 or below pay $7.

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?\n"))
# if height > 120:
#     age = int(input("What's your age\n"))
#     if age > 18:
#         print("Please pay $12.")
#     elif age >= 12:
#         print("Please pay $7 to ride.")
#     else:
#         print("Please pay $5 to ride.")
# else:
#     print("You can't ride.")


# task 4
# print("Welcome to python pizza deliveries!")
# size = input("What size pizza do you want? S, M or L?\n")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
# extra_cheese = input("Do you want extra cheese? Y or N?\n")

# todo:  work out how much they need to pay based on their size choice.
# todo: work out how much to add to their bill based on their pepperoni choice.
# todo: work out on their final amount based on whether if they want extra cheese.

# if size == 'S':
#     price = 15
#     if pepperoni == 'Y':
#         price += 2
# if size == 'M':
#     price = 20
#     if pepperoni == 'Y':
#         price += 3
# if size == 'L':
#     price = 25
#     if pepperoni == 'Y':
#         price += 3
# if extra_cheese == 'Y':
#     price += 1

# print(f"Your bill is ${price}.")