from art import logo
from art import vs
from game_data import data
import random
import os


def display_account(account):
    '''format the data '''
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check(follower_a,follower_b,guess):
    '''check the answer'''
    if follower_a > follower_b:
        return guess=='a'
    else:
        return guess=='b'

print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
   
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b :
        account_b = random.choice(data)
  

    print(f"Compare A: {display_account(account_a)}.")
    print(vs)
    print(f"Compare B: {display_account(account_b)}.")

    follower_a = account_a["follower_count"]
    follower_b = account_b["follower_count"]

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    os.system('cls')
    print(logo)
    bool = check(follower_a,follower_b,guess)
    if bool:
        score+=1
        print(f"You're Right!! Current score = {score}")
     
    else:
        game_should_continue = False
        print(f"That's wrong!! Final score = {score}")


