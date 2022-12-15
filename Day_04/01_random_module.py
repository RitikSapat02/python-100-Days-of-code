#module
import module
print(module.pi)


import random
# random.seed(321)
#random int
random_integer = random.randint(1,10)
print(random_integer)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")

#random float
random_float = random.random() #0-1
print(random_float)

random_float = random_float * 5 #(0-4.99)
print(random_float)
