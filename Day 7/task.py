# Task 1
# The project is split into 5 major steps. In each step, there will be multiple TODOs. Your goal is to go through each todo in order and complete them.

# TODO-1
# Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2
# Ask the user to guess a letter and assign their answer to a variable called guess. Make the String stored in guess lowercase.

#  Hint 1 
# TODO-3
# Check if the letter the user guessed guess is one of the letters in the chosen_word. Loop through each of the letters in the chosen_word and print "Right" if the letter is a match, "Wrong" if it's not.

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# guess = input("Please guess a letter from the chosen word.\n").lower()
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# task 2
# TODO-1
# Create an empty String called placeholder.
# For each letter in the chosen_word, add a _ to placeholder.
# So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.
# Print out hint.

# TODO-2
# Create an empty string called "display".
# Loop through each letter in the chosen_word
# If the letter at that position matches guess then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
# Print display and you should see the guessed letter in the correct position.
# But every letter that is not a match is represented with a "_".

# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win.")

# Hangman game

# import random
# stages = [r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', r'''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# word_list = ["aardvark", "baboon", "camel"]

# # TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #  Set 'lives' to equal 6.
# lives = 6
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter: ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
#     #  If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in correct_letters:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("You Lose!")
#     if "_" not in display:
#         game_over = True
#         print("You win.")

#     # TODO-3: - print the ASCII art from 'stages'
#     #  that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives])

# Final Hangman game

# import random
# from hangman_words import word_list
# from hangman_art import stages, logo

# # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

# lives = 6

# # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# print(logo)
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("Word to guess: " + placeholder)

# game_over = False
# correct_letters = []

# while not game_over:

#     # TODO-6: - Update the code below to tell the user how many lives they have left.
#     print(f"****************************<???>{lives}/6 LIVES LEFT****************************")
#     guess = input("Guess a letter: ").lower()

#     # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in correct_letters:
#         print(f"You've already guessed {guess}")

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print("Word to guess: " + display)

#     # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#     #  e.g. You guessed d, that's not in the word. You lose a life.

#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")

#         if lives == 0:
#             game_over = True

#             # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
#             print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

#     if "_" not in display:
#         game_over = True
#         print("****************************YOU WIN****************************")

#     # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
#     print(stages[lives])
