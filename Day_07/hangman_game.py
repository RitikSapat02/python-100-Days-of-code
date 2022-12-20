import random
from hangman_words import word_list
from hangman_art import logo,stages

import os

print(logo)

choosen_word = random.choice(word_list)
print(choosen_word)
lives = 6

#create  a list with black spaces
length = len(choosen_word)
list_of_blanks = ['_']*length
print(list_of_blanks)
            #  or
# l = []
# for i in choosen_word:
#     l+='_'
# print(l)

while '_' in list_of_blanks:
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    
    if guess not in choosen_word:
      print(f"you guessed {guess}, that's not in the word. you lose a life.")
      lives-=1
      if(lives==0):
            print(stages[lives])
            print("You lose!!")
            break 
    elif guess in list_of_blanks:
      print(f"You've already guessed {guess}")

    for i in range(len(choosen_word)):
        if guess==choosen_word[i]:
            list_of_blanks[i] = guess
    print(list_of_blanks)
    print(stages[lives])

if not '_' in list_of_blanks:
  print("You win!!") 