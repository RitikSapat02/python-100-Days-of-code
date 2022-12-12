age  = int(input("What is your current age? "))

print("If you live for 90 years then you have left with:")

years_rem = 90 - age
months_rem = years_rem * 12
weeks_rem = years_rem * 52
days_rem  = years_rem *365

print(f"Days = {days_rem}\nweeks = {weeks_rem}\nMonth = {months_rem}\nYears = {years_rem}")