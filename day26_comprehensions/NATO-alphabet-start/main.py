student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alpha = {row.letter: row.code for index, row in data.iterrows()}
print(nato_alpha)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
output = ""
while True:
    user_word = input("Enter a word: ")
    nato_list = [nato_alpha[code.upper()] for code in user_word]
    print(nato_list)
    if user_word == 'q':
        break
    else:
        for letter in user_word.strip().upper():
            if letter in nato_alpha.keys():
                output += f'{nato_alpha[letter]} '
            else:
                output += '-- '

    print(output)
