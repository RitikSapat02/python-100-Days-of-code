var_a = 0
programming_dictionary = {
    "bug":"An error in a program that prevents the program from running as expected.",
    "function":"a piece of code that you can easily call over and over again.",
    "Loop":"The action of doing somethng over and over again.",
    var_a : "Ritik",
    "var_a":"Sapat",
    6:6,
}

#retrieving items from dictionary.
# print(var_a)
# print(programming_dictionary[var_a])
# print(programming_dictionary["var_a"])

#Adding new items to dictionary
programming_dictionary["New_item"] = True
print(programming_dictionary)

#empty dictionary
a = {}
a["a"]=1
a["b"]=3

#wipe/clear an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#editing item in dictionary
programming_dictionary['bug']= "A moth in your computer"
# print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])