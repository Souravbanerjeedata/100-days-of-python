from logo import logo
import random

# Global variables
difficulty = {'easy': 10, 'hard': 5}

def get_a_random():
    return random.randint(1, 100)

# check if guess is lower or higher than target number
def compare_difference(guess, random_number):
    if guess > random_number:
        return "Too high."
    if guess < random_number:
        return "Too low."
    else:
        return "correct"

#  Starts
print(logo)
print("\n" + "=" * 90)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
while True:
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if choice in difficulty:
        attempt = difficulty[choice]
        break
    print("Invalid choice. Please type 'easy' or 'hard'.")
    
random_number = get_a_random()
print(random_number) # debugg purposes
game_over = False
while not game_over:
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("make a guess: "))
    attempt -= 1
    result = compare_difference(guess, random_number)

    if result == "correct":
        print("Congratulations!! 🎉🎉")
        print(f"You got it! The number was {random_number}")
        game_over = True
    elif attempt == 0:
        print("You've run out of guesses.")
        print(f"The number was {random_number}.")
        print("Refresh the page to run again.")
        game_over = True
    else:
        print(result)
        print("Guess again.")