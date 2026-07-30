# import random
# from game_data import data
# from art import logo, vs

# def format_data(account):
#     return f"{account["name"]} -- {account["description"]}, from {account["country"]}"

# def check_answer(guess, a_followers, b_followers):
#     if a_followers > b_followers:
#         return guess == 'a'
#     else:
#         return guess == 'b'

# def play_game():
#     print(logo)
#     game_should_continue = True
#     score = 0

#     account_a = random.choice(data)
#     account_b = random.choice(data)

#     while account_a == account_b:
#         account_b = random.choice(data)

#     while game_should_continue:
#     # Make B become the new A, pick a fresh B
#         account_a = account_b
#         account_b = random.choice(data)
#         while account_a == account_b:
#             account_b = random.choice(data)

#         print(f"Compare A: {format_data(account_a)}.")
#         print(vs)
#         print(f"Against B: {format_data(account_b)}.")

#         guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

#         a_followers = account_a['follower_count']
#         b_followers = account_b['follower_count']
#         is_correct = check_answer(guess, a_followers, b_followers)

#         # clear skin
#         print("\n" * 50 + logo)

#         if is_correct:
#             score += 1
#             print(f"You're right! Current score: {score}")
#         else:
#             print(f"Sorry, that's wrong. Final score: {score}")
#             game_should_continue = False


# # Main game loop
# while True:
#     play_game()
#     again = input("\nDo you want to play again? Type 'y' or 'n':  ").lower()
#     if again != 'y':
#         print("Thankks for playing!")
#         break

# Practice

import random
from art import logo, vs
from game_data import data

def format_data(account):
    return f"{account['name']} -- {account['description']}, from {account['country']}"

def check_answer(followers_a, followers_b, guess):
    if followers_a > followers_b:
        return guess == 'a'
    else:
        return guess == 'b'

def play_game():
    print(logo)
    game_should_continue = True
    score = 0

    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

        followers_a = account_a['follower_count']
        followers_b = account_b['follower_count']
        is_correct = check_answer(followers_a, followers_b, guess)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False


while True:
    play_game()
    again = input("Do you want to play again? Type 'y' or 'n':  ").lower()
    if again != 'y':
        print("Thanks for playing!")
        break
