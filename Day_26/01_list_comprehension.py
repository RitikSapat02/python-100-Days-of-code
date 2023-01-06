a = [1,2,3,4,5]

square_list = [newitem*2 for newitem in a]
print(square_list)

plus_one_list = [i+1 for i in a]
print(plus_one_list)

name ="Ritik"
name_char_list = [char for char in name]
print(name_char_list)

range_list = [item*2 for item in range(1,5)]
print(range_list)


##conditional list comprehension

even_list = [item for item in range(10) if item%2==0]
print(even_list)

names = ["alexa","paige","saraya","becky","Bayley","nikki","brie","livMorgan","maris"]
names_sort = [name for name in names if len(name)<=5]
print(names_sort)

uppercase_list = [name.upper() for name in names if len(name)<7]
print(uppercase_list)