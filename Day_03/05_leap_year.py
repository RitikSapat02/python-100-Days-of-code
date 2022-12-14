year = int(input("Enter a year: "))
if year%4==0 and year%100!=0:
    print("leap year!")
elif year%400==0:
    print("Leap year!")
else:
    print("Not Leap year!")