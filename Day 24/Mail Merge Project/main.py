#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_lines = letter_file.readlines()
with open("./Input/Names/invited_names.txt", "r") as names_file:
    names_list = names_file.readlines()

new_letter_lines = []
for each_word in letter_lines:
    new_letter_lines.append(each_word.strip())
new_names_list = []
for name in names_list:
    new_names_list.append(name.strip())
    
letter = "\n".join(new_letter_lines)

for name in new_names_list:
    new_letter = letter.replace(f"Dear [name],", "Dear {name},")
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
        letter.write(f"{new_letter}")
    
    