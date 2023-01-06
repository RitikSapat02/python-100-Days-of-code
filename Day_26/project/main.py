import pandas

data_frame = pandas.read_csv("Day_26/project/nato_alphabet.csv")
mydict = {row.letter:row.code for (index,row) in data_frame.iterrows()}
print(mydict)

word = input("Enter a word: ").upper()

phonetic_code = [mydict[letter] for letter in word]
print(phonetic_code)