#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    letter_content = starting_letter.read()
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.read()
    names_list = names.split("\n")
for name in names_list:
    new_letter = letter_content.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)
