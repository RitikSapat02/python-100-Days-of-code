# new_dict = {new_key : new_value for item in list if condition}

# new_dict = {new_key:new_value for (key,value) in dict.items()}

import random
names = ["alexa","paige","saraya","becky","Bayley","nikki","brie","livMorgan","maris"]
names_dict = {name: random.randint(1,100) for name in names}
print(names_dict)


relationship_material = {key:value for (key,value) in names_dict.items() if value >= 60}
print(relationship_material)