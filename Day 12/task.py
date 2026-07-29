### Scope & Number guessing game
# Prime Number Checker
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.

# You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.  It should return True or False.

# e.g.
# 7 is a primer number because it is only divisible by 1 and itself.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

# Example Input 1
# 73

# Example Output 1
# True

# Example Input 2
# 75

# Example Output 2
# False

# def is_prime(num):
#     if num == 2:
#         return True
#     if num == 1:
#         return False
 
#     # Loop through all the numbers between 2 and the number
#     for i in range(2, num):
#         # Check if the number (num) can be divided by the potential prime number
#         if num % i == 0:
#             return False
 
#     # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
#     return True

### Final Task: Number Guessing Game ###

# AI solution
# import random
# from logo import logo

# difficulty = {'easy': 10, 'hard': 5}

# def compare_difference(random_number, guess):
#     if random_number > guess:
#         return "Too low."
#     elif random_number < guess:
#         return "Too high."
#     return None  # equal – caller should handle this

# def get_a_random():
#     return random.randint(1, 100)

# print(logo)
# print("\n" + "=" * 90)
# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# # Validate difficulty
# while True:
#     choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
#     if choice in difficulty:
#         attempt = difficulty[choice]
#         break
#     print("Invalid choice. Please type 'easy' or 'hard'.")

# random_number = get_a_random()
# print(random_number)  # ← remove this (debug)

# guess = None
# while attempt > 0:
#     try:
#         guess = int(input("Make a guess: "))
#     except ValueError:
#         print("Please enter a whole number.")
#         continue

#     attempt -= 1

#     if guess == random_number:
#         print("Congratulations! You have guessed right. 🎉")
#         break

#     # Only give hints when the guess is wrong
#     print(compare_difference(random_number, guess))
#     if attempt > 0:
#         print("Guess again.")
#         print(f"You have {attempt} attempts remaining to guess the number.")
#     else:
#         print(f"You've run out of guesses. The number was {random_number}.")
#         print("Refresh the page to run again.")