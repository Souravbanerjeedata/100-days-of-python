#  Primitive Data Types
#  Strings, Integers, Floats, Booleans
# Task 1: From string "Hello", print "o".

# print("Hello"[-1])

# len function can not take number, only takes strings. make it so that it can calculate 12345.
# 1st way
# number = str(12345)
# print(len(number))

# 2nd way
# print(len("12345"))

# Task 2 : check the type of 4 different data types

# print(type(123))
# print(type('123'))
# print(type(123.22))
# print(type(True))

# we can change data types using these functions: str(), int(), float(), bool()
#  Mathematical operators : addition(+), substraction(-), multiplication(*), division(/), exponents(**)
# when dividing something in python the result is automatically a float, it is called implicit typecasting
# to avoid that and to get int when dividing we use '//'
# for prioterise some operator over others we use parenthisis'()'

# Task 3: calculate BMI, if the height is 165 cm and weight is 84 kg.
# bmi formula is weight in kilogram divided by square of (height in m).
# height = 165 / 100
# weight = 84
# bmi = weight / height ** 2
# print(bmi)


# Number manupulation
# to round up a float we use round(number, number of digits)
# Example: round(30.85258, 2) answer: 30.85

#  final task: create a tip calculator

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill?\n$"))
# tip = int(input("how much tip would you like to give? 10, 12 or 15?\n$"))
# people = int(input("How many people to split the bill?\n"))
# total_bill = (tip / 100 * bill) + bill
# result = round((total_bill / people), 2)
# print(f"Each person should pay: ${result}")
