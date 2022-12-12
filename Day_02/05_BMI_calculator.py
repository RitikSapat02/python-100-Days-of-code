#bmi = weight(kg) / height^2 (m^2)

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight/(height*height)
print(int(bmi))