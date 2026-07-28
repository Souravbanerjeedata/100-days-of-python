
# Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53

# def calculate_love_score(name1, name2):
#     true = 0
#     love = 0
#     input_str = (name1 + name2).lower().strip()
#     for letter in input_str:
#         if letter == 't' or letter == 'r' or letter == 'u' or letter == 'e':
#             true += 1
#         if letter == 'l' or letter == 'o' or letter == 'v' or letter == 'e':
#             love += 1

#     print(str(true) + str(love))

# calculate_love_score("Kanye West", "Kim Kardashian")

# Cesar cypher 1
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(encode_or_decode, original_text, shift_amount):
    output_text = ''
    if encode_or_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(encode_or_decode=direction, original_text=text, shift_amount=shift)
    choice = input("Type 'yes' if you want to go again.\nOtherwise type 'no'.\n").lower()

    if choice == 'no':
        should_continue = False
        print("Goodbye")