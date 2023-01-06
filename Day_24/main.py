####read
'''
file = open("Day_24/mytext.txt")
content = file.read()
print(content)
file.close()
'''


###########Or###############
'''
with open("Day_24/mytext.txt") as file:
    content = file.read()
    print(content)
'''


####write
with open("Day_24/newfile.txt",mode="w") as file:
    file.write(" New text.")
