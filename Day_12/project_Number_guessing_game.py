import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1,100)

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty_level == 'easy':
    lives = 10
else:
    lives = 5

win = False
while(lives):
    print(f"You have {lives} attempts to guesss the number.")
    guess = int(input("Make a guess: "))
    if(guess>number):
        print("Too high.")
        
    elif(guess < number):
        print("Too Low.")
    else:
        print(f"You win!!, the number was {number}")
        break
    lives-=1
   
    if lives == 0:
        print("You have run out of attempts")
    else:
         print("Guess again")
    

    
    
