import random

test_seed = int(input("Cerate a seed Number: "))
random.seed(test_seed)

namesAsCsv = input("Give me everybody's names,separated by comma.")
names = namesAsCsv.split(',')

# print(names[random.randint(0,len(names)-1)])
#                   or
print(random.choice(names))