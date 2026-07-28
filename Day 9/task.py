#  dictionaries and nesting

#  Task 1:
# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 



# Write a program that converts their scores to grades.



# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 



# The final version of the student_grades dictionary will be checked. 



# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 



# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades ={}

# def convert_score_to_grade(input_list):
#     for key in input_list:
#         if input_list[key] > 90:
#             student_grades[key] = "Outstanding"
#         elif input_list[key] > 80:
#             student_grades[key] = "Exceeds Expectations"
#         elif input_list[key] > 70:
#             student_grades[key] = "Acceptable"
#         else:
#             student_grades[key] = "Fail"

# convert_score_to_grade(input_list=student_scores)
# print(student_grades)

#  Nested dictionaries
## Task 2 ##
# print out "Lille" from the below dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log["France"][1])

## Task 3 ##
# Print out 'D'
# 2D list
# nested_list = ["A","B",["C","D"]]

# print(nested_list[2][1])


## Task 4 ##
# Figure out how to print out "Stuttgart" from the following list:

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits" : 12
#     }, "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5
#     },
# }

# print(travel_log["Germany"]["cities_visited"][2])

## Final Project ##
#  Crreate a secret auction -- rules as mention in the course of day 9

### My Way ##
# bidders = {}
# continue_bidding = True
# bidder_count = 0
# winner_price = 0
# while continue_bidding:
#     bidder = input("What is your name?: ")
#     bid = int(input("What is your bid?: $  "))
#     other_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n    ").lower()
#     # save the data
#     bidder_count += 1
#     bidders[bidder_count] = {"name" : bidder, "price": bid}
#     # decide if continues
#     if other_bidder == 'no':
#         continue_bidding = False

# # calculate the greater bidder
# for key in bidders:
#     if bidders[key]["price"] > winner_price:
#         winner_price = bidders[key]["price"]

# # print out the winner
# for key in bidders:
#     if bidders[key]["price"] == winner_price:
#         winner_name = bidders[key]["name"].title()
#         print(f"The winner is {winner_name} with a bid of ${winner_price}")

### Angela's Way ###
# TODO-1: Ask the user for input
# TODO-2: Save the data into dictionary
# TODO-3: Whether if new bids to be added
# TODO-4: Compare bids in dictionary

def calculate_winner(bidding_dictionary):
    winner_bid = 0
    winner = ''
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > winner_bid:
            winner_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${winner_bid}")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $  "))
    bids[name] = price
    more_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n    ").lower()
    print("\n" * 50)
    if more_bidder == 'no':
        print("\n" * 50)
        continue_bidding = False
        calculate_winner(bids)
    