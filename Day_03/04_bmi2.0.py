height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight/(height**2))  #nearest whole number
if(bmi<18.5):
    print(f"your bmi is {bmi}, you are Underweight!")
elif(bmi<25):
    print(f"your bmi is {bmi}, you are Normal weight!")
elif(bmi<30):
    print(f"your bmi is {bmi}, you are Overweight!")
elif(bmi<35):
    print(f"your bmi is {bmi}, you are obese!")
else:
    print(f"your bmi is {bmi}, you are clinically obese!")