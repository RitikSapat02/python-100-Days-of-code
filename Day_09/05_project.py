import os
bids = {}

bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    i = input("Are there any other bidders? Type 'yes' or 'no'.")
    if i=="no":
        bidding_finished = True
    elif i== "yes":
        os.system('cls')

highest_bid = 0
winner = ""
for key in bids:
    bid_amount = bids[key]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")

