import random
import pandas
# List comprehension
numbers = [1,2,3]
new_number = [n + 1 for n in numbers]
# print(new_number)

name = "Sourav"
new_list = [letter for letter in name]

num_list = [n * 2 for n in range(1,5)]
# print(num_list)

# Conditional list comprehension
names = ["Alex", "Beth", "Carolina", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)
long_names = [name.upper() for name in names if len(name) >= 5]
# print(long_names)

# Dictionary comprehension
students_score = {student:random.randint(1,100) for student in names}
# print(students_score)
passed_student = {student:score for (student,score) in students_score.items() if score >= 60}
# print(passed_student)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
result = {word:len(word) for word in sentence_list}
# print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day:temp * 9/5 + 32 for (day, temp) in weather_c.items()}
# print(weather_f)

# student_data_frame = pandas.Series(students_score).to_frame(name="Score")
student_data_frame = pandas.DataFrame(list(students_score.items()), columns=["Student", "Score"])
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.Student == 'Carolina':
        print(row.Score)