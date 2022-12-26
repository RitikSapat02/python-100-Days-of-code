import random
import os
from art import logo

def choose():
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]
    selected_card = random.choice(cards)
    return selected_card

def score(l):
    total = sum(l)
    if len(l)==2 and total == 21:
        return 0
    if 11 in l and total > 21:
        l.remove(11)
        l.append(1)
    return total

def check_winner(user_score,computer_score):
    if user_score==computer_score:
        return "Draw 🙃"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack 😨"
    elif user_score>21:
        return "You went over. You lose"
    elif computer_score>21:
        return "Opponent went over.You win 😍"
    elif user_score > computer_score:
        return "You win 🤩"
    else:
        return "You lose 😶"

def game():
    user = []
    computer = []

    for _ in range(2):
        user.append(choose())
        computer.append(choose())

    is_game_over = False

    while not is_game_over:
        user_score = score(user)
        computer_score = score(computer)

        print(f"    Your cards:{user}, current_score:{user_score}")
        print(f"    Computer's first card: {computer[0]}")

        if user_score == 0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            i = input("Do you want to draw another card? type 'y' for yes or 'n' for no: ")
            if(i=='y'):
                user.append(choose())
            else:
                is_game_over = True

    while(computer_score!=0 and computer_score<17):
        computer.append(choose())
        computer_score = score(computer)


    print(f"    your final hand: {user}, Final score: {user_score}")
    print(f"    computer's final hand: {computer}, Final score: {computer_score}")
    print(check_winner(user_score,computer_score))


while(input("Do you want to play a game of blackjack? Type 'y' or 'n': ")=='y'):
    os.system('cls')
    print(logo)
    game()