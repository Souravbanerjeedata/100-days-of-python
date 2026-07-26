# import random

# # # random_integer = random.randint(1, 10)
# # # print(random_integer)

# # random_number_0_to_1 = random.random()
# # print(random_number_0_to_1)

# # Task 1: Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.

# # one way:
# # print("Let's do a coin toss!")
# # choice = input("To choose, type 'heads' or 'tails'\n")
# # random_choice = round(random.random() * 10)
# # if random_choice % 2 == 0:
# #     if choice == 'heads':
# #         print("It's a head, you win!")
# #     elif choice == 'tails':
# #         print("It's a head, you loose.")
# # if random_choice % 2 != 0:
# #     if choice == 'tails':
# #         print("It's a tail, you win!")
# #     elif choice == 'heads':
# #         print("It's a tail, you loose.")
# # print(random_choice)

# # alternate way:

# # random_num = random.randint(0,1)
# # choice = input("Coin toss! type 'head' or 'tail'?\n")
# # if random_num == 0:
# #     if choice == 'head':
# #         print("It's a head, you win!")
# #     elif choice == 'tails':
# #         print("It's a head, you loose.")
# # if random_num == 1:
# #     if choice == 'tails':
# #         print("It's a tail, you win!")
# #     elif choice == 'heads':
# #         print("It's a tail, you loose.")

# # You can create a simple collection of ordered items using a Python list. e.g.

# # fruits = ["Cherry", "Apple", "Pear"]

# # or

# # states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # Accessing Items in Lists
# # You can provide the name of the list then a square bracket and then the item index that you want. e.g.

# # states_of_america[0]

# # will give you "Delaware".

# # Remember that everything computer related, the first number we count with is 0 and never 1. 0, 1, 2, 3 instead of 1, 2, 3 4.

# # Negative Indices
# # You can access items in the list counting from the end of the list by using negative whole numbers. e.g.

# # fruits = ["Cherry", "Apple", "Pear"]
# # fruits[-1] #this will be "Pear"
# # Modifying Items
# # You can use the same syntax to get hold of items in a List to modify it. e.g.

# # fruits = ["Cherry", "Apple", "Pear"]
# # fruits[0] = "Orange"
# # # fruits will now become ["Orange", "Apple", "Pear"]
# # Adding Items
# # You can add items to the end of a List using the append() function. e.g.

# # fruits = ["Cherry", "Apple", "Pear"]
# # fruits.append("Orange")
# # # fruits will now become ["Cherry", "Apple", "Pear", "Orange"]
# # Lists Documentation
# # You can find the documentation for Python Lists and other List related functions here: https://docs.python.org/3/tutorial/datastructures.html

# # Task: Figure out how to pick a random name from the list of friends.
# # friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# # one way:
# # rand_num = random.randint(0, len(friends) - 1)
# # print(friends[rand_num])

# # Alternate way:
# # print(random.choice(friends))

# # final challenge:
# # You are going to build a Rock, Paper, Scissors game. You will need to use what you have learnt about randomisation and Lists to achieve this.

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# choices = [rock,paper,scissors]
# print(choices[player_choice])
# computer_choice = random.randint(0,2)
# print(f"Computer chose:\n{choices[computer_choice]}")

# if ((player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0)):
#     print("You loose.")
# elif ((player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1)):
#     print('You win!!')
# else:
#     print("It's a draw!")
