student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)
nato_dict = {rows.letter:rows.code for (idx,rows) in nato_data.iterrows()}
# print(nato_dict)
go_on = True
while go_on:
    user_input = input('Enter a word to convert to NATO: ').upper()
    try:
        nato_word_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, please input alphabet letters only.")
    else:
        print(f"NATO Phonetic Alphabet: {', '.join(nato_word_list)}")
        go_on = False