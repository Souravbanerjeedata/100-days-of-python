# List comprehension
numbers = [1,2,3]
new_number = [n + 1 for n in numbers]
# print(new_number)

name = "Sourav"
new_list = [letter for letter in name]

num_list = [n * 2 for n in range(1,5)]
# print(num_list)

# Conditional list comprehension
names = ['Alex', "Beth","Carolina", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)

