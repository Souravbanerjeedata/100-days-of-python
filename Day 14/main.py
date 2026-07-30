### Higher Lower game project ###

import random
from art import logo, vs
from game_data import data

def format_data(account):
    """Return a printable description of the account."""
    return f"{account['name']}-- {account['description']}, from {account['country']}"

def check_answer(guess, a_followers, b_followers):
    """Return True if the guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    print(logo)
    score = 0
    game_should_continue = True

    # First pair
    account_a = random.choice(data)
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    while game_should_continue:
        # Make B become the new A, pick a fresh B
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        is_correct = check_answer(guess, a_followers, b_followers)

        # Clear screen
        print("\n" * 50)
        print(logo)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

# Main loop – asks if you want to play again
while True:
    play_game()
    again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if again != "y":
        print("Thanks for playing!")
        break