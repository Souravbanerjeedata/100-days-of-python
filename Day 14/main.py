### Higher Lower game project ###

# TODO-1: IMPORT EVERY DEPENDENCY DATA AND PRINT THE LOGO
from art import logo
from art import vs
from game_data import data
import random

# create random index
def create_a_random():
    return random.randint(0, 49)
# in an empty list store index of each question already asked as reference
asked_question = []

# check if answer was correct and give score
def check_answer(data, score):
    return f""


# TODO-2: CREATE A WHILE LOOP.
game_over = False
while not game_over:
    # CREATE RANDOM INDEXES FOR QUESTIONS
    random_index = create_a_random()
    # CHECK FIRST IF QUESTION WAS ASKED BEFORE. IF YES CHANGE RANDOM INDEX
    if random_index in asked_question:
        random_index = create_a_random()
    # IF NO ASK QUESTION
    else:
        print(f"Compare A: {data[random_index]['name']}, a {data[random_index]['description']}, from {data[random_index]['country']}")
        print("\n" + vs + "\n")
        print(f"Against B: {data}")
        # TODO-3: CHECK FOR CORRECT ANSWER. TOTAL THE SCORE

    # TODO-4: GIVE RESULT AND SCORE 
    # TODO-5: CHECK IF ALL QUESTIONS WERE ASKED IF YES END LOOP
    # TODO-6: FOR WRONG ANSWER END THE LOOP