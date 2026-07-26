# Loops allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.

# Syntax
# for <variable name of each item> in <a List>:
#     <do something>
#     <do something else> 
# PAUSE 1 - Be a Computer
# Predict what will be printed from the code below:

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# Indentation
# Indentation is very important in Python programming. Every time you see the : symbol used, you need to be careful about the indentation that comes afterwards.

# e.g. This code will behave very differently

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print("Hello")
# from this code:

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
# print("Hello")

# Sum
# Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

# student_scores = [180, 124, 165, 173, 189, 169, 146]
# total_score = sum(student_scores) 
# But how does sum() work behind the scenes? The code is written by the people who developed Python and it might look something like this:

# student_scores = [180, 124, 165]

# sum = 0
# for score in student_scores:
#     sum += score
    
# print(sum)

# Task : PAUSE 1 - Max
# There are also a built-in Python methods called max() and min(), which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.

# Your job is to figure out how the Python programmers might have built this functionality using loops and conditionals.

# COMPLETE THIS CHALLENGE WITHOUT USING max()
# You are given a list of exam scores, and you have to print out the highest score from the List. You will need to use what you have learnt about Lists, For Loops and Conditionals to print out the highest score in the list of student_scores. For example, if the scores were:

# 8 65 89 86 55 91 64 89
# Your code should print

# 91

# scores = [8, 65, 89, 86, 55, 91, 64, 89]
# highest_score = 0

# for score in scores:
#     if highest_score < score:
#         highest_score = score
    
# print(highest_score)

# The combination of the range() function with the Python For Loop allows us to run a loop for as many times as we wish. Instead of looping through each item in a List, we can loop through a range of numbers.

# Range Function
# range(1, 10)

# This code doesn't do anything by itself. For example, if you tried to print it, it would not give you individual numbers.

# But it can be used in conjunction with For Loops. e.g.

# for number in range(1, 10):
#     print(number)
# This will print out each of the numbers 1 - 9. So the range can also be expressed like this:

# a <= range(a, b) < b

# Where the range of numbers is inclusive of the lower bound but not inclusive of the upper bound.

#  Task: PAUSE 1 - The Gauss Challenge
# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

# 1st option
# newList = []
# for num in range(1, 101):
#     newList.append(num)
# print(sum(newList))

# 2nd option
# total = 0
# for number in range(1,101):
#     total += number
# print(total)

# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:



# Your program should print each number from 1 to 100 in turn and include number 100.



# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".



# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`



# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"



# e.g. it might start off like this:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

# solution:
# for number in range(1,101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print('FizzBuzz')
#     elif number % 3 == 0:
#         print('Fizz')
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)
    

# Final task: Password generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# 1st solution
# password_list = []
# for letter in range(1, nr_letters + 1):
#     random_letters = letters[random.randint(0, len(letters) - 1)]
#     password_list.append(random_letters)
# for symbol in range(1, nr_symbols + 1):
#     random_symbols = symbols[random.randint(0, len(symbols) - 1)]
#     password_list.append(random_symbols)
# for number in range(1, nr_numbers + 1):
#     random_numbers = numbers[random.randint(0, len(numbers) - 1)]
#     password_list.append(random_numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# password = ''.join(password_list)
# print(f"Your password is: {password}")

# 2nd solution
# password= ''
# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# password_list = list(password)
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
# final_password = ''.join(password_list)
# print(f"Your password is: {final_password}")