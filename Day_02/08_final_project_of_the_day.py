#Tip Calculator

total_bill = float(input("Enter bill: $"))
per = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
n = int(input("How many people to split the bill? "))

tip = total_bill * per/100

print(f"Tip = {round(tip,2)}\nEach person should pay: ${round((tip+total_bill)/n ,2)}")