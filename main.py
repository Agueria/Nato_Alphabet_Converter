import pandas as pd

class PhoneticConverter:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        self.phonetic_dict = {row.letter: row.code for (index, row) in self.data.iterrows()}
    
    def convert_to_phonetic(self, word):
        word = word.upper()
        try:
            return [self.phonetic_dict[letter] for letter in word]
        except KeyError:
            return "One or more letters not in phonetic dictionary."

# Provide the path to your CSV file (e.g., "nato_phonetic_alphabet.csv")
csv_file = "nato_phonetic_alphabet.csv"
converter = PhoneticConverter(csv_file)

# Take word input from the user
word = input("Enter a word: ")
result = converter.convert_to_phonetic(word)

print(result)
