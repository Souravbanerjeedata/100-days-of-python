### Functions with outputs, Docstrings ###

# Task 1:
# Create a function called format_name() that takes two inputs: f_name and l_name. this function should take in first and last name and return full name with first letter in capital for first and last name

# 1st way
# def format_name(f_name, l_name):
#     name_list = [f_name, l_name]
#     full_name = name_list[0] + " " + name_list[1]
#     return full_name.title()

# print(format_name('SoURav', 'BANERjee'))

#2nd way
# def make_a_string(input1, input2):
#     return input1 + ' ' + input2

# def return_a_name(input):
#     return input.title()

# output = return_a_name(make_a_string('soURAV', 'BANERJEE'))
# print(output)

# Edge cases
# def format_name(f_name, l_name):
#     if f_name == '' or l_name =='':
#         return "Please provide a valid name."
#     name_list = [f_name, l_name]
#     full_name = name_list[0] + " " + name_list[1]
#     return f"Result: {full_name.title()}"

# print(format_name(input("What's your first name? "), input("What's your last name? ")))

## Task 2: ##
# Leap Year
# 💪 This is a difficult challenge! 💪 
# Write a program that returns True or False whether if a given year is a leap year.

# A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice

# This is how you work out whether if a particular year is a leap year. 

# - on every year that is divisible by 4 with no remainder

# - except every year that is evenly divisible by 100 with no remainder 

# - unless the year is also divisible by 400 with no remainder   

# If English is not your first language, or if the above logic is confusing, try using this flow chart.

# e.g. The year 2000: 
# 2000 ÷ 4 = 500 (Leap)  
# 2000 ÷ 100 = 20 (Not Leap)  
# 2000 ÷ 400 = 5 (Leap!)  
# So the year 2000 is a leap year. 
# But the year 2100 is not a leap year because: 
# 2100 ÷ 4 = 525 (Leap)  
# 2100 ÷ 100 = 21 (Not Leap)  
# 2100 ÷ 400 = 5.25 (Not Leap)  
# Warning
# Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation. 

# def is_leap_year(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#         else: 
#             return True
#     return False
    
# print(is_leap_year(1989))

# Final challenge: create a calculator

def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

operations = {
    "+": add, 
    "-": substract, 
    "*": multiply, 
    "/": divide
}
def calculator():
    continue_calculating = True
    f_number = float(input("What's the first number?: "))
    while continue_calculating:
        operator = input("+\n-\n*\n/\nPick an operation: ")
        s_number = float(input("What's the next number?: "))
        result = float(operations[operator](f_number, s_number))
        print(f"{f_number} {operator} {s_number} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            f_number = result
        else:
            continue_calculating = False
            print("\n" * 20)
            calculator()

calculator()
